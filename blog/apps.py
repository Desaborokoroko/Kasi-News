from django.apps import AppConfig
import os

class BlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog' #matches your folder name
    
    def ready(self):
        if os.getenv('CREATE_SUPERUSER') == 'True':
            from django.contrib.auth import get_user_model
            from django.db.utils import OperationalError, ProgrammingError
            try:
                User = get_user_model()
                username = os.getenv('DJANGO_SUPERUSER_USERNAME','admin')
                email = os.getenv('DJANGO_SUPERUSER_EMAIL','kasinews@gmail.com')
                password = os.getenv('DJANGO_SUPERUSER_PASSWORD')
    
                if password:
                    user, created = User.objects.get_or_create(username=username, 
                    defaults={'email':email,'is_staff':True,
                            'is_superuser':True})
                    user.set_password(password)
                    user.save()
                    print("superuser password updated")
            except(OperationalError,ProgrammingError):
                pass
            
