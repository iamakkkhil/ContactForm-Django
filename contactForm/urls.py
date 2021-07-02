from django.contrib import admin
from django.urls import path
from contactForm import views 

urlpatterns = [
    path('', views.index, name='contactForm'),
    path('portfolio', views.contactMe, name='contactMe')
]
