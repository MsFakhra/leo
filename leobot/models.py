from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    text = models.CharField(max_length=500)
    emotions = models.CharField(max_length=700)
    before = models.CharField(max_length=100)
    after = models.CharField(max_length=100)
    prolific = models.CharField(max_length=100,default='0000000')
    def __str__(self):
        return self.name
