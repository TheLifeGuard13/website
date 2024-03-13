from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from mailing.models import Mailing


class MailingListView(ListView):
    model = Mailing

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Рассылки'
        return context

#
# class MailingDetailView(DetailView):
#     model = Mailing
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title'] = self.object
#         return context
#
#
# class MailingCreateView(CreateView):
#     model = Mailing
#     fields = ('letter_header', 'letter_body',)
#     success_url = reverse_lazy('mailing:letters_page')
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title'] = 'Добавление письма-рассылки'
#         return context
#
#
# class MailingUpdateView(UpdateView):
#     model = Mailing
#     fields = ('letter_header', 'letter_body',)
#
#     def get_success_url(self):
#         return reverse('mailing:view_letter', args=[self.kwargs.get('pk')])
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title'] = 'Обновление письма-рассылки'
#         return context
#
#
# class MailingDeleteView(DeleteView):
#     model = Mailing
#     success_url = reverse_lazy('mailing:letters_page')
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title'] = 'Удаление письма-рассылки'
#         return context

