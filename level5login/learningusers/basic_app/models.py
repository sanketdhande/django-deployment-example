from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class UserProfileInfo(models.Model):
    user_info = models.OneToOneField(User,on_delete=models.CASCADE)
    portfolio_site = models.URLField(blank = True)
    profile_pic = models.ImageField(upload_to = 'profile_pics',blank = True)
    bio = models.CharField(max_length = 200, blank = False)
    def __str__(self):
        return self.user_info.username
