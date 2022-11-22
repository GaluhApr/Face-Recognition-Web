from django import forms
from .models import Member
from .models import dosen
import os

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
gender = (
    ('Laki-laki', 'Laki-laki'),
    ('Perempuan', 'Perempuan')
)


class Memberform(forms.ModelForm):
    class Meta:
        model = Member
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
            'Kelas': forms.Select(choices=golongan, attrs={'class': 'form-control'}),
            'Semester': forms.Select(choices=smt, attrs={'class': 'form-control'}),
            'Telepon': forms.TextInput(attrs={'class': 'form-control'}),
            'Alamat': forms.TextInput(attrs={'class': 'form-control'}),
            'Jenis_Kelamin': forms.Select(choices=gender, attrs={'class': 'form-control'}),
        }
        
class dosenform(forms.ModelForm):
    class Meta:
        model = dosen
        fields = "__all__"

        labels = {
            'nip': 'Nip',
            'namaDosen': 'Nama',
        }

        widgets = {
            'nip': forms.TextInput(attrs={'class': 'form-control'}),
            'namaDosen': forms.TextInput(attrs={'class': 'form-control'}),
        }
