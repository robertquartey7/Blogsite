
from django.contrib import admin
from django.contrib.auth import views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('', include('users.urls')),
    path('login/', views.LoginView.as_view(template_name ='users/login.html'), name='login'),
    path('logout/', views.LogoutView.as_view(template_name ='users/logout.html'), name='logout' )

] 


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
    
    
    
