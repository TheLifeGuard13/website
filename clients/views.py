from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from clients.models import Client


class ClientListView(ListView):
    model = Client

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Клиенты'
        return context


class ClientDetailView(DetailView):
    model = Client

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.object.name
        return context


class ClientCreateView(CreateView):
    model = Client
    fields = ('email', 'name', 'avatar', 'created_at', 'comment',)
    success_url = reverse_lazy('clients:clients_page')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Добавление клиента'
        return context


class ClientUpdateView(UpdateView):
    model = Client
    fields = ('email', 'name', 'avatar', 'created_at', 'comment',)

    def get_success_url(self):
        return reverse('clients:view_client', args=[self.kwargs.get('pk')])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Обновление данных клиента'
        return context


class ClientDeleteView(DeleteView):
    model = Client
    success_url = reverse_lazy('clients:blog_homepage')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Удаление данных клиента'
        return context
