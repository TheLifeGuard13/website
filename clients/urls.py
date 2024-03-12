from django.urls import path

from clients.apps import ClientsConfig
from clients.views import ClientListView, ClientDetailView, ClientCreateView, ClientUpdateView, ClientDeleteView

app_name = ClientsConfig.name

urlpatterns = [
    path('', ClientListView.as_view(), name='clients_page'),
    path('view_client/<int:pk>/', ClientDetailView.as_view(), name='view_clients'),
    path('add_client/', ClientCreateView.as_view(), name='add_client'),
    path('update_client/<int:pk>/', ClientUpdateView.as_view(), name='update_client'),
    path('delete_client/<int:pk>/', ClientDeleteView.as_view(), name='delete_client')
]
