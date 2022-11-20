from django.urls import path
from django.conf.urls import url
from . import views


urlpatterns = [
    path('', views.index),
    path('', views.add_member, name="add-member"),
    path('', views.delete_member, name="delete-member"),
    
]
