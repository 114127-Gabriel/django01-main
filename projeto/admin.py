from django.contrib import admin

# Register your models here.
from projeto.models import Agenda, Patient, Professional

class PatientAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name",)
    search_fields = ("first_name", "last_name",)


class ProfessionalAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "specialty",)
    search_fields = ("first_name", "last_name", "specialty",)
    list_filter = ("specialty",)

class AgendaAdmin(admin.ModelAdmin):
    list_display = ("patiente", "professional", "date", "hour", "status",)
    search_fields = ("patiente", "professional", "date", "hour",)
    list_filter = ("patiente", "professional", "date", "hour", "status",)


admin.site.register(Patient, PatientAdmin)
admin.site.register(Professional, ProfessionalAdmin)
admin.site.register(Agenda, AgendaAdmin)