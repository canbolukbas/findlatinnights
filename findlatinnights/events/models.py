from collections.abc import Iterable
from django.db import models
from django.core.exceptions import ValidationError


class Event(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='event_images', blank=True, null=True)
    venue = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    does_play_bachata = models.BooleanField()
    does_play_salsa = models.BooleanField()
    does_play_kizomba = models.BooleanField()
    external_url = models.URLField()
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()

    def __str__(self) -> str:
        return f'{self.title}'

    def clean(self):
        if self.end_datetime <= self.start_datetime:
            raise ValidationError("End time must be after start time")

    def save(self):
        self.full_clean()
        return super().save()
