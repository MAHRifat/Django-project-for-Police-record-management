from django.db import models

# Create your models here.

class Authantication(models.Model):
    state_speacial_code = models.IntegerField(primary_key = True,default = False)
    police_station_name = models.CharField(max_length = 100, default = False)
    police_station_location = models.CharField(max_length = 100, default = False)

    def __str__(self):
        return self.police_station_name
