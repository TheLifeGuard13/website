import typing

from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import ListView

from blog.models import Blog
from clients.models import Client
from mailing.models import Mailing
from mailing.services import get_cache_clients_count, get_cache_mailing_active, get_cache_mailing_count
from users.models import User


class WebsiteListView(ListView):
    """Контроллер для просмотра сущностей"""
    model = Blog
    template_name = "website/homepage.html"

    def get_queryset(self, *args: typing.Any, **kwargs: typing.Any) -> typing.Any:
        queryset = super().get_queryset(*args, **kwargs)
        return queryset.order_by("?")[:3]

    def get_context_data(self, **kwargs: typing.Any) -> typing.Any:
        context = super().get_context_data(**kwargs)

        context["title"] = "Главная страница"
        context["mailing_amount"] = get_cache_mailing_count()
        context["mailing_active"] = get_cache_mailing_active()
        context["clients_amount"] = get_cache_clients_count()
        return context


class ManagerListView(UserPassesTestMixin, ListView):
    """Контроллер для просмотра сущностей"""
    model = User
    template_name = "website/manager.html"

    def test_func(self) -> typing.Any:
        return self.request.user.is_staff

    def get_queryset(self, *args: typing.Any, **kwargs: typing.Any) -> typing.Any:
        queryset = super().get_queryset(*args, **kwargs)
        user = self.request.user
        if user.is_superuser:
            queryset = queryset
        else:
            queryset = queryset.filter(is_staff=False)
        return queryset


def toggle_activity(request: typing.Any, pk: int) -> typing.Any:
    """Контроллер для изменения статуса сущности"""
    user_activity = get_object_or_404(User, pk=pk)
    if user_activity.is_active:
        user_activity.is_active = False
    else:
        user_activity.is_active = True
    user_activity.save()

    return redirect(reverse("website:manager"))
