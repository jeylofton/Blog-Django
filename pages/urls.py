from django.urls import path

from . import views

# Each path() connects a URL address to a view function.
# The name= is a nickname you can use in templates and code.
urlpatterns = [
    path("", views.home, name="home"),          # http://127.0.0.1:8000/
    path("about/", views.about, name="about"),  # http://127.0.0.1:8000/about/
]
