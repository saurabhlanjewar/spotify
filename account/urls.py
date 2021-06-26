from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url

from django.contrib import admin
urlpatterns = [
    path('', home),
    path('home', UserProfile.as_view()),
    path('auth/spotify', AuthURL.as_view()),
    path('redirect', spotify_callback),
    path('is-authenticated', IsAuthenticated.as_view())
]
urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 