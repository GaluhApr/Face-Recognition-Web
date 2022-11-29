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
            'nim': 'Nim',
            'foto': 'Foto',
            'nama': 'Nama',
            'golongan': 'Golongan',
            'semester': 'Semester',
            'telepon': 'Telepon',
            'alamat': 'Alamat',
            'jenisKelamin': 'Jenis Kelamin',
        }

        widgets = {
            'nim': forms.TextInput(attrs={'class': 'form-control'}),
            'foto': forms.FileInput(attrs={'class': 'form-control'}),
            'nama': forms.TextInput(attrs={'class': 'form-control'}),
            'golongan': forms.Select(attrs={'class': 'form-control'}),
            'semester': forms.Select(choices=smt, attrs={'class': 'form-control'}),
            'telepon': forms.TextInput(attrs={'class': 'form-control'}),
            'alamat': forms.TextInput(attrs={'class': 'form-control'}),
            'jenisKelamin': forms.Select(choices=gender, attrs={'class': 'form-control'}),
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
        
class jadwalform(forms.ModelForm):
    class Meta:
        model = Jadwal
        fields = "__all__"

        labels = {
            'namaDosen': 'Nama Dosen',
            'golongan': 'Golongan',
            'matkul': 'Mata Kuliah',
            'ruangan': 'Ruangan',
            'hari': 'Hari',
            'jamMulai': 'Jam Mulai',
            'jamSelesai': 'Jam Selesai',
        }

        widgets = {
            'namaDosen': forms.Select(attrs={'class': 'form-control' }),
            'golongan': forms.Select(attrs={'class': 'form-control'}),
            'matkul': forms.Select(attrs={'class': 'form-control'}),
            'ruangan': forms.TextInput(attrs={'class': 'form-control'}),
            'hari': forms.TextInput(attrs={'class': 'form-control'}),
            'jamMulai': forms.TimeInput(attrs={'type': 'time' }),
            'jamSelesai': forms.TimeInput(attrs={'type': 'time' }),
        }
        