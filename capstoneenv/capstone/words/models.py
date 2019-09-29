from django.db import models
from django.contrib.auth.models import User


class Word(models.Model):
    word = models.CharField(max_length=40)
    isGood = models.BooleanField(default=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{} - {} - {}".format(self.word, self.created_by, self.created)


class Text(models.Model):
    title = models.CharField(max_length=180)
    content = models.TextField()
    badWordCount = models.IntegerField(default=0)
    goodWordCount = models.IntegerField(default=0)
    isGood = models.BooleanField(default=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{} - {} - {}".format(self.title, self.created_by, self.created)
# Create your models here.
