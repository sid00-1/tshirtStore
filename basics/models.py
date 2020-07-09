from django.db import models
from core.models import Item
# Create your models here.


class TestM(models.Model):
    message = models.TextField(null=True, blank=True)
    name = models.CharField(max_length=150, null=True, blank=True)
    email = models.EmailField(max_length=150, null=True, blank=True)

    def __str__(self):
        return f'{self.name}'


class ContactM(models.Model):
    message = models.TextField(null=True, blank=True)
    name = models.CharField(max_length=150, null=True, blank=True)
    email = models.EmailField(max_length=150, null=True, blank=True)

    def __str__(self):
        return f'{self.name}'


class Review(models.Model):
    review = models.TextField(default="Great Product!", null=True, blank=True)
    name = models.CharField(max_length=150, null=True, blank=True)
    item = models.ManyToManyField(Item)

    def __str__(self):
        return f'{self.review}'
