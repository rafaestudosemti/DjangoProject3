from django.urls import path

from . import views

#path takes the name after the domain, and the view which you would like to map

urlpatterns = [
    path("", views.starting_page, name="starting-page"),
    path("posts", views.posts, name="posts-page"),
    path("posts/<slug:slug>", views.post_detail, name="post_detail-page") #/posts/my-first-post
]
