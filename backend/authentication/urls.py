from django.urls import include, path
from dj_rest_auth.registration.views import VerifyEmailView
from . import views

urlpatterns = [
    # dj-rest-auth endpoints
    path("", include("dj_rest_auth.urls")),
    path("registration/", include("dj_rest_auth.registration.urls")),
    path('dj-rest-auth/account-confirm-email/', VerifyEmailView.as_view(), name='account_email_verification_sent'),
    # Custom endpoints
    path("user/", views.user_info, name="user-info"),
    path("user/delete/", views.delete_account, name="delete-account"),
]
