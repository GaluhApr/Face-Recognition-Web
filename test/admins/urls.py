from django.urls import path, re_path as url

from . import views


urlpatterns = [
    path('deletedosen/<int:id>', views.delete_dosen, name='delete-dosen'),
    path('deletemember/<int:id>', views.delete_member, name="delete-member"),
    path('', views.index),
    path('addmember', views.add_member, name="add-member"),
    path('adddosen', views.add_dosen, name="add-dosen"),
    path('addmatakuliah', views.add_dosen, name="add-matakuliah"),
    path('dashboard/', views.index),
    path('attendance/', views.attendance),
    path('user/', views.user),
    path('dosen/', views.dosenview),
    path('sudahabsen/', views.sudahabsen),
    path('tidakabsen/', views.tidakabsen),
    path('screen/', views.screen),
    path('jadwal/', views.jadwal),
    path('createmember/', views.createmember, name='createmember'),
    path('createdosen/', views.createdosen, name='createdosen'),
    path('creatematakuliah/', views.creatematakuliah, name='creatematakuliah'),
    path('matkul/', views.matkul),
]
