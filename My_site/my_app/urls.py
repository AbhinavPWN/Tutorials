from django.contrib import admin
from django.urls import path
from . import views

app_name = 'my_app'


urlpatterns = [
    path('', views.index, name='index'),
    path('variable/', views.variable_view, name='variable'),
    path('rental_review', views.rental_review, name='rental_review'),
    path('thank_you', views.thankyou, name='thank_you'),
]
