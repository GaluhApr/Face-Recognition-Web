from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    
    def __str__(self):
        return "{}".format(self.title)


class Member(models.Model):
    Nim = models.CharField(max_length=9)
    Foto = models.ImageField()
    Nama = models.TextField(max_length=20)
    Kelas = models.TextField(max_length=10)
    Semester = models.TextField(max_length=10)
    Telepon = models.TextField(max_length=14)
    Alamat = models.TextField(max_length=20)
    Jenis_Kelamin = models.TextField(max_length=10)
    
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