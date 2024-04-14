from django.urls import path
from django.views.decorators.cache import cache_page

from mailing.apps import MailingConfig
from mailing.views import (MailingCreateView, MailingDeleteView, MailingDetailView, MailingListView, MailingUpdateView,
                           toggle_activity)

app_name = MailingConfig.name

urlpatterns = [
    path("", cache_page(60)(MailingListView.as_view()), name="mailing_page"),
    path("view_mailing/<int:pk>/", MailingDetailView.as_view(), name="view_mailing"),
    path("add_mailing/", MailingCreateView.as_view(), name="add_mailing"),
    path("update_mailing/<int:pk>/", MailingUpdateView.as_view(), name="update_mailing"),
    path("delete_mailing/<int:pk>/", MailingDeleteView.as_view(), name="delete_mailing"),
    path("activity/<int:pk>/", toggle_activity, name="toggle_activity"),
]
