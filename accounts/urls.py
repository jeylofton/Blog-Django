from django.urls import path
from .views import SignUpView, LogoutGetView

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("logout/", LogoutGetView.as_view(), name="logout"),
]
