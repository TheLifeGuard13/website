from django.urls import path
from django.views.decorators.cache import cache_page

from website.apps import WebsiteConfig
from website.views import ManagerListView, WebsiteListView, toggle_activity

app_name = WebsiteConfig.name

urlpatterns = [
    path("", WebsiteListView.as_view(), name="homepage"),
    path("manager/", ManagerListView.as_view(), name="manager"),
    path("activity/<int:pk>/", toggle_activity, name="managerpage"),
]
