from django.contrib import admin
from . import models

admin.site.register(models.Employee)


@admin.register(models.EmpClockin)
class ClockinAdmin(admin.ModelAdmin):
    list_display = ('emp', 'clockinTime', 'clockinDate')
    list_filter = ('emp', 'clockinTime')
    search_fields = ('emp__name', 'clockinTime')
