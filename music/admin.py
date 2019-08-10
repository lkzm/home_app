from django.contrib import admin
from music import models
admin.site.register(models.Collection)
admin.site.register(models.Track)
admin.site.register(models.User)
# Register your models here.
