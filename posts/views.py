from django.views import View
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    FormView
)
from django.views.generic.detail import SingleObjectMixin
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Q
from django.urls import reverse, reverse_lazy
from .models import Post
from .forms import CommentForm


def visible_posts(user):
    """Posts this user may open: everything except other people's drafts."""
    return Post.objects.filter(~Q(status__name="Draft") | Q(author=user))


# Create your views here.
class PostListView(ListView):
    template_name = "postsTemplates/list.html"
    model = Post
    context_object_name = "posts"

    def get_queryset(self):
        return Post.objects.filter(
            status__name="Published"
        ).order_by("created_on")


class PostDraftListView(LoginRequiredMixin, ListView):
    template_name = "postsTemplates/list.html"
    model = Post
    context_object_name = "posts"

    def get_queryset(self):
        return Post.objects.filter(
            status__name="Draft",
            author=self.request.user
        ).order_by("created_on")


class PostArchivedListView(LoginRequiredMixin, ListView):
    template_name = "postsTemplates/list.html"
    model = Post
    context_object_name = "posts"

    def get_queryset(self):
        return Post.objects.filter(
            status__name="Archived",
            author=self.request.user
        ).order_by("created_on")


# ---------- Comment Section ----------
class PostView(View):
    def get(self, request, *args, **kwargs):
        view = PostDetailView.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = PostCommentFormView.as_view()
        return view(request, *args, **kwargs)


class PostDetailView(LoginRequiredMixin, DetailView):  # GET Request -> Single Object
    template_name = "postsTemplates/detail.html"
    model = Post
    context_object_name = "single_post"

    def get_queryset(self):
        return visible_posts(self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentForm()
        context["comments"] = self.object.comments.all()
        return context


class PostCommentFormView(LoginRequiredMixin, SingleObjectMixin, FormView):
    template_name = "postsTemplates/detail.html"
    form_class = CommentForm
    model = Post
    context_object_name = "single_post"

    def get_queryset(self):
        return visible_posts(self.request.user)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comments"] = self.object.comments.all()
        return context

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.author = self.request.user
        comment.save()  # needs a PK before the many-to-many .add() below works
        comment.posts.add(self.object)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("post_detail", kwargs={"pk": self.object.pk})


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
        # Not the author -> 403 Access Denied (a missing post is still a 404)
        return self.get_object().author == self.request.user

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    template_name = "postsTemplates/delete.html"
    model = Post
    success_url = reverse_lazy("post_list")

    def test_func(self):
        # Not the author -> 403 Access Denied (a missing post is still a 404)
        return self.get_object().author == self.request.user
