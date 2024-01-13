"""fusion URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import (
    path, 
    include
)
from django.conf.urls.static import static
from django.conf import settings

from fusion.core.urls import router

urlpatterns = [
    # DJANGO ADMIN
    path('admin/', admin.site.urls),

    # DJANGO REST FRAMEWORK ADMIN
    path('auth/', include('rest_framework.urls')),

    # CORE URLS
    path('', include('fusion.core.urls')),

    # API (1) Generics
    path('api/v1/', include('fusion.core.urls')),

    # API (2) Viewsets
    path('api/v2/', include(router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
