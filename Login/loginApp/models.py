from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # add any new fields if needed
    protfoilo = models.URLField(blank=True)
    profile_pic =models.ImageField(upload_to='profile_pics', blank=True)

    def __str__(self):
        return self.user.username


