from django.urls import path

from mailing.views import MailingListView, MailingDetailView, MailingCreateView, MailingUpdateView, MailingDeleteView
from mailing.apps import MailingConfig

app_name = MailingConfig.name

urlpatterns = [
    path('', MailingListView.as_view(), name='mailing_page'),
    # path('view_mailing/<int:pk>/', MailingDetailView.as_view(), name='view_mailing'),
    # path('add_mailing/', MailingCreateView.as_view(), name='add_mailing'),
    # path('update_mailing/<int:pk>/', MailingUpdateView.as_view(), name='update_mailing'),
    # path('delete_mailing/<int:pk>/', MailingDeleteView.as_view(), name='delete_mailing')
]
