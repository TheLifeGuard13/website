from django.urls import path

from website.apps import WebsiteConfig
from website.views import WebsiteListView

app_name = WebsiteConfig.name

urlpatterns = [
    path('', WebsiteListView.as_view(), name='homepage')
]
