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

class PostCreateView(CreateView):
        template_name = "postsTemplates/new.html"
        model = Post
        fields = ["title", 'subtitle', "body"]

        def form_valid(self, form):
            form.instance.author = User.objects.last()
            return super().form_valid(form)

class PostUpdateView(UpdateView):
    template_name = "postsTemplates/edit.html"
    model = Post
    fields =["title", "subtitle", "body"]

class PostDeleteView(DeleteView):
    template_name = "postsTemplates/delete.html"
    model = Post
    success_url = reverse_lazy("post_list")