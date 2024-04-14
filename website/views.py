from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import ListView

from blog.models import Blog
from clients.models import Client
from mailing.models import Mailing
from users.models import User


class WebsiteListView(ListView):
    model = Blog
    template_name = "website/homepage.html"

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        return queryset.order_by("?")[:3]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Главная страница"
        context["mailing_amount"] = Mailing.objects.count()
        context["mailing_active"] = Mailing.objects.filter(is_active=True).count()
        context["clients_amount"] = Client.objects.distinct().count()
        return context


class ManagerListView(UserPassesTestMixin, ListView):
    model = User
    template_name = "website/manager.html"

    def test_func(self):
        return self.request.user.is_staff


def toggle_activity(request, pk):
    user_activity = get_object_or_404(User, pk=pk)
    if user_activity.is_active:
        user_activity.is_active = False
    else:
        user_activity.is_active = True
    user_activity.save()

    return redirect(reverse("website:manager"))
