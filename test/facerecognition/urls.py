"""facerecognition URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from . import views
from admins import views as adminsview
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('coba/', views.coba),
    path('dashboard/', adminsview.index),
    path('attendance/', adminsview.attendance),
    path('user/', adminsview.user),
    path('dosen/', adminsview.dosen),
    path('sudahabsen/', adminsview.sudahabsen),
    path('tidakabsen/', adminsview.tidakabsen),
    path('screen/', adminsview.screen),
    path('jadwal/', adminsview.jadwal),
    path('createmember/', adminsview.createmember, name='createmember'),
    path('', adminsview.add_member, name='add_member'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

