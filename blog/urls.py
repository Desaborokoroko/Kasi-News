from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = []
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

urlpatterns = [path("",views.home,name='home'),path('category/<slug:category_slug>/',views.category_posts,name='category_posts'),
            path('post/<int:post_id>/',views.post_detail,name='post_detail'),]