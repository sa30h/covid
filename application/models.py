from django.db import models

# Create your models here.

class Covidcases(models.Model):
    country=models.CharField( max_length=100)
    total_case=models.IntegerField()
    date=models.DateField()

    def __str__(self):
        return str(self.country+" "+str(self.date))
