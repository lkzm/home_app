from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length = 69)
    

class Collection (models.Model):
    user = models.ForeignKey('User', on_delete = models.CASCADE)
    name = models.CharField(max_length = 69)
    description = models.CharField (max_length = 255, default = 'none')


def path_fix(album, artist)
class Track (models.Model):
    album = models.CharField(max_length = 69)
    artist = models.CharField(max_length = 69)
    file = model.FileField(upload.to='artist/al
