
from django.shortcuts import render,get_object_or_404
from .models import Post, Category

# Create your views here.
def home(request):
    categories = Category.objects.all()
    latest_post = Post.objects.order_by("-created_at").first()
    other_posts = Post.objects.order_by("-created_at")[1:]
    
    return render(request, 'blog/home.html',{"categories":categories,"latest_post":latest_post,"other_posts":other_posts})


def category_posts(request,category_id):
    categories = Category.objects.all()
    category = get_object_or_404(Category,id=category_id)
    posts = Post.objects.filter(category=category).order_by('-created_at')
    
    return render(request,'blog/category.html',{'categories':categories,'category':category,'posts':posts})


def post_detail(request,post_id):
    categories = Category.objects.all()
    post = get_object_or_404(Post,id=post_id)
    
    return render(request,'blog/post_detail.html',{'categories':categories,'post':post})
