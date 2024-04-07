import random

from django.views.generic import ListView

from blog.models import Blog


class WebsiteListView(ListView):
    model = Blog
    template_name = 'website/homepage.html'

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        return queryset.order_by('?')[:3]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        return context
