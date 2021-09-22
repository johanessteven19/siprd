from django.urls import path
from . import views

app_name = "main"   


urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("register", views.register_request, name="register"),
    path("login", views.login_request, name="login"),
    path("ping", views.ping, name="ping"),
    path("api/register", views.APIViewRegister.as_view()),
    path("api/login", views.APIViewLogin.as_view())
]