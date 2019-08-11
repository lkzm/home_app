from music import models
from django import forms
from music import gvars

class UploadFileForm (forms.Form):
    file = forms.FileField()


class MetaDataForm (forms.Form):
    title = forms.CharField(max_length=gvars.names)
    album = forms.CharField(max_length=gvars.names)
    artist = forms.CharField(max_length=gvars.names)
    track_number = forms.IntegerField()

class CreateCollectionForm (forms.Form):
    name = forms.CharField(max_length=gvars.names)
    description = forms.CharField(max_length=gvars.text)


