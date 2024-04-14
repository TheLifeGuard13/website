import typing

from django.contrib.auth import logout
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, TemplateView, UpdateView

from users.forms import UserProfileForm, UserRegisterForm
from users.models import User
from users.services import get_generated_key, send_key_mail, send_password_mail


def logout_view(request: typing.Any) -> typing.Any:
    """Контроллер для выхода из авторизации пользователя"""
    logout(request)
    return redirect("/")


class RegisterView(CreateView):
    """Контроллер для регистрации пользователя"""

    model = User
    form_class = UserRegisterForm
    template_name = "users/register.html"

    def form_valid(self, form: typing.Any) -> typing.Any:
        new_user = form.save()
        current_site = self.request.get_host()
        new_user.is_active = False
        new_user.auth_token = get_generated_key(5)
        new_user.save()
        send_key_mail(new_user.auth_toke, current_site, new_user.email)

        return super().form_valid(form)

    def get_context_data(self, **kwargs: typing.Any) -> typing.Any:
        context = super().get_context_data(**kwargs)
        context["title"] = "Регистрация"
        return context

    def get_success_url(self) -> typing.Any:
        return reverse("users:verification")


class ProfileView(UpdateView):
    """Контроллер для просмотра профиля пользователя"""

    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy("users:profile")

    def get_object(self, queryset: typing.Any = None) -> typing.Any:
        return self.request.user

    def get_context_data(self, **kwargs: typing.Any) -> typing.Any:
        context = super().get_context_data(**kwargs)
        context["title"] = "Мой профиль"
        return context


class Verification(TemplateView):
    """Контроллер для верификации пользователя"""

    def get(self, request: typing.Any, *args: typing.Any, **kwargs: typing.Any) -> typing.Any:
        return render(request, "users/verification.html")

    def post(self, request: typing.Any, *args: typing.Any, **kwargs: typing.Any) -> typing.Any:
        code = request.POST.get("auth_token")
        user = get_object_or_404(User, auth_token=code)

        if not user.is_active:
            user.is_active = True
            user.save()
        return redirect("users:login")


class RestorePassword(TemplateView):
    """Контроллер для восстановления пароля пользователя"""

    def get(self, request: typing.Any, *args: typing.Any, **kwargs: typing.Any) -> typing.Any:
        return render(request, "users/new_password.html")

    def post(self, request: typing.Any, *args: typing.Any, **kwargs: typing.Any) -> typing.Any:
        mail = request.POST.get("email")
        user = get_object_or_404(User, email=mail)
        new_password = get_generated_key(15)
        send_password_mail(new_password, user.email)
        user.set_password(new_password)
        user.save()
        return redirect("users:login")
