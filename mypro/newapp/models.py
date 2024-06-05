from django.db import models

class Member(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    mobile = models.CharField(max_length=20, default="")
    heurrestante = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"

class Creneau(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    date = models.DateField()
    heure = models.TimeField()
    moniteur = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.member.firstname} {self.member.lastname} - {self.date} {self.heure}"