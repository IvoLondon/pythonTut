from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class People(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField(max_length=250)
    text = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    portfolio = models.URLField()
    picture = models.ImageField(
                                upload_to='profile_pics',
                                )

    def __str__(self):
        return self.user.username
