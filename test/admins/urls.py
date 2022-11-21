from django.urls import path, re_path

from . import views


urlpatterns = [
    path('', views.index),
    path('deletemember/(?P<delete_id>[0-9]+)', views.delete_member, name='delete-member'),
    
    
]
