from django.db import models

# Create your models here.
class Contactus(models.Model):
    contactid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=55)
    email = models.EmailField(max_length=25)
    mobile = models.CharField(max_length=15)
    desc = models.CharField(max_length=1000)

class Meta:
    db_table = "contactus"