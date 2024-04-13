from django.urls import path
from django.views.decorators.cache import cache_page

from letters.apps import MessagesConfig
from letters.views import LetterListView, LetterDetailView, LetterCreateView, LetterUpdateView, LetterDeleteView

app_name = MessagesConfig.name

urlpatterns = [
    path('', cache_page(60)(LetterListView.as_view()), name='letters_page'),
    path('view_letter/<int:pk>/', cache_page(60)(LetterDetailView.as_view()), name='view_letter'),
    path('add_letter/', LetterCreateView.as_view(), name='add_letter'),
    path('update_letter/<int:pk>/', LetterUpdateView.as_view(), name='update_letter'),
    path('delete_letter/<int:pk>/', LetterDeleteView.as_view(), name='delete_letter')
]
