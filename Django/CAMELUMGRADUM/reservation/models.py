from django.db import models
from django.utils import timezone
# Create your models here.

class Reserve(models.Model):
    RName = models.CharField(max_length=80, null=False)
    RDate = models.DateField(null=False)
    RTime = models.TimeField(null=False,default=timezone.now())
    RPersons = models.PositiveIntegerField(null=False)