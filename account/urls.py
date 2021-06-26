from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url

from django.contrib import admin
urlpatterns = [
    path('', views.home ),
    path('auth/spotify', views.verify ),
    # path('redirect', spotify_callback),
]
urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 