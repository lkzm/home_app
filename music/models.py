from django.db import models
from music import gvars

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length = gvars.names)
    

class Collection (models.Model):
    user = models.ForeignKey('User', on_delete = models.CASCADE)
    name = models.CharField(max_length = gvars.names)
    description = models.CharField (max_length = gvars.text, default = 'none')


def path_fix(album, artist)
class Track (models.Model):
    title = models.CharField(max_length = gvars.names)
    album = models.CharField(max_length = gvars.names)
    artist = models.CharField(max_length = gvars.names)
    file = models.FileField()
    track_number = models.IntegerField(default=0)

    

