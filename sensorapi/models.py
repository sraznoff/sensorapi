from django.db import models

class Sensor(models.Model):
    name = models.CharField(max_length = 50)
    description = models.CharField(max_length  =200)
    location = models.CharField(max_length = 100)
    last_reading = models.DecimalField(max_digits = 18, decimal_places = 8)
    last_reading_time = models.DateTimeField(auto_now = True)

class Reading(models.Model):
    sensor_id = models.ForeignKey(Sensor, on_delete = models.DO_NOTHING)
    location = models.CharField(max_length = 100)
    reading = models.DecimalField(max_digits = 18, decimal_places = 8)
    reading_time = models.DateTimeField()