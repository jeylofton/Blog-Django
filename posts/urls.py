from django.urls import path
from .views import (
    PostListView,
    PostDraftListView,
    PostArchivedListView,
    PostView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView
)

urlpatterns = [
    path("list/", PostListView.as_view(), name="post_list"),
    path("drafts/", PostDraftListView.as_view(), name="post_draft_list"),
    path("archived/", PostArchivedListView.as_view(), name="post_archived_list"),
    path('detail/<int:pk>/', PostView.as_view(), name="post_detail"),
    path("new/", PostCreateView.as_view(), name="post_new"),
    path("edit/<int:pk>/", PostUpdateView.as_view(), name="post_edit"),
    path("delete/<int:pk>/", PostDeleteView.as_view(), name="post_delete")
]


