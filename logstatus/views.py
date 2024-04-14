import typing

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView

from logstatus.models import LogMessage


class LogMessageListView(LoginRequiredMixin, ListView):
    """Контроллер для просмотра сущностей"""
    model = LogMessage
    login_url = reverse_lazy('users:login')

    def get_context_data(self, **kwargs: typing.Any) -> typing.Any:
        context = super().get_context_data(**kwargs)
        context["title"] = "Логи"
        return context

    def get_queryset(self, *args: typing.Any, **kwargs: typing.Any) -> typing.Any:
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(id_mailing=self.kwargs.get("pk"))
        return queryset
