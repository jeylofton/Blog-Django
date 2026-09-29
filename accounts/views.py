from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LogoutView
from django.views.generic import CreateView
from django.urls import reverse_lazy

# Create your views here.
class SignUpView(CreateView):
    template_name = "registration/signup.html"


    from_class = UserCreationForm
    success_url = reverse_lazy("login")


class LogoutGetView(LogoutView):
    # Django 5+ only allows POST for logout; this also lets a plain link (GET) log out.
    http_method_names = ["get", "post", "options"]

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
