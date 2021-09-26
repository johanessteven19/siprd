from django.urls import path, include
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)

app_name = "main"   


urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("ping", views.ping, name="ping"),
    path("api/register", views.Register.as_view()),
    path("api/user", views.ViewUserData.as_view()),
    path("api/ping", views.pingAuth),
    path('api/google', include('djoser.social.urls')),
    #path('accounts/profile/', RedirectSocial.as_view()),

    # NOTE: Grants users a Refresh-Access token pair.
    # Input: JSON file containing username and password
    # Refresh Token to be stored in local storage
    # Access Token to be stored as a cookie
    # Access Token needed to access views which have the permission_classes variable set as [IsAuthenticated]
    path("api/token/", TokenObtainPairView.as_view(), name='token_obtain_pair'),

    # NOTE: Grants the user a new Access token using their existing refresh token
    # If user's Refresh token has expired, they will be logged out
    path("api/token/refresh/", TokenRefreshView.as_view(), name='token_refresh')
]