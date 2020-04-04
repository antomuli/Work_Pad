from django.contrib import admin
from .models import *


# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    filter_horizontal=('assigned_to')
admin.site.register(profile)
admin.site.register(tasks,TaskAdmin)
admin.site.register(kpis)


