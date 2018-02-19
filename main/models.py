from django.db import models

# Create your models here.
class fund_info(models.Model):
    name = models.CharField(max_length=200)
    founding_date = models.DateTimeField('date founded')


