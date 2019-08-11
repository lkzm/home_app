from django.shortcuts import render
from music import models, forms


def select_user (request, context = {}):
    try:
        u = request.session['user']
        return library(request, u.id)
    except:
        u = models.User.objects.all()
        context['u'] = u
        return render(request, 'music/select_user.html', context)

def us (request, user_id, context = {}):
    request.session['user'] = user_id
    return library(request, user_id)

def library (request, user_id, context = {}):
    c = models.Collection.objects.get(user = user_id)
    context['c'] = c
    return render(request, 'music/library.html', context)

def track_info (request, track_id, context = {}):
    t = models.Track.objects.get(pk = track_id)
    context['t'] = t
    return render(request, 'music/track_info.html', context)

def edit_meta (request, track_id, context = {} ):
    t = models.Track.objects.get(pk = track_id)
    context['t'] = t
    if request.method == 'POST':
        f = forms.MetaDataForm(request.POST)
        context['f'] = f  
        if f.is_valid():
            t.title = f.cleaned_data['title']
            t.album = f.cleaned_data['album']
            t.artist = f.cleaned_data['artist']
            t.track_number = f.cleaned_data['track_number']
            t.save()
            return track_info(request, track_id)
        else:
            context['invalid_f'] = True
            return edit_meta(request, track_id, context)
    else:
        data = {}
        data['title'] = t.title
        data['album'] = t.album
        data['artist'] = t.artist
        data['track_number'] = t.track_number
        f = forms.MetaDataForm(initial=data)
        context['f'] = f
        return render(request, 'music/track_edit.html', context)
    return render(request, 'music/track_edit.html', context)


def upload_track (request, context =  {} ):


    if request.method == 'POST':
        f = forms.UploadFileForm(request.POST)
        context['fu'] = f
        if f.is_valid():
            file = f.cleaned_data['file']
            t = models.Track.objects.create(track_number=0, title="title", album="album", artist="artist", file=file)
            t.save()
            return edit_meta(request, t.pk)
        else:

            return render(request,'music/upload_track.html', context)
    else:
        f = forms.UploadFileForm()
        context['fu'] = f 
        return render(request,'music/upload_track.html', context)
    return render(request, 'music/upload_track.html', context)












# Create your views here.
