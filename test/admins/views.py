from django.shortcuts import render, redirect
from .models import Member, dosen, matakuliah
from .forms import Memberform, matakuliahform
from .models import dosen  # type: ignore
from .forms import dosenform
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from PIL import Image

from keras.models import load_model
import numpy as np
from numpy import asarray
from numpy import expand_dims

import pickle
import cv2


# Create your views here.


def index(request):
    
    return render(request, 'dashboard.html')


def attendance(request):
    return render(request, 'attendance.html')

#user
def user(request):
    members = Member.objects.all()
    context = {
        'Members': members,
        'form': Memberform()
    }
    
    return render(request, 'user.html', context,)

def createmember(request):
    Nim = request.POST["Nim"]
    Foto = request.POST["Foto"]
    Nama = request.POST["Nama"]
    Kelas = request.POST["Kelas"]
    Semester = request.POST["Semester"]
    Telepon = request.POST["Telepon"]
    Alamat = request.POST["Alamat"]
    Jenis_Kelamin = request.POST["Jenis_Kelamin"]

    admins_member = Member(Nim=Nim, Foto=Foto, Nama=Nama, Kelas=Kelas, Semester=Semester,
                        Telepon=Telepon, Alamat=Alamat, Jenis_Kelamin=Jenis_Kelamin)
    admins_member.save()
    return redirect('listuser')

def delete_member(request, id):
    delmember = Member.objects.get(id=id)
    delmember.delete()
    members = Member.objects.all()
    return redirect('listuser')

def edit_member(request,id):
    member_edit = Member.objects.get(id=id)
    
    data = {
        'Nim': member_edit.Nim,
        'Foto': member_edit.Foto,
        'Nama': member_edit.Nama,
        'Kelas': member_edit.Kelas,
        'Semester': member_edit.Semester,
        'Telepon': member_edit.Telepon,
        'Alamat': member_edit.Alamat,
        'Jenis_Kelamin': member_edit.Jenis_Kelamin,
    }
    
    admins_member = Memberform(request.POST or None, initial=data , instance=member_edit)
    
    if request.method == 'POST':
        if admins_member.is_valid():
            admins_member.save()
            return redirect('listuser')
    
    context = {
        'Member': member_edit,
        'admins_member': admins_member,
    }
    return render(request, 'editmember.html', context)



def createdosen(request):
    nip = request.POST["nip"]
    namaDosen = request.POST["namaDosen"]

    admins_dosen = dosen(nip=nip, namaDosen=namaDosen)
    admins_dosen.save()
    return redirect( 'listdosen')

def delete_dosen(request, id):
    deldosen = dosen.objects.get(id=id)
    deldosen.delete()
    Dosen = dosen.objects.all()
    return redirect ('listdosen')

def edit_dosen(request,id):
    dosen_edit = dosen.objects.get(id=id)
    
    data = {
        'nip': dosen_edit.nip,
        'namaDosen': dosen_edit.namaDosen,
    }
    
    admins_dosen = dosenform(request.POST or None, initial=data , instance=dosen_edit)
    
    if request.method == 'POST':
        if admins_dosen.is_valid():
            admins_dosen.save()
            return redirect('listdosen')
    
    context = {
        'dosen': dosen_edit,
        'admins_dosen': admins_dosen,
    }
    return render(request, 'editdosen.html', context)

def dosenview(request):
    dosens = dosen.objects.all()
    context = {
        'Dosens': dosens,
        'form': dosenform()
    }
    return render(request, 'dosen.html', context,)

#matakuliah
def creatematkul(request):
    kodeMK = request.POST["kodeMK"]
    mataKuliah = request.POST["mataKuliah"]
    sks = request.POST["sks"]
    
    admins_matakuliah = matakuliah(kodeMK=kodeMK, mataKuliah=mataKuliah, sks=sks)
    admins_matakuliah.save()
    return redirect('listmatkul')

def edit_matkul(request,id):
    matkul_edit = matakuliah.objects.get(id=id)
    
    data = {
        'kodeMK': matkul_edit.kodeMK,
        'mataKuliah': matkul_edit.mataKuliah,
        'sks': matkul_edit.sks,
    }
    
    admins_matakuliah = matakuliahform(request.POST or None, initial=data , instance=matkul_edit)
    
    if request.method == 'POST':
        if admins_matakuliah.is_valid():
            admins_matakuliah.save()
            return redirect('listmatkul')
    
    context = {
        'matakuliah': matkul_edit,
        'admins_matakuliah': admins_matakuliah,
    }
    return render(request, 'editmatkul.html', context)

def delete_matakuliah(request, id):
    deletematakuliah = matakuliah.objects.get(id=id)
    deletematakuliah.delete()
    return redirect('listmatkul')

def matkulview(request):
    matkuls = matakuliah.objects.all()
    context = {
        'Matkuls': matkuls,
        'form': matakuliahform()
    }
    return render(request, 'matakuliah.html', context,)

#sudah absen
def sudahabsen(request):
    return render(request, 'sudahabsen.html')

#belum absen
def tidakabsen(request):
    return render(request, 'tidakabsen.html')

#absen
def screen(request):
    return render(request, 'attendancescreen.html')


#jadwal
def jadwal(request):
    return render(request, 'jadwal.html')
