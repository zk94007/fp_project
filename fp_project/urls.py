"""fp_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, include
from fp_project.views import register

urlpatterns = [
    # Django urls
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),

    # Registration url
    path('register/', register, name = 'register'),

    # App specific urls
    path('', include('dashboard.urls')),

    # Notice board urls
    path('post/', include('post.urls')),

    # Game urls
    path('game/', include('game.urls')),

    # Content Learning Tool urls
    path('tool/', include('tool.urls')),

    # User Manual urls
    path('manual/', include('manual.urls')),
]
