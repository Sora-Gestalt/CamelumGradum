from django.db import models
import datetime

class Coffee_Bags(models.Model):
    CName   = models.CharField(max_length=80, null=False) # [Coffee-Bag:Roaster_Name + Coffee_Family_Name]
    CBP     = models.ImageField(null=False, upload_to='Coffee-Bags') # [Should be in .svg form]
    CBD     = models.TextField(default="Sorry No Description Has Been Added ;-;", null=False) # [Should include (Family name , Country , Roast date , Plantation details {Degree in C, land height from sea})]
    Country = models.CharField(max_length=56, null=False) # [Should be one of those (Yemen,France,Ethopia,Colombia,Saudi Arabia,CostaRica,Ghana,Italy)]
    Cdate   = models.DateField(default=datetime.date.today)
    price   = models.PositiveIntegerField(null=False)
