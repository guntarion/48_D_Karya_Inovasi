from django.urls import path

from .views import openai_request, openai_request_for_ideasi

urlpatterns = [
    path('request/', openai_request, name='openai_request'),
    path('ideasi/', openai_request_for_ideasi, name='openai_request_for_ideasi'),
]

