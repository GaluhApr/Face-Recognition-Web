from django.db import models
import datetime
import os

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    
    def __str__(self):
        return "{}".format(self.title)

def filepath(request, filename):
    old_filename = filename
    filename = (old_filename)
    return os.path.join('upload/', filename)

class Dosen(models.Model):
    nip = models.CharField(max_length=20)
    namaDosen = models.CharField(max_length=100)
    
    class Meta :
        db_table = "tb_dosen"
        
    def __str__(self):
        return "{}".format(self.namaDosen)

class Golongan(models.Model):
    golongan = models.CharField(max_length=50)
    
    class Meta :
        db_table = "tb_golongan"
    
    def __str__(self):
        return "{}".format(self.golongan)
    
class Matkul(models.Model):
    kodeMK = models.CharField(max_length=20)
    mataKuliah = models.CharField(max_length=50)
    sks = models.IntegerField()
    
    class Meta :
        db_table = "tb_matkul"
        
    def __str__(self):
        return "{}".format(self.mataKuliah)

class Mahasiswa(models.Model):
    gender = (
        ('Laki-laki', 'Laki-laki'),
        ('Perempuan', 'Perempuan')
    )
    smt = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
    )
    
    nim = models.CharField(max_length=10)
    nama = models.CharField(max_length=20)
    golongan = models.ForeignKey(Golongan, null=True, on_delete=models.SET_NULL)
    semester = models.TextField(choices=smt)
    telepon = models.CharField(max_length=14)
    alamat = models.TextField(max_length=20)
    jenisKelamin = models.TextField(choices=gender)
    
    class Meta :
        db_table = "tb_mahasiswa"
    
    def __str__(self):
        return "{}".format(self.nama)
    
class Dataset(models.Model):
    nama = models.ForeignKey(Mahasiswa, null=True, on_delete=models.SET_NULL)
    foto1 = models.FileField(upload_to='dataset/', null=True, blank=True)
    foto2 = models.FileField(upload_to='dataset/', null=True, blank=True)
    foto3 = models.FileField(upload_to='dataset/', null=True, blank=True)
    foto4 = models.FileField(upload_to='dataset/', null=True, blank=True)
    foto5 = models.FileField(upload_to='dataset/', null=True, blank=True)
    foto6 = models.FileField(upload_to='dataset/', null=True, blank=True)
    foto7 = models.FileField(upload_to='dataset/', null=True, blank=True)
    foto8 = models.FileField(upload_to='dataset/', null=True, blank=True)
    foto9 = models.FileField(upload_to='dataset/', null=True, blank=True)
    foto10 = models.FileField(upload_to='dataset/', null=True, blank=True)
    class Meta :
        db_table = "tb_dataset"
        
    def __str__(self):
        return "{}".format(self.foto1)    
    
class Jadwal(models.Model):
    namaDosen = models.ForeignKey(Dosen, null=True, on_delete=models.SET_NULL)
    golongan = models.ForeignKey(Golongan, null=True, on_delete=models.SET_NULL)
    matkul = models.ForeignKey(Matkul, null=True, on_delete=models.SET_NULL)
    ruangan = models.CharField(max_length=5)
    hari = models.CharField(max_length=30)
    jamMulai = models.TimeField(auto_now=False, auto_now_add=False)
    jamSelesai = models.TimeField(auto_now=False, auto_now_add=False)
    
    class Meta :
        db_table = "tb_jadwal"
    
    def __str__(self):
        return "{}".format(self.ruangan)
    
class Absen(models.Model):
    sts = (
        ('Masuk', 'Masuk'),
        ('Ijin', 'Ijin'),
        ('Sakit', 'Sakit'),
        ('Alpha', 'Alpha')
    )
    
    mahasiswa = models.ForeignKey(Mahasiswa, null=True, on_delete=models.SET_NULL)
    jadwal = models.ForeignKey(Jadwal, null=True, on_delete=models.SET_NULL)
    tanggal = models.DateField(auto_now=False, auto_now_add=False)
    status = models.TextField(choices=sts)
    
    class Meta :
        db_table = "tb_absen"
        
    def __str__(self):
        return "{}".format(self.mahasiswa, self.status)
    
class Users(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=40)
    
    class Meta :
        db_table = "tb_users"
        
    def __str__(self):
        return "{}".format(self.username)
    

    
    
