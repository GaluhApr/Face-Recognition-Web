from django.shortcuts import render, redirect
from .models import Member
from .forms import Memberform
from .models import dosen  # type: ignore
from .forms import dosenform
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponseRedirect


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

#dosen
def dosenview(request):
    Dosen = dosen.objects.all()
    context = {
        'dosen': Dosen,
        'form': dosenform()
    }
    return render(request, 'dosen.html', context,)

def createdosen(request):
    nip = request.POST["nip"]
    namaDosen = request.POST["namaDosen"]

    admins_dosen = dosen(nip=nip, namaDosen=namaDosen)
    admins_dosen.save()
    return render(request, 'successdosen.html')

def add_dosen(request):
	submitted = False
	if request.method == "POST":
		form = dosenform(request.POST, request.FILES)
		if form.is_valid():
			dosen = form.save(commit=False)
			# logged in user
			dosen.save()
			#form.save()
			return 	HttpResponseRedirect('/add_dosen?submitted=True')	
	else:
		form = dosenform
		if 'submitted' in request.GET:
			submitted = True

	return render(request, 'dosen.html', {'form':form, 'submitted':submitted})

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
