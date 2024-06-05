from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages
from .models import Member, Creneau
from collections import defaultdict
import locale
from datetime import datetime, timedelta
from babel.dates import format_date

def index(request):
    members = Member.objects.all()
    creneaux = Creneau.objects.all()
    
    # Préparation des créneaux groupés par jour et par heure
    creneaux_by_day_hour = defaultdict(lambda: defaultdict(list))
    for creneau in creneaux:
        day = creneau.date.strftime('%A')  # Nom du jour
        hour = creneau.heure.strftime('%H')  # Heure en format 24h
        creneaux_by_day_hour[day][hour].append(creneau)
    
    # Ajoutez des instructions de débogage pour vérifier les données
    print("creneaux_by_day_hour:", creneaux_by_day_hour)

    jours = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"]
    heures = range(10, 20)  # Heures de 10h à 19h

    return render(request, 'index.html', {
        'members': members,
        'creneaux': creneaux,
        'creneaux_by_day_hour': creneaux_by_day_hour,
        'jours': jours,
        'heures': heures
    })

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

def add_creneau(request):
    if request.method == 'POST':
        member_id = request.POST['member_id']
        member = get_object_or_404(Member, id=member_id)
        date = request.POST['date']
        heure = request.POST['heure']
        moniteur = request.POST['moniteur']
        creneau = Creneau(member=member, date=date, heure=heure, moniteur=moniteur)
        creneau.save()
        messages.success(request, 'Créneau ajouté avec succès.')
        print(f'Créneau ajouté : {member.firstname} {member.lastname}, Date : {date}, Heure : {heure}, Moniteur : {moniteur}')
        return redirect('/')  # Redirection après l'ajout

    members = Member.objects.all()
    return render(request, 'add_creneau.html', {'members': members})

def creneaux(request, id):
    member = get_object_or_404(Member, id=id)
    if request.method == 'POST':
        date = request.POST['date']
        heure = request.POST['heure']
        moniteur = request.POST['moniteur']
        creneau = Creneau(member=member, date=date, heure=heure, moniteur=moniteur)
        creneau.save()
        messages.success(request, 'Créneau ajouté avec succès.')
        print(f'Créneau ajouté : {member.firstname} {member.lastname}, Date : {date}, Heure : {heure}, Moniteur : {moniteur}')
        return redirect('/')  # Redirection après l'ajout

    return render(request, 'creneaux.html', {'member': member})

def delete(request, id):
    mem = Member.objects.get(id=id)
    mem.delete()
    messages.success(request, 'Membre supprimé avec succès.')
    print(f'Membre supprimé : {mem.firstname} {mem.lastname}')
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
    messages.success(request, 'Informations mises à jour avec succès.')
    print(f'Informations mises à jour : {mem.firstname} {mem.lastname}, Email : {mem.email}, Mobile : {mem.mobile}, Heures restantes : {mem.heurrestante}')
    return redirect("/")
