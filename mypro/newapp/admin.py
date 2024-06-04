from django.contrib import admin
from .models import Member

class MemberAdmin(admin.ModelAdmin):
    list_display="firstname","lastname","email", "mobile", "heurrestante"

admin.site.register(Member,MemberAdmin)
