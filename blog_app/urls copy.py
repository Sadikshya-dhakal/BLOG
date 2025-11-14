from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('detail/<int:pk>/', views.post_detail, name='post_detail'),
    path("create/", views.post_create, name="post_create"),
    path("draft-list/", views.draft_list, name="draft_list"),
    path("drafft-detail/<int:pk>/", views.draft_detail, name="draft_detail"),
    path("update/<int:pk>/", views.post_update, name="post_update"),
    path("delete/<int:pk>/", views.post_delete, name="post_delete"),
    path("publish/<int:pk>/", views.draft_publish, name="draft_publish"),

]