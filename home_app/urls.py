"""home_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from music import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('select_user/', views.select_user, name = 'Select User'),
    path('us%<user_id>/', views.us, name = 'us'),
    path('library/', views.library, name = 'Library'),
    path('track_info%<track_id>/', views.track_info, name = 'edit_track'),
    path('track_edit%<track_id>/', views.edit_meta, name = 'edit_meta'),
    path('track_upload/', views.upload_track, name = 'upload_track'),

]
