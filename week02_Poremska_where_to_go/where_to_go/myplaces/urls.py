from django.urls import path
from . import views

app_name = "myplaces"

urlpatterns = [
    path("home/", views.home, name="home"),
    path("places/", views.places_list, name="places_list"),
    path("places/add/", views.add_place, name="add_place"),
    path("places/<int:place_id>/", views.place_detail, name="place_detail"),
]
