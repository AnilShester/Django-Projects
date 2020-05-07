from django.db import models
from users.models import UserProfilePic
# Create your models here.

class Topic(models.Model):
    text = models.CharField(max_length=100)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text


class Entry(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Entries'

    def __str__(self):
        return self.text[:50] + '.....'

