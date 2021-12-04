from django.urls import path, include, re_path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)

from .views import RequestPasswordResetEmail, PasswordTokenCheckAPI, SetNewPasswordAPIView

app_name = "main"

urlpatterns = [
    path("ping", views.ping, name="ping"),
    path("api/register", views.Register.as_view()),
    path("api/user", views.ViewUserData.as_view()),
    path("api/ping", views.ping_auth),
    path("api/get-linked-users/", views.GetLinkedUsers.as_view()),
    path("api/get-karil-summary/", views.GetLinkedKarils.as_view()),
    path("api/manage-users/", views.ManageUsers.as_view()),
    path("api/manage-karil/", views.ManageKaril.as_view()),
    path("api/download", views.DownloadKaril.as_view()),
    path("api/download-review-form", views.DownloadReviewForm.as_view()),
    path("api/upload-review-form", views.UploadReviewForm.as_view()),
    # path("api/get-all-reviews", views.GetAllReviews.as_view()), --> only for debugging, can be deleted
    path('api/google/', include('rest_social_auth.urls_jwt_pair')),
    path(r'^auth/', include('rest_framework_social_oauth2.urls')),
    path("api/is-user-exists", views.IsUserExist.as_view()),

    # Review form Management
    path("api/manage-reviews/", views.ManageReviewForm.as_view()),
    path("api/get-review-form/", views.GetSpecificReviewForm.as_view()),
    path("api/manage-reviewers/", views.ManageReviewers.as_view()),
    path("api/assign-reviewer/", views.AssignReviewer.as_view()),
    path("api/get-assigned-karils/", views.GetAssignedKarils.as_view()),

    # Review management
    # I am so sorry for the confusing naming
    # Expected path: api/manage-karil-reviews?id=<review_id to get>
    re_path(r"^api\/manage-karil-reviews(\?id=(?P<id>.+))?.?$", views.ManageKarilReview.as_view()),
    # Expected path: api/get-linked-reviews?id=<karil_id>
    re_path(r"^api\/get-linked-reviews(\?id=(?P<id>.+))?.?$", views.GetLinkedReviews.as_view()),

    path("api/approve-user/", views.ApproveUsers.as_view()),
    
    # Reset password endpoints
    path('api/request-reset-email/', RequestPasswordResetEmail.as_view(), name="request-reset-email"),
    path('api/password-reset/<uidb64>/<token>/<username>', PasswordTokenCheckAPI.as_view(), name='password-reset-confirm'),
    path('api/password-reset-complete', SetNewPasswordAPIView.as_view(), name='password-reset-complete'),

    # NOTE: Grants users a Refresh-Access token pair.
    # Input: JSON file containing username and password
    # Refresh Token to be stored in local storage
    # Access Token to be stored as a cookie
    # Access Token needed to access views which have the permission_classes variable set as [IsAuthenticated]
    path("api/token/", TokenObtainPairView.as_view(), name='token_obtain_pair'),

    # NOTE: Grants the user a new Access token using their existing refresh token
    # If user's Refresh token has expired, they will be logged out
    path("api/token/refresh/", TokenRefreshView.as_view(), name='token_refresh'),

   
]
