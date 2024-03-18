from django.forms import TimeInput, ModelForm, DateTimeInput
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from mailing.models import Mailing
from mailing.services import start_mailing


class MailingForm(ModelForm):
    class Meta:
        model = Mailing
        fields = ('name', 'client_emails', 'period', 'letter', 'first_sending_time', 'start_datetime', 'end_datetime',)
        widgets = {
            'first_sending_time': DateTimeInput(attrs={'type': 'datetime-local'}),
            'start_datetime': DateTimeInput(attrs={'type': 'datetime-local'}),
            'end_datetime': DateTimeInput(attrs={'type': 'datetime-local'}),
        }
        labels = {
            'sending_time': 'Время рассылки',
            'start_datetime': 'Время начала',
            'end_datetime': 'Время конца',
        }


class MailingListView(ListView):
    model = Mailing

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Рассылки'
        return context


class MailingDetailView(DetailView):
    model = Mailing

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        # if self.object.status == 'Готовится':
        #     start_mailing(self.object)
        # self.object.status = 'Успешно'
        # self.object.save()
        return self.object

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.object.name
        return context


class MailingCreateView(CreateView):
    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy('mailing:mailing_page')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Добавление рассылки'
        return context


class MailingUpdateView(UpdateView):
    model = Mailing
    form_class = MailingForm

    def get_success_url(self):
        return reverse('mailing:view_mailing', args=[self.kwargs.get('pk')])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Обновление рассылки'
        return context


class MailingDeleteView(DeleteView):
    model = Mailing
    success_url = reverse_lazy('mailing:mailing_page')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Удаление рассылки'
        return context


def toggle_activity(request, pk):
    mailing_status = get_object_or_404(Mailing, pk=pk)
    if mailing_status.is_active:
        mailing_status.is_active = False
    else:
        mailing_status.is_active = True
    mailing_status.save()

    return redirect(reverse('mailing:mailing_page'))
