import typing

from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic import ListView

from blog.models import Blog


class BlogListView(UserPassesTestMixin, ListView):
    """Контроллер для просмотра сущностей"""
    model = Blog
    template_name = "blog/index.html"

    def get_context_data(self, **kwargs: typing.Any) -> typing.Any:
        context = super().get_context_data(**kwargs)
        context["title"] = "Блоги"
        return context

    def test_func(self) -> typing.Any:
        return self.request.user.is_staff
