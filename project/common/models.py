from django.db import models

# Create your models here.

class Laborer(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=10)
    
    email = models.CharField(max_length=30)


    class Meta:
        db_table = "laborer"


class AppAdmin(models.Model):
    id = models.AutoField(primary_key=True)
    password = models.CharField(max_length=10)
    email = models.CharField(max_length=30)

    class Meta:
        db_table = "appadmin"
