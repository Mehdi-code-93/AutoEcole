from django.shortcuts import redirect, render
from .models import Member

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
