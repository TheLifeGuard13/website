from django.urls import path
from django.views.decorators.cache import cache_page

from letters.apps import MessagesConfig
from letters.views import LetterCreateView, LetterDeleteView, LetterDetailView, LetterListView, LetterUpdateView

app_name = MessagesConfig.name

urlpatterns = [
    path("", cache_page(60)(LetterListView.as_view()), name="letters_page"),
    path("view_letter/<int:pk>/", LetterDetailView.as_view(), name="view_letter"),
    path("add_letter/", LetterCreateView.as_view(), name="add_letter"),
    path("update_letter/<int:pk>/", LetterUpdateView.as_view(), name="update_letter"),
    path("delete_letter/<int:pk>/", LetterDeleteView.as_view(), name="delete_letter"),
]
