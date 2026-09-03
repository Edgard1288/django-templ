from django.urls import path
from . import views

name_app="inicio"

urlpatterns = [
    path('', views.index, name='inicio'),
]
