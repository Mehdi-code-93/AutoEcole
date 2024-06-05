# from django.shortcuts import redirect, render
# from .models import Member

# def index(request):
#     mem = Member.objects.all()
#     return render(request, 'index.html', {'mem': mem})

# def add(request):
#     return render(request, 'add.html')

# def addrec(request):
#     x = request.POST['first']
#     y = request.POST['last']
#     z = request.POST['email']
#     a = request.POST['mobile']
#     b = request.POST['heurrestante']
#     mem = Member(firstname=x, lastname=y, email=z, mobile=a, heurrestante=b)
#     mem.save()
#     return redirect("/")

# def delete(request, id):
#     mem = Member.objects.get(id=id)
#     mem.delete()
#     return redirect("/")

# def update(request, id):
#     mem = Member.objects.get(id=id)
#     return render(request, 'update.html', {'mem': mem})

# def uprec(request, id):
#     x = request.POST['first']
#     y = request.POST['last']
#     z = request.POST['email']
#     a = request.POST['mobile']
#     b = request.POST['heurrestante']
#     mem = Member.objects.get(id=id)
#     mem.firstname = x
#     mem.lastname = y
#     mem.email = z
#     mem.mobile = a
#     mem.heurrestante = b
#     mem.save()
#     return redirect("/")

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Member

@login_required
def index(request):
    mem = Member.objects.all()
    return render(request, 'index.html', {'mem': mem})

def add(request):
    return render(request, 'add.html')

def addrec(request):
    x = request.POST['first']
    y = request.POST['last']
    z = request.POST['email']
    a = request.POST['mobile']
    b = request.POST['heurrestante']
    mem = Member(firstname=x, lastname=y, email=z, mobile=a, heurrestante=b)
    mem.save()
    return redirect("/")

def delete(request, id):
    mem = Member.objects.get(id=id)
    mem.delete()
    return redirect("/")

def update(request, id):
    mem = Member.objects.get(id=id)
    return render(request, 'update.html', {'mem': mem})

def uprec(request, id):
    x = request.POST['first']
    y = request.POST['last']
    z = request.POST['email']
    a = request.POST['mobile']
    b = request.POST['heurrestante']
    mem = Member.objects.get(id=id)
    mem.firstname = x
    mem.lastname = y
    mem.email = z
    mem.mobile = a
    mem.heurrestante = b
    mem.save()
    return redirect("/")

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    return render(request, 'login.html')

def signup_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.create_user(username=username, password=password)
        user.save()
        login(request, user)
        return redirect('/')
    return render(request, 'signup.html')

def logout_view(request):
    logout(request)
    return redirect('/login')
