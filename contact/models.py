from django.db import models
from django.utils import timezone
# Create your models here.

class contact(models.Model):
    frist_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    created_at = models.DateTimeField(default=timezone.now)
    description = models.TextField()
    show = models.BooleanField(default=True)
    picture = models.ImageField(blank=True, upload_to='pictures/%Y/%m')
    
    def __str__(self):
        return self.frist_name + ' ' + self.last_name
