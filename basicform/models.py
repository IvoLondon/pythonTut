from django.db import models

# Create your models here.
class People(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField(max_length=250)
    text = models.CharField(max_length=250)

    def __str__(self):
        return self.name