from django.shortcuts import render

from datetime import datetime
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from .forms import CustomLoginForm, CustomSignUpForm


# Create your views here.
class SignupView(CreateView):
    form_class = CustomSignUpForm
    template_name = "home/register.html"
    success_url = "/smart/notes"

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect("notes.list")
        return super().get(request, *args, **kwargs)


class LoginInterfaceView(LoginView):
    form_class = CustomLoginForm
    redirect_authenticated_user = True
    template_name = "home/login.html"


class LogoutInterfaceView(LogoutView):
    template_name = "home/logout.html"


class HomeView(TemplateView):
    template_name = "home/welcome.html"
    extra_context = {"today": datetime.today()}


class AuthorizedView(LoginRequiredMixin, TemplateView):
    template_name = "home/authorized.html"
    login_url = "/admin"
