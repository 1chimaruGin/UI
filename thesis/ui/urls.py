from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('select', views.select_attributes, name='select_attributes'),
    path('classify', views.classify, name='classify'),
]