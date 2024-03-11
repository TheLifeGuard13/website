from django.urls import path

from website.apps import WebsiteConfig
from website.views import index

app_name = WebsiteConfig.name

urlpatterns = [
    path('', index, name='homepage')
]
