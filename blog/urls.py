from django.urls import path
from . import views


urlpatterns = [
    path("", views.home_page , name="home-page"),
    path("posts", views.AllPostView.as_view(), name="posts-page"),
    path("posts/<slug:slug>", views.SinglePostView.as_view(), name="post-detail-page")
]