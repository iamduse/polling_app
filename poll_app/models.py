from django.db import models

# Create your models here.
class Candidates(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    party = models.CharField(max_length=200, default='unknown')

    def __str__(self):
        return self.name




