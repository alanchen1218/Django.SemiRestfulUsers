from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import *
# Create your views here.


# the index function is called when root is visited
def index(request):
  context = {
    'users' : User.objects.all().values()
  }
  return render(request, 'first_app/index.html',context)
  # return redirect('/')

def new(request):
  return render(request, 'first_app/new.html') #render when you wanna display info

def create(request):
  if request.method =='POST':
    errors = User.objects.nameValidation(request.POST)
    if len(errors):
      for key, value in errors.items():
        messages.error(request, value)
        request.session['fullname'] =request.POST['fullname']
        request.session['email'] =request.POST['email']
        return redirect('/first_app/new')
    else:
      User.objects.create(fullname = request.POST['fullname'], email=request.POST['email'])
      return redirect('/') #always redirect on process route

def edit(request,number):
  if request.method == 'POST':
    user = User.objects.get(id=number)
  context = {
    "user" : User.objects.get(id = number)
  }
  return render(request, 'first_app/edit.html', context)

def update(request):
  # if request.method == 'POST':
  updateuser = User.objects.get(id=request.POST["usersid"])
  updateuser.fullname = request.POST['name']
  updateuser.email = request.POST['email']
  updateuser.save()
  return redirect('/') #always redirect on process route

def show(request, number):
  # if request.method == 'POST':
  #   user = User.objects.get(id=number)
  #   # user.fullname = request.POST['fullname']
  #   # user.email = request.POST['email']
  #   # user.save()
  context = {
    'user' : User.objects.get(id=number)
  }
  return render(request, 'first_app/show.html',context)

def destroy(request, number):
  User.objects.get(id=number).delete()
  return redirect('/') #always redirect on process route

