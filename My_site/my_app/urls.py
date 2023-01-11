from django.contrib import admin
from django.urls import path
from . import views
from .views import ThankYouView

app_name = 'my_app'
# domain.com/my_app/......

urlpatterns = [
    path('', views.index, name='index'),
    path('variable/', views.variable_view, name='variable'),
    path('rental_review', views.rental_review, name='rental_review'),
    path('thank_you', ThankYouView.as_view(), name='thank_you'),
]
