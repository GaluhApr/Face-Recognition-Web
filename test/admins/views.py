from django.shortcuts import render,redirect
from .models import Member, Post

# Create your views here.


def index(request):
    return render(request, 'dashboard.html')


def attendance(request):
    return render(request, 'attendance.html')


def user(request):
    members = Member.objects.all()
    context = {
        'Members' : members,
    }
    return render(request, 'user.html',context)

def insert(request):
    member = Member(Nim=request.POST['firstname'], lastname=request.POST['lastname'], address=request.POST['address'])
    member.save()
    return redirect('/')

def sudahabsen(request):
    return render(request, 'sudahabsen.html')

def tidakabsen(request):
    return render(request, 'tidakabsen.html')

def screen(request):
    return render(request, 'attendancescreen.html')