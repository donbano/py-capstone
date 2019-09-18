from django.db import models
from django.contrib.auth.models import User


class Word(models.Model):
    title = models.CharField(max_length=40)
    isBad = models.BooleanField
    isGood = models.BooleanField
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    modified = models.DateTimeField(auto_now=True)
# Create your models here.
