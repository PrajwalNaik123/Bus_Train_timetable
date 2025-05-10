from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('search-bus/', views.search_buses, name='search_bus'),
    path('search-train/', views.search_trains, name='search_train'),
    path('suggest/', views.suggest_routes, name='suggest_routes'),
]