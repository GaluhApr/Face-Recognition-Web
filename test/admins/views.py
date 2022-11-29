from django.shortcuts import render, redirect, HttpResponse
from .models import Mahasiswa, Matkul, Dosen, Jadwal
from .forms import Memberform, matakuliahform, dosenform, jadwalform
from django.core.files.storage import FileSystemStorage
from PIL import Image
from keras.models import load_model
import numpy as np
from numpy import asarray
from numpy import expand_dims
from .resource import jadwaltable, mahasiswatable, dosentable, matkultable
import pickle
import cv2


# Create your views here.


def index(request):

    return render(request, 'dashboard.html')


def attendance(request):
    return render(request, 'attendance.html')

# user


def user(request):
    members = Mahasiswa.objects.all()
    context = {
        'Members': members,
        'form': Memberform()
    }

    return render(request, 'user.html', context,)


def createmember(request):
    nim = request.POST["nim"]
    foto = request.POST["foto"]
    nama = request.POST["nama"]
    golongan = request.POST["golongan"]
    semester = request.POST["semester"]
    telepon = request.POST["telepon"]
    alamat = request.POST["alamat"]
    jenisKelamin = request.POST["jenisKelamin"]

    admins_member = Mahasiswa(nim=nim, foto=foto, nama=nama, golongan_id=golongan, semester=semester,
                              telepon=telepon, alamat=alamat, jenisKelamin=jenisKelamin)
    admins_member.save()
    return redirect('listuser')


def delete_member(request, id):
    delmember = Mahasiswa.objects.get(id=id)
    delmember.delete()
    members = Mahasiswa.objects.all()
    return redirect('listuser')


def edit_member(request, id):
    member_edit = Mahasiswa.objects.get(id=id)

    data = {
        'nim': member_edit.nim,
        'foto': member_edit.foto,
        'nama': member_edit.nama,
        'golongan': member_edit.golongan,
        'semester': member_edit.semester,
        'telepon': member_edit.telepon,
        'alamat': member_edit.alamat,
        'jenisKelamin': member_edit.jenisKelamin,
    }

    admins_member = Memberform(
        request.POST or None, initial=data, instance=member_edit)

    if request.method == 'POST':
        if admins_member.is_valid():
            admins_member.save()
            return redirect('listuser')

    context = {
        'page_title': 'Mahasiswa',
        'Member': member_edit,
        'form': Memberform(initial=data, instance=member_edit)
    }
    return render(request, 'editdata.html', context)


def createdosen(request):
    nip = request.POST["nip"]
    namaDosen = request.POST["namaDosen"]

    admins_dosen = Dosen(nip=nip, namaDosen=namaDosen)
    admins_dosen.save()
    return redirect('listdosen')


def delete_dosen(request, id):
    deldosen = Dosen.objects.get(id=id)
    deldosen.delete()
    deldosen = Dosen.objects.all()
    return redirect('listdosen')


def edit_dosen(request, id):
    dosen_edit = Dosen.objects.get(id=id)

    data = {
        'nip': dosen_edit.nip,
        'namaDosen': dosen_edit.namaDosen,
    }

    admins_dosen = dosenform(request.POST or None,
                             initial=data, instance=dosen_edit)

    if request.method == 'POST':
        if admins_dosen.is_valid():
            admins_dosen.save()
            return redirect('listdosen')

    context = {
        'page_title': 'Dosen',
        'dosen': dosen_edit,
        'form': dosenform(initial=data, instance=dosen_edit)
    }
    return render(request, 'editdata.html', context)


def dosenview(request):
    dosens = Dosen.objects.all()
    context = {
        'Dosens': dosens,
        'form': dosenform()
    }
    return render(request, 'dosen.html', context,)

# matakuliah


def creatematkul(request):
    kodeMK = request.POST["kodeMK"]
    mataKuliah = request.POST["mataKuliah"]
    sks = request.POST["sks"]

    admins_matakuliah = Matkul(kodeMK=kodeMK, mataKuliah=mataKuliah, sks=sks)
    admins_matakuliah.save()
    return redirect('listmatkul')


def edit_matkul(request, id):
    matkul_edit = Matkul.objects.get(id=id)

    data = {
        'kodeMK': matkul_edit.kodeMK,
        'mataKuliah': matkul_edit.mataKuliah,
        'sks': matkul_edit.sks,
    }

    admins_matakuliah = matakuliahform(
        request.POST or None, initial=data, instance=matkul_edit)

    if request.method == 'POST':
        if admins_matakuliah.is_valid():
            admins_matakuliah.save()
            return redirect('listmatkul')

    context = {
        'page_title': 'Matkul',
        'matakuliah': matkul_edit,
        'form': matakuliahform(initial=data, instance=matkul_edit)
    }
    return render(request, 'editdata.html', context)


def delete_matakuliah(request, id):
    deletematakuliah = Matkul.objects.get(id=id)
    deletematakuliah.delete()
    return redirect('listmatkul')


def matkulview(request):
    matkuls = Matkul.objects.all()
    context = {
        'Matkuls': matkuls,
        'form': matakuliahform()
    }
    return render(request, 'matakuliah.html', context,)

# sudah absen


def sudahabsen(request):
    return render(request, 'sudahabsen.html')

# belum absen


def tidakabsen(request):
    return render(request, 'tidakabsen.html')

# absen


def screen(request):
    return render(request, 'attendancescreen.html')


# jadwal
def jadwal(request):
    jadwals = Jadwal.objects.all()
    context = {
        'Jadwals': jadwals,
        'form': jadwalform()
    }
    return render(request, 'jadwal.html', context)


def delete_jadwal(request, id):
    deletejadwal = Jadwal.objects.get(id=id)
    deletejadwal.delete()
    return redirect('listjadwal')


def createjadwal(request):
    namaDosen = request.POST["namaDosen"]
    golongan = request.POST["golongan"]
    matkul = request.POST["matkul"]
    ruangan = request.POST["ruangan"]
    hari = request.POST["hari"]
    jamMulai = request.POST["jamMulai"]
    jamSelesai = request.POST["jamSelesai"]

    admins_jadwal = Jadwal(namaDosen_id=namaDosen, golongan_id=golongan, matkul_id=matkul,
                           ruangan=ruangan, hari=hari, jamMulai=jamMulai, jamSelesai=jamSelesai)
    admins_jadwal.save()
    return redirect('listjadwal')


def edit_jadwal(request, id):
    jadwal_edit = Jadwal.objects.get(id=id)

    data = {
        'namaDosen': jadwal_edit.namaDosen,
        'golongan': jadwal_edit.golongan,
        'matkul': jadwal_edit.matkul,
        'ruangan': jadwal_edit.ruangan,
        'hari': jadwal_edit.hari,
        'jamMulai': jadwal_edit.jamMulai,
        'jamSelesai': jadwal_edit.jamSelesai,

    }

    admins_jadwal = jadwalform(
        request.POST or None, initial=data, instance=jadwal_edit)

    if request.method == 'POST':
        if admins_jadwal.is_valid():
            admins_jadwal.save()
            return redirect('listjadwal')

    context = {
        'page_title': 'Jadwal',
        'jadwal': jadwal_edit,
        'form': jadwalform(initial=data, instance=jadwal_edit)
    }
    return render(request, 'editdata.html', context)


def exportjadwal(request):
    jadwal = jadwaltable()
    dataset = jadwal.export()
    response = HttpResponse(
        dataset.xls, content_type='application/vnd.ms-excel')  # type: ignore
    response['Content-Disposition'] = 'attachment; filename="jadwal.xls"'
    return response


def exportmahasiswa(request):
    mahasiswa = mahasiswatable()
    dataset = mahasiswa.export()
    response = HttpResponse(
        dataset.xls, content_type='application/vnd.ms-excel')  # type: ignore
    response['Content-Disposition'] = 'attachment; filename="mahasiswa.xls"'
    return response


def exportdosen(request):
    dosen = dosentable()
    dataset = dosen.export()
    response = HttpResponse(
        dataset.xls, content_type='application/vnd.ms-excel')  # type: ignore
    response['Content-Disposition'] = 'attachment; filename="dosen.xls"'
    return response


def exportmatkul(request):
    matkul = matkultable()
    dataset = matkul.export()
    response = HttpResponse(
        dataset.xls, content_type='application/vnd.ms-excel')  # type: ignore
    response['Content-Disposition'] = 'attachment; filename="matakuliah.xls"'
    return response
