import typing

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import Http404
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from clients.forms import ClientForm
from clients.models import Client


class ClientListView(LoginRequiredMixin, ListView):
    """Контроллер для просмотра сущностей"""

    model = Client
    login_url = reverse_lazy("website:homepage")

    def get_context_data(self, **kwargs: typing.Any) -> typing.Any:
        context = super().get_context_data(**kwargs)
        context["title"] = "Клиенты"
        return context

    def get_queryset(self, *args: typing.Any, **kwargs: typing.Any) -> typing.Any:
        queryset = super().get_queryset(*args, **kwargs)
        user = self.request.user
        if user.is_superuser:
            queryset = queryset
        else:
            queryset = queryset.filter(owner=self.request.user)
        return queryset


class ClientDetailView(DetailView):
    """Контроллер для просмотра сущности"""

    model = Client

    def get_context_data(self, **kwargs: typing.Any) -> typing.Any:
        context = super().get_context_data(**kwargs)
        context["title"] = self.object.name
        return context

    def get_object(self, queryset: typing.Any = None) -> typing.Any:
        self.object = super().get_object(queryset)
        user = self.request.user
        if not user.is_superuser and self.object.owner != user:
            raise Http404("Доступ запрещен")
        return self.object


class ClientCreateView(UserPassesTestMixin, CreateView):
    """Контроллер для создания сущности"""

    model = Client
    form_class = ClientForm
    success_url = reverse_lazy("clients:clients_page")

    def get_context_data(self, **kwargs: typing.Any) -> typing.Any:
        context = super().get_context_data(**kwargs)
        context["title"] = "Добавление клиента"
        return context

    def form_valid(self, form: typing.Any) -> typing.Any:
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save()
        return super().form_valid(form)

    def test_func(self) -> typing.Any:
        return not self.request.user.groups.filter(name="manager")


class ClientUpdateView(UpdateView):
    """Контроллер для изменения сущности"""

    model = Client
    form_class = ClientForm

    def get_success_url(self) -> typing.Any:
        return reverse("clients:view_client", args=[self.kwargs.get("pk")])

    def get_context_data(self, **kwargs: typing.Any) -> typing.Any:
        context = super().get_context_data(**kwargs)
        context["title"] = "Обновление данных клиента"
        return context

    def get_object(self, queryset: typing.Any = None) -> typing.Any:
        self.object = super().get_object(queryset)
        user = self.request.user
        if not user.is_superuser and self.object.owner != user:
            raise Http404("Доступ запрещен")
        return self.object


class ClientDeleteView(DeleteView):
    """Контроллер для удаления сущности"""

    model = Client
    success_url = reverse_lazy("clients:clients_page")

    def get_context_data(self, **kwargs: typing.Any) -> typing.Any:
        context = super().get_context_data(**kwargs)
        context["title"] = "Удаление данных клиента"
        return context

    def get_object(self, queryset: typing.Any = None) -> typing.Any:
        self.object = super().get_object(queryset)
        user = self.request.user
        if not user.is_superuser and self.object.owner != user:
            raise Http404("Доступ запрещен")
        return self.object
