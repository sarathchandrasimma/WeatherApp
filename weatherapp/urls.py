from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('', views.weather_game, name='weather_game'),
]