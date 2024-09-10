from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
    name = models.CharField(max_length=50)    
    def __str__(self):
        return self.name


class contact(models.Model):
    frist_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    created_at = models.DateTimeField(default=timezone.now)
    description = models.TextField()
    show = models.BooleanField(default=True)
    picture = models.ImageField(blank=True, upload_to='pictures/%Y/%m')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL,blank=True, null=True)
    
    def __str__(self):
        return self.frist_name + ' ' + self.last_name
