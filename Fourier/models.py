from django.db import models
from django.utils import timezone

class Post(models.Model):
        text = models.TextField()
        upload = models.FileField(upload_to='uploads/', max_length=200, default='null')
        created_date = models.DateTimeField(default=timezone.now) 

def publish(self):
            self.published_date = timezone.now()
            self.save()

def __str__(self):
            return self.text