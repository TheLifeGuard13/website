from django.urls import path
from django.views.decorators.cache import cache_page

from clients.apps import ClientsConfig
from clients.views import ClientCreateView, ClientDeleteView, ClientDetailView, ClientListView, ClientUpdateView

app_name = ClientsConfig.name

urlpatterns = [
    path("", cache_page(60)(ClientListView.as_view()), name="clients_page"),
    path("view_client/<int:pk>/", ClientDetailView.as_view(), name="view_client"),
    path("add_client/", ClientCreateView.as_view(), name="add_client"),
    path("update_client/<int:pk>/", ClientUpdateView.as_view(), name="update_client"),
    path("delete_client/<int:pk>/", ClientDeleteView.as_view(), name="delete_client"),
]
