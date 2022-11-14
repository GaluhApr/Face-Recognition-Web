from django.db import models

# Create your models here.


class Member(models.Model):
    Nim = models.CharField(max_length=50)
    Nama = models.CharField(max_length=50)
    Kelas = models.CharField(max_length=50)
    Semester = models.CharField(max_length=50)
    Telepon = models.CharField(max_length=50)
    Alamat = models.CharField(max_length=50)
    JenisKelamin = models.CharField(max_length=50)

    # def __str__(self):
    #     return self.firstname + " " + self.lastname
    #create model?
