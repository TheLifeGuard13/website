from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from mailing.forms import MailingForm
from mailing.models import Mailing
from mailing.services import start_mailing


class MailingListView(LoginRequiredMixin, ListView):
    model = Mailing
    login_url = reverse_lazy("website:homepage")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Рассылки"
        return context

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        user = self.request.user
        if user.groups.filter(name="manager") or user.is_superuser:
            queryset = queryset
        else:
            queryset = queryset.filter(owner=self.request.user)
        return queryset


class MailingDetailView(DetailView):
    model = Mailing

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        # if self.object.status == 'Готовится':
        #     start_mailing(self.object)
        # self.object.status = 'Успешно'
        # self.object.save()

        user = self.request.user
        if not user.is_superuser and self.object.owner != user and not user.groups.filter(name="manager"):
            raise Http404("Доступ запрещен")
        return self.object

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = self.object.name
        return context


class MailingCreateView(CreateView):
    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy("mailing:mailing_page")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Добавление рассылки"
        return context

    def form_valid(self, form):
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save()
        return super().form_valid(form)

    def test_func(self):
        return not self.request.user.groups.filter(name="manager")


class MailingUpdateView(LoginRequiredMixin, UpdateView):
    model = Mailing
    form_class = MailingForm
    login_url = reverse_lazy("website:homepage")

    def get_success_url(self):
        return reverse("mailing:view_mailing", args=[self.kwargs.get("pk")])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Обновление рассылки"
        return context

    def test_func(self):
        custom_perms = ("mailing.set_inactive",)
        if self.request.user.groups.filter(name="manager") and self.request.user.has_perms(custom_perms):
            return True
        return self.handle_no_permission()

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        user = self.request.user
        if not user.is_superuser and self.object.owner != user:
            raise Http404("Доступ запрещен")
        return self.object


class MailingDeleteView(DeleteView):
    model = Mailing
    success_url = reverse_lazy("mailing:mailing_page")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Удаление рассылки"
        return context

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        user = self.request.user
        if not user.is_superuser and self.object.owner != user:
            raise Http404("Доступ запрещен")
        return self.object


def toggle_activity(request, pk):
    mailing_status = get_object_or_404(Mailing, pk=pk)
    if mailing_status.is_active:
        mailing_status.is_active = False
    else:
        mailing_status.is_active = True
    mailing_status.save()

    return redirect(reverse("mailing:mailing_page"))
