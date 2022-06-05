from django.db import models
from social_django.models import UserSocialAuth

# Create your models here.

class Profile(models.Model):
 
    user = models.OneToOneField(UserSocialAuth, on_delete=models.CASCADE)
    image = models.ImageField(UserSocialAuth, default='default.jpg', upload_to='profile_pics',)
    avatar = models.CharField(max_length=100, null=True, blank=True)
 
    def __str__(self):
        return f'{self.user.username} Profile'