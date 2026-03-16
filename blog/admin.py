from django.contrib import admin
from .models import Category,Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title','category','created_at')
    fields = ('title','content','category','image','video')
    

# Register your models here.
admin.site.register(Category)
admin.site.register(Post,PostAdmin)
