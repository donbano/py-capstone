from django.db import models
from django.contrib.auth.models import User


class Text(models.Model):
    title = models.CharField
    description = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    modified = models.DateTimeField(auto_now=True)

# Create your models here.
