from django.db import models
from authantication.models import Authantication
# Create your models here.

class Record_entry_NID(models.Model):
    nid_number = models.CharField(max_length = 20,primary_key = True)
    name = models.CharField(max_length = 100, default = None)
    father_name = models.CharField(max_length = 100, default = None)
    mother_name = models.CharField(max_length = 100, default = None)
    birthmark = models.CharField(max_length = 100, default = None)
    extraIdentificationMark = models.CharField(max_length = 100, default = None)
    Address = models.CharField(max_length = 200, default = None)
    phone_number = models.CharField(max_length = 11, null = False)
    date_of_birth = models.DateField(null = False, default = None)
    crime_type = models.CharField(max_length = 50, default = None)
    crime_location = models.CharField(max_length = 200, default = None)
    crime_date_time = models.DateTimeField(null = False)
    crime_status = models.CharField(max_length = 50, default = None)
    picture = models.ImageField(upload_to= 'img',null=True, blank=True, default=False)
    def __str__(self) -> str:
        return f"{self.nid_number}"
    
    
class Record_entry_DOB(models.Model):
    Birth_certification_number = models.CharField(max_length=100,primary_key = True)
    name = models.CharField(max_length = 100, default = None)
    father_name = models.CharField(max_length = 100, default = None)
    mother_name = models.CharField(max_length = 100, default = None)
    birthmark = models.CharField(max_length = 100, default = None)
    extraIdentificationMark = models.CharField(max_length = 100, default = None)
    Address = models.CharField(max_length = 200, default = None)
    phone_number = models.CharField(max_length = 11, null = False)
    date_of_birth = models.DateField(null = False, default = None)
    crime_type = models.CharField(max_length = 50, default = None)
    crime_location = models.CharField(max_length = 200, default = None)
    crime_date_time = models.DateTimeField(null = False)
    crime_status = models.CharField(max_length = 50, default = None)
    picture = models.ImageField(upload_to= 'img',null=True, blank=True, default=False)
    def __str__(self) -> str:
        return f"{self.Birth_certification_number}"
    

class SecureCodeModel(models.Model):
    id = models.IntegerField(primary_key=True)
    secure_code = models.ForeignKey(Authantication, on_delete = models.CASCADE)


    