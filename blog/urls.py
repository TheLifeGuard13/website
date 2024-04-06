from django.urls import path

from blog.apps import BlogConfig
from blog.views import index

app_name = BlogConfig.name

urlpatterns = [
    path('', index, name='blog_page')
]
