from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('select', views.select, name='select'),
    path('selectedupload', views.selected_and_upload, name='selectedupload'),
    path('upload', views.result, name='result'),
]