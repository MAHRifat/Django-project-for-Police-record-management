from django.contrib import admin
from .models import Record_entry_NID,Record_entry_DOB
# Register your models here.

class Record_entry_NID_Admin(admin.ModelAdmin):
    list_display = ('nid_number','name','father_name', 'mother_name','birthmark','extraIdentificationMark','Address','phone_number','date_of_birth','crime_type', 'crime_location', 'crime_date_time','crime_status','picture')
class Record_entry_DOB_Admin(admin.ModelAdmin):
    list_display = ('Birth_certification_number','name','father_name', 'mother_name','birthmark','extraIdentificationMark','Address','phone_number','date_of_birth','crime_type', 'crime_location', 'crime_date_time','crime_status','picture')

admin.site.register(Record_entry_NID, Record_entry_NID_Admin)
admin.site.register(Record_entry_DOB,Record_entry_DOB_Admin)