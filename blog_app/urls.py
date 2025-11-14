from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),
    path('detail/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path("create/", views.PostCreateView.as_view(), name="post_create"),
    path("draft-list/", views.DraftListView.as_view(), name="draft_list"),
    path("drafft-detail/<int:pk>/", views.DraftDetailView.as_view(), name="draft_detail"),
    path("update/<int:pk>/", views.PostUpdateView.as_view(), name="post_update"),
    path("delete/<int:pk>/", views.PostDeleteView.as_view(), name="post_delete"),
    path("publish/<int:pk>/", views.DraftPublishView.as_view(), name="draft_publish"),

]