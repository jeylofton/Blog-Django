from django.urls import path

from .views import HomePageView, AboutPageView

# Each path() connects a URL address to a view function.
# The name= is a nickname you can use in templates and code.
urlpatterns = [
    path("", HomePageView.as_view(), name="home"),          # http://127.0.0.1:8000/
    path("about/", AboutPageView.as_view(), name="about"),  # http://127.0.0.1:8000/about/
]
