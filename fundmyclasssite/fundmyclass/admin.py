from django.contrib import admin
from .models import TeacherInfo
from .models import SchoolInfo
# Register your models here.


class TeacherInfoAdmin(admin.ModelAdmin):
   fieldsets = [
       ("Identity", {"fields": ["first_name", "last_name", "subject"]}),
       ("Supples", {"fields": ["supply_list", "supply_cost"]}),
       ("School", {"fields": ["school_id"]})
   ]

admin.site.register(TeacherInfo, TeacherInfoAdmin)
admin.site.register(SchoolInfo)
