from django.urls import path

from .views import makalah_home, makalah_create, makalah_edit, makalah_single_view, masukan_home, masukan_single_view

urlpatterns = [
    path('', makalah_home, name='makalah_home'),
    path('masukan/', masukan_home, name='masukan_home'),
    path('masukan/<int:masukan_id>/',
         masukan_single_view, name='masukan_single_view'),
    path('makalah-create/', makalah_create, name='makalah_create'),
    path('makalah-edit/<int:makalah_id>/', makalah_edit, name='makalah_edit'),
    path('makalah/<int:makalah_id>/',
         makalah_single_view, name='makalah_single_view'),
]

