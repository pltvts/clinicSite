from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('doctors', views.doctors, name='doctors'),
    path('appoint', views.appoint, name='appoint'),
    path('services', views.services, name='services'),
]
