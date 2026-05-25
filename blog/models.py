from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    
    def __str__(self):
        return self.name
    
class Post(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to="post_images/",blank=True,null=True)
    video = models.FileField(upload_to="post_videos/",blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.title



