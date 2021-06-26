from django.shortcuts import render
from rest_framework.views import APIView
from requests import Request
from rest_framework.response import Response
from .credentials import REDIRECT_URI, CLIENT_SECRET, CLIENT_ID

# Create your views here.
def home(request):
    return render(request,'account/home.html')

def verify(request):
    scopes = 'user-library-read user-read-private user-read-email user-read-recently-played user-top-read user-follow-read playlist-read-private playlist-read-collaborative'
    url = Request('GET', 'https://accounts.spotify.com/authorize', params={
            'scope': scopes,
            'response_type': 'code',
            'redirect_uri': REDIRECT_URI,
            'client_id': CLIENT_ID
        }).prepare().url

    return Response(url)