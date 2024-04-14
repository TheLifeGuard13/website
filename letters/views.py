from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import Http404
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from letters.forms import LetterForm
from letters.models import Letter


class LetterListView(LoginRequiredMixin, ListView):
    model = Letter
    login_url = reverse_lazy("website:homepage")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Письма"
        return context

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        user = self.request.user
        if user.is_superuser:
            queryset = queryset
        else:
            queryset = queryset.filter(owner=self.request.user)
        return queryset


class LetterDetailView(DetailView):
    model = Letter

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = self.object
        return context

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        user = self.request.user
        if not user.is_superuser and self.object.owner != user:
            raise Http404("Доступ запрещен")
        return self.object


class LetterCreateView(UserPassesTestMixin, CreateView):
    model = Letter
    form_class = LetterForm
    success_url = reverse_lazy("letters:letters_page")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Добавление письма"
        return context

    def form_valid(self, form):
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save()
        return super().form_valid(form)

    def test_func(self):
        return not self.request.user.groups.filter(name="manager")


class LetterUpdateView(UpdateView):
    model = Letter
    form_class = LetterForm

    def get_success_url(self):
        return reverse("letters:view_letter", args=[self.kwargs.get("pk")])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Обновление письма"
        return context


class LetterDeleteView(DeleteView):
    model = Letter
    success_url = reverse_lazy("letters:letters_page")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Удаление письма"
        return context

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        user = self.request.user
        if not user.is_superuser and self.object.owner != user:
            raise Http404("Доступ запрещен")
        return self.object
