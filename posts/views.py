from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .models import Post, Status

# Create your views here.
class PostListView(ListView):
    template_name = "postsTemplates/list.html"
    model = Post
    context_object_name = "posts"

    def get_queryset(self):
        status = Status.objects.get(name="Published")
        return Post.objects.filter(status=status).order_by("created_on")


class PostDraftListView(LoginRequiredMixin, ListView):
    template_name = "postsTemplates/list.html"
    model = Post
    context_object_name = "posts"

    def get_queryset(self):
        status = Status.objects.get(name="Draft")
        return Post.objects.filter(
            status=status,
            author=self.request.user
        ).order_by("created_on")


class PostArchivedListView(LoginRequiredMixin, ListView):
    template_name = "postsTemplates/list.html"
    model = Post
    context_object_name = "posts"

    def get_queryset(self):
        status = Status.objects.get(name="Archived")
        return Post.objects.filter(
            status=status,
            author=self.request.user
        ).order_by("created_on")


class PostDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    template_name = "postsTemplates/detail.html"
    model = Post
    context_object_name = "single_post"

    def test_func(self):
        return self.request.user.is_superuser

class PostCreateView(LoginRequiredMixin, CreateView):
        template_name = "postsTemplates/new.html"
        model = Post
        fields = ["title", 'subtitle', "body", "status"]

        def form_valid(self, form):
            form.instance.author = self.request.user
            return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = "postsTemplates/edit.html"
    model = Post
    fields =["title", "subtitle", "body", "status"]

    def test_func(self):
        return self.get_object().author == self.request.user

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    template_name = "postsTemplates/delete.html"
    model = Post
    success_url = reverse_lazy("post_list")

    def test_func(self):
        return self.get_object().author == self.request.user
