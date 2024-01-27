from django.urls import path

from .views import openai_request

urlpatterns = [
    path('request/', openai_request, name='openai_request'),
]

