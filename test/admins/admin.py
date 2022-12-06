from django.contrib import admin

# Register your models here.

from .models import Post, Mahasiswa, Dosen, Golongan, Matkul, Jadwal, Absen, Users,Dataset
admin.site.register(Post)
admin.site.register(Mahasiswa)
admin.site.register(Dosen)
admin.site.register(Golongan)
admin.site.register(Jadwal)
admin.site.register(Matkul)
admin.site.register(Absen)
admin.site.register(Users)
admin.site.register(Dataset)