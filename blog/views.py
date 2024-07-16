from django.shortcuts import render
from .models import Post
from django.views.generic import ListView
from django.views import View
from .forms import CommentForm
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def home_page(request):
    latest_posts = Post.objects.all().order_by("date")[:3]
    return render(request,"blog/index.html", {
        "posts":latest_posts
    })

class AllPostView(ListView):
    template_name = "blog/all-posts.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "all_posts"


# def posts(request):
#     return render(request,"blog/all-posts.html", {
#         "all_posts" : Post.objects.all()
#     })

# def post_detail(request,slug):
#     if request == "POST":
#         commentform = CommentForm(request.POST)
#         post = Post.objects.get(slug=slug)
#         if commentform.is_valid():
#             comment = commentform.save(commit=False)
#             comment.post = post
#             commentform.save()
#             return HttpResponseRedirect(reverse("post-detail-page", args=[slug]))


#     else:
#         identified_post = Post.objects.get(slug=slug) #left slug is model data , right slug is argument
#         return render(request,"blog/post-detail.html", {
#             "post": identified_post,
#             "post_tags": identified_post.tags.all(),
#             "commentform" : CommentForm()
#         })
    
class SinglePostView(View):
    def get(self,request,slug):
        post = Post.objects.get(slug=slug)
        context = {
            "post" : post,
            "post_tags" : post.tags.all(),
            "commentform" : CommentForm(),
            "comment": post.comments.all()
        }
        return render(request, "blog/post-detail.html", context)

    def post(self,request,slug):
        commentform = CommentForm(request.POST)
        post = Post.objects.get(slug=slug)
        if commentform.is_valid():
            comment = commentform.save(commit=False)
            comment.post = post
            commentform.save()
            return HttpResponseRedirect(reverse("post-detail-page", args=[slug]))
        
        post = Post.objects.get(slug=slug)
        context = {
            "post" : post,
            "post_tags" : post.tags.all(),
            "commentform" : CommentForm(),
            "comment": post.comments.all()
        }
        return render(request, "blog/post-detail.html", context)