from django.contrib import admin
from .models import Authantication
# Register your models here.

class AuthanticationAdmin(admin.ModelAdmin):
    list_display = ('state_speacial_code','police_station_name','police_station_location')

admin.site.register(Authantication, AuthanticationAdmin)

