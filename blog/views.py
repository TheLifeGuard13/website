from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic import ListView

from blog.models import Blog


class BlogListView(UserPassesTestMixin, ListView):
    model = Blog
    template_name = "blog/index.html"

    def test_func(self):
        return self.request.user.is_staff
