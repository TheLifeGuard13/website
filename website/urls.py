from django.urls import path
from django.views.decorators.cache import cache_page

from website.apps import WebsiteConfig
from website.views import WebsiteListView, toggle_activity, ManagerListView

app_name = WebsiteConfig.name

urlpatterns = [
    path('', cache_page(60)(WebsiteListView.as_view()), name='homepage'),
    path('manager/', cache_page(60)(ManagerListView.as_view()), name='manager'),
    path('activity/<int:pk>/', toggle_activity, name='managerpage')
]
