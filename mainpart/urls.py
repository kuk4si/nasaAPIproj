
from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='index'),
    path('asteroids_neows/', asteroids_neows, name='asteroids_neows'),
    path('neo_lookup/', neo_lookup, name='neo_lookup'),
    path('mars_rover_photos/', mars_rover_photos, name='mars_rover_photos')
]
