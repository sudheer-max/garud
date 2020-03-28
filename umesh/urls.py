from django.urls import path
from .views import (
    home,
    domestic,
    domestic_detail,
    search,
    search_int,
    search_hotel,
    international,
    international_detail,
    hotel,
    hotel_detail,
    bus,
    car,
)


app_name = 'umesh'

urlpatterns = [
    path('', home, name='home'),
    path('domestic/', domestic, name='domestic'),
    path('search/', search, name='search'),
    path('search_int/', search_int, name='search_int'),
    path('search_hotel/', search_hotel, name='search_hotel'),
    path('international/', international, name='international'),
    path('hotel/', hotel, name='hotel'),
    path('bus/', bus, name='bus'),
    path('car/', car, name='car'),
    path('hotel-detail/<slug>/', hotel_detail, name='hotel-detail'),
    path('international-detail/<slug>/', international_detail, name='international-detail'),
    path('domestic-detail/<slug>/', domestic_detail, name='domestic-detail'),
]