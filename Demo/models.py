from django.db import models

# Create your models here.

class Book(models.Model):
    bname = models.CharField(max_length=200, blank=True, null=True)
    pub = models.ForeignKey('Publisher', on_delete=models.PROTECT, related_name='book', db_column='pid', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'book'


class Publisher(models.Model):
    pname = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'publisher'


class User_data(models.Model):
    uname = models.CharField(max_length=10)
    icon = models.ImageField(upload_to='%Y%m/icons')
