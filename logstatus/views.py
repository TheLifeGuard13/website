from django.views.generic import ListView

from logstatus.models import LogMessage


class LogMessageListView(ListView):
    model = LogMessage

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Логи'
        return context

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(id_mailing=self.kwargs.get('pk'))
        return queryset
