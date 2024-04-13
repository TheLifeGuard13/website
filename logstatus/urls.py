from django.urls import path
from django.views.decorators.cache import cache_page

from logstatus.apps import LogstatusConfig
from logstatus.views import LogMessageListView

app_name = LogstatusConfig.name

urlpatterns = [
    path('view_log/<int:pk>/', cache_page(60)(LogMessageListView.as_view()), name='logs_page')
]
