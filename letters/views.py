from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from letters.models import Letter


class LetterListView(ListView):
    model = Letter

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Письма-рассылки'
        return context


class LetterDetailView(DetailView):
    model = Letter

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.object.name
        return context


class LetterCreateView(CreateView):
    model = Letter
    fields = ('letter_header', 'letter_body',)
    success_url = reverse_lazy('letters:letters_page')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Добавление письма-рассылки'
        return context


class LetterUpdateView(UpdateView):
    model = Letter
    fields = ('letter_header', 'letter_body',)

    def get_success_url(self):
        return reverse('letters:view_letter', args=[self.kwargs.get('pk')])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Обновление письма-рассылки'
        return context


class LetterDeleteView(DeleteView):
    model = Letter
    success_url = reverse_lazy('letters:letters_page')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Удаление письма-рассылки'
        return context

