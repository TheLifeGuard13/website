from django.urls import path

from website.apps import WebsiteConfig
from website.views import WebsiteListView, toggle_activity, ManagerListView

app_name = WebsiteConfig.name

urlpatterns = [
    path('', WebsiteListView.as_view(), name='homepage'),
    path('manager/', ManagerListView.as_view(), name='manager'),
    path('activity/<int:pk>/', toggle_activity, name='managerpage')
]
