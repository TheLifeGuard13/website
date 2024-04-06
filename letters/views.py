from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from letters.forms import LetterForm
from letters.models import Letter


class LetterListView(ListView):
    model = Letter

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Письма'
        return context


class LetterDetailView(DetailView):
    model = Letter

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.object
        return context


class LetterCreateView(CreateView):
    model = Letter
    form_class = LetterForm
    success_url = reverse_lazy('letters:letters_page')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Добавление письма'
        return context


class LetterUpdateView(UpdateView):
    model = Letter
    form_class = LetterForm

    def get_success_url(self):
        return reverse('letters:view_letter', args=[self.kwargs.get('pk')])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Обновление письма'
        return context


class LetterDeleteView(DeleteView):
    model = Letter
    success_url = reverse_lazy('letters:letters_page')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Удаление письма'
        return context

