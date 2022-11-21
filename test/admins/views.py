from django.shortcuts import render, redirect
from .models import Member
from .forms import Memberform
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponseRedirect


# Create your views here.


def index(request):
    return render(request, 'dashboard.html')


def attendance(request):
    return render(request, 'attendance.html')


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
    return render(request, 'success.html')


def add_dosen(request):
	submitted = False
	if request.method == "POST":
		form = Memberform(request.POST, request.FILES)
		if form.is_valid():
			Member = form.save(commit=False)
			# logged in user
			Member.save()
			#form.save()
			return 	HttpResponseRedirect('/add_member?submitted=True')	
	else:
		form = Memberform
		if 'submitted' in request.GET:
			submitted = True

	return render(request, 'user.html', {'form':form, 'submitted':submitted})

def dosen(request):
    members = Member.objects.all()
    context = {
        'Members': members,
        'form': Memberform()
    }
    return render(request, 'dosen.html', context,)


def createdosen(request):
    No = request.POST["No"]
    Nip = request.POST["Nip"]
    Nama = request.POST["Nama"]

    admins_member = Member(No=No, Nip=Nip, Nama=Nama)
    admins_member.save()
    return render(request, 'success.html')


def add_member(request):
	submitted = False
	if request.method == "POST":
		form = Memberform(request.POST, request.FILES)
		if form.is_valid():
			Member = form.save(commit=False)
			# logged in user
			Member.save()
			#form.save()
			return 	HttpResponseRedirect('/add_member?submitted=True')	
	else:
		form = Memberform
		if 'submitted' in request.GET:
			submitted = True

	return render(request, 'dosen.html', {'form':form, 'submitted':submitted})

# # dosen
# def createmember(request):
#     Nim = request.POST["Nim"]
#     Foto = request.POST["Foto"]
#     Nama = request.POST["Nama"]
#     Kelas = request.POST["Kelas"]
#     Semester = request.POST["Semester"]
#     Telepon = request.POST["Telepon"]
#     Alamat = request.POST["Alamat"]
#     Jenis_Kelamin = request.POST["Jenis_Kelamin"]

#     admins_member = Member(Nim=Nim, Foto=Foto, Nama=Nama, Kelas=Kelas, Semester=Semester,
#                         Telepon=Telepon, Alamat=Alamat, Jenis_Kelamin=Jenis_Kelamin)
#     admins_member.save()
#     return render(request, 'success.html')

def sudahabsen(request):
    return render(request, 'sudahabsen.html')

def tidakabsen(request):
    return render(request, 'tidakabsen.html')

def screen(request):
    return render(request, 'attendancescreen.html')

def jadwal(request):
    return render(request, 'jadwal.html')
