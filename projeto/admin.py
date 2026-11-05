from django.contrib import admin

# Register your models here.
from projeto.models import Agenda

class PatientAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name")
    search_fields = ("first_name", "last_name")


class ProfessionalAdmin(admin.ModelAdmin):
    list_display = ("name", "teacher", "workload", "period")
    search_fields = ("name",)
    list_filter = ("teacher", "period")

class AgendaAdmin(admin.ModelAdmin):
    list_display = ("name", "teacher", "workload", "period")
    search_fields = ("name",)
    list_filter = ("teacher", "period")


admin.site.register(Person, PersonAdmin)
admin.site.register(Course, CourseAdmin)