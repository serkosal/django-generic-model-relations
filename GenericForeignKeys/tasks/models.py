from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models


# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=150)


class Group(models.Model):
    name = models.CharField(max_length=150)
    creator = models.ForeignKey(Person, on_delete=models.PROTECT)


class Tasks(models.Model):
    description = models.CharField(max_length=200)
    
    owner_id = models.PositiveBigIntegerField()
    owner_type = models.ForeignKey(ContentType, on_delete=models.PROTECT)
    
    owner = GenericForeignKey('owner_type', 'owner_id')
    
    class Meta:
        verbose_name_plural = 'tasks'
