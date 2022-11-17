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

class Member(models.Model):
    gender = (
        ('Laki-laki', 'Laki-laki'),
        ('Perempuan', 'Perempuan')
    )
    golongan = (
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
        ('E', 'E'),
        ('Internasional', 'Internasional')
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
    
    Nim = models.CharField(max_length=9)
    Foto = models.ImageField(upload_to='upload/', blank=True, null=True)
    Nama = models.CharField(max_length=20)
    Kelas = models.TextField(choices=golongan)
    Semester = models.TextField(choices=smt)
    Telepon = models.CharField(max_length=14)
    Alamat = models.TextField(max_length=20)
    Jenis_Kelamin = models.TextField(choices=gender)
    
    class Meta :
        db_table = "admins_member"
    
    def __str__(self):
        return "{}".format(self.Nama)
    
class foto(models.Model):
    idFoto = models.IntegerField()
    namaFoto = models.TextField(max_length=50)
    
    def __str__(self):
        return "{}".format(self.namaFoto)
    
class absensi(models.Model):
    idAbsen = models.TextField(max_length=50)
    keterangan = models.TextField(max_length=50)
    
    def __str__(self):
        return "{}".format(self.keterangan)
    
class beritaAcara(models.Model):
    idAcara = models.TextField(max_length=50)
    pertemuan = models.TextField(max_length=5)
    tanggal = models.DateTimeField()
    
    def __str__(self):
        return "{}".format(self.pertemuan)
    
class jadwal(models.Model):
    idJadwal = models.TextField(max_length=50)
    ruangan = models.TextField(max_length=5)
    hari = models.TextField(max_length=30)
    jamMulai = models.IntegerField()
    jamSelesai = models.IntegerField()
    
    def __str__(self):
        return "{}".format(self.ruangan)
    
class golongan(models.Model):
    idGol = models.TextField(max_length=2)
    namaGol = models.TextField(max_length=50)
    
    def __str__(self):
        return "{}".format(self.namaGol)
    
class mataKuliah(models.Model):
    kodeMK = models.TextField(max_length=10)
    mataKuliah = models.TextField(max_length=50)
    sks = models.IntegerField()
    
    def __str__(self):
        return "{}".format(self.mataKuliah)
    
class dosen(models.Model):
    nip = models.TextField(max_length=15)
    namaDosen = models.TextField(max_length=50)
    
    def __str__(self):
        return "{}".format(self.namaDosen)