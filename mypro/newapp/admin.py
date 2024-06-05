from django.contrib import admin
from .models import Member, Creneau

class MemberAdmin(admin.ModelAdmin):
    list_display = ("firstname", "lastname", "email", "mobile", "heurrestante")

class CreneauAdmin(admin.ModelAdmin):
    list_display = ("member", "date", "heure", "moniteur")

admin.site.register(Member, MemberAdmin)
admin.site.register(Creneau, CreneauAdmin)
