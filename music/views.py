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
            t.album = f.cleaned_data['album']
            t.artist = f.cleaned_data['artist']
            t.track_number = f.cleaned_data['track_number']
            t.save()
            return track_info(request, track_id)
        else:
            context['invalid_f'] = True
            return edit_meta(request, track_id, context)
    else:
        f = forms.MetaDataForm(instance=t)
        context['f'] = f
        return render(request, 'music/track_edit.html', context)
    return render(request, 'music/track_edit.html', context)










# Create your views here.
