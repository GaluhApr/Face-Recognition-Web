from django.urls import path, re_path

from . import views


urlpatterns = [
    path('', views.index),
    path('addmember', views.add_member, name="add-member"),
    path('adddosen', views.add_dosen, name="add-dosen"),
]
