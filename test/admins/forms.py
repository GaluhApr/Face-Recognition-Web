from django import forms
from .models import Mahasiswa, Dosen, Matkul, Jadwal, Golongan, Absen, Users
import os


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
gender = (
    ('Laki-laki', 'Laki-laki'),
    ('Perempuan', 'Perempuan')
)


class Memberform(forms.ModelForm):
    class Meta:
        model = Mahasiswa
        fields = "__all__"

        labels = {
            'Nim': 'Nim',
            'Foto': 'Foto',
            'Nama': 'Nama',
            'Kelas': 'Kelas',
            'Semester': 'Semester',
            'Telepon': 'Telepon',
            'Alamat': 'Alamat',
            'Jenis_Kelamin': 'Jenis_Kelamin',
        }

        widgets = {
            'Nim': forms.TextInput(attrs={'class': 'form-control'}),
            'Foto': forms.FileInput(attrs={'class': 'form-control'}),
            'Nama': forms.TextInput(attrs={'class': 'form-control'}),
            'Golongan': forms.Select(attrs={'class': 'form-control'}),
            'Semester': forms.Select(choices=smt, attrs={'class': 'form-control'}),
            'Telepon': forms.TextInput(attrs={'class': 'form-control'}),
            'Alamat': forms.TextInput(attrs={'class': 'form-control'}),
            'Jenis_Kelamin': forms.Select(choices=gender, attrs={'class': 'form-control'}),
        }
        
class dosenform(forms.ModelForm):
    class Meta:
        model = Dosen
        fields = "__all__"

        labels = {
            'nip': 'Nip',
            'namaDosen': 'Nama',
        }

        widgets = {
            'nip': forms.TextInput(attrs={'class': 'form-control'}),
            'namaDosen': forms.TextInput(attrs={'class': 'form-control'}),
        }

class matakuliahform(forms.ModelForm):
    class Meta:
        model = Matkul
        fields = "__all__"

        labels = {
            'kodeMK': 'KodeMK',
            'mataKuliah': 'Matakuliah',
            'sks': 'SKS',
        }

        widgets = {
            'kodeMK': forms.TextInput(attrs={'class': 'form-control'}),
            'mataKuliah': forms.TextInput(attrs={'class': 'form-control'}),
            'sks': forms.TextInput(attrs={'class': 'form-control'}),
        }