from django.urls import path
from . import views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create_blog, name='create_blog'),
    path('register/', views.register, name='register'),
     path('api/blogs/', views.get_blogs, name='get_blogs'),
    path('api/blogs/create/', views.create_blog, name='create_blog'),
    path('register/', views.UserRegistrationView.as_view(), name='register'),
]

