from django.db import models
from django.utils import timezone

# Create your models here.


class VeterinaryOfficer(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=254)
    county = models.CharField(max_length=100)
    idNo = models.CharField(max_length=50)
    mobile_number = models.CharField(max_length=20)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Veterinary Officers'
        db_table = 'Veterinary_Officers'
