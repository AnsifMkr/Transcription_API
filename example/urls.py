# example/urls.py
from django.urls import path

from example.views import index, AudioTranscript


urlpatterns = [
    path('', index),
    path('api/transcript/', AudioTranscript),
]