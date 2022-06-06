from django.db import models
from django.conf import settings

# Create your models here.


class Profile(models.Model):

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='users/%Y/%m/%d', blank=True)
    avatar = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'


class PlaceMarker(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    marker_name = models.CharField(max_length=40)
    x_map_pos = models.FloatField(name='x_position')
    y_map_pos = models.FloatField(name='y_position')
    description = models.TextField(max_length=4000)

    def __str__(self):
        return f'{self.user.username} {self.marker_name} marker'
