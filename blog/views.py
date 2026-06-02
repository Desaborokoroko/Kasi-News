
from django.shortcuts import render,get_object_or_404
from .models import Post, Category

# Create your views here.
def home(request):
    categories = Category.objects.all()
    top_story = Post.objects.order_by('-created_at').first()
    
    
    if top_story:
        latest_news = Post.objects.exclude(id=top_story.id).order_by('-created_at')[:10]
    else:
        latest_news = Post.objects.order_by('-created_at')[:10]
        
    context = {"categories":categories,"top_story":top_story,"latest_news":latest_news,}
    
    return render(request, 'blog/home.html',context)


def category_posts(request,category_slug):
    categories = Category.objects.all()
    category = get_object_or_404(Category,slug=category_slug)
    posts = Post.objects.filter(category=category).order_by('-created_at')
    
    return render(request,'blog/category.html',{'categories':categories,'category':category,'posts':posts})


def post_detail(request,post_id):
    categories = Category.objects.all()
    post = get_object_or_404(Post,id=post_id)
    
    return render(request,'blog/post_detail.html',{'categories':categories,'post':post})
