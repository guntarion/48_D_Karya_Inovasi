# urls.py
from django.urls import path
from .views import create_ideasi

app_name = 'ideasi'

urlpatterns = [
     path('create_ideasi/', create_ideasi, name='create_ideasi'),
]