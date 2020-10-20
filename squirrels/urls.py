from django.urls import path

from . import views

app_name = 'squirrels'

urlpatterns = [
   # path('', views.index, name='index'),
    path('map/', views.map, name='map'),
    path('sightings/', views.sightings, name='sightings'),
    path('sightings/<squirrel_id>/', views.unique, name='unique'),
    path('sightings/add/', views.add, name='add'),
]


