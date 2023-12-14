from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=False)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=50)
    images = models.ImageField(default='avatar.jpg', upload_to='media/images')

    def __str__(self):
        return f'{self.user.username}-Profile'
