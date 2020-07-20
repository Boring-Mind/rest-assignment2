from django.views import generic
from django.contrib.auth import views as auth_views
from user.forms import LoginForm


class HomeView(generic.TemplateView):
    template_name = "html/base.html"


class LoginView(auth_views.LoginView):
    template_name = 'html/login.html'
    form_class = LoginForm
