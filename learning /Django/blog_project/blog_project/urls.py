from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    # Admin URL
    path('admin/', admin.site.urls),

    # Blog app URLs
    path('', include('blog.urls')),

    # Authentication URLs (Django's built-in auth views)
    path('accounts/', include('django.contrib.auth.urls')),

    # JWT Authentication URLs
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
