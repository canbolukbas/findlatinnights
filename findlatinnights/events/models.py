from django.db import models


class Event(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='event_images')
    venue = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    does_play_bachata = models.BooleanField()
    does_play_salsa = models.BooleanField()
    does_play_kizomba = models.BooleanField()
    external_url = models.URLField()
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
