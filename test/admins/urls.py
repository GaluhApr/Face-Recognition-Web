from django.urls import path, re_path as url

from . import views


urlpatterns = [
    path('deletedosen/<int:id>', views.delete_dosen, name='delete-dosen'),
    path('deletemember/<int:id>', views.delete_member, name="delete-member"),
    path('editdosen/<int:id>', views.edit_dosen, name='edit-dosen'),
    # path('editmember/<int:id>', views.edit_member, name="edit-member"),
    path('', views.index),
    path('dashboard/', views.index),
    path('attendance/', views.attendance),
    path('user/', views.user, name='listuser'),
    path('dosen/', views.dosenview ,name='listdosen'),
    path('sudahabsen/', views.sudahabsen),
    path('tidakabsen/', views.tidakabsen),
    path('screen/', views.screen),
    path('jadwal/', views.jadwal),
    path('createmember/', views.createmember, name='createmember'),
    path('createdosen/', views.createdosen, name='createdosen'),
    path('creatematakuliah/', views.creatematakuliah, name='creatematakuliah'),
    path('matkul/', views.matkul),
]
