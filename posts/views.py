from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.urls import reverse_lazy
from .models import Post
from django.contrib.auth.models import User

# Create your views here.
class PostListView(ListView):
    template_name = "postsTemplates/list.html"

    model = Post

    context_object_name = "posts"

class PostDetailView(DetailView):
    template_name = "poststemplates/detail.html"
    model = Post
    context_object_name = "single_post"