from django.contrib import admin
from django.urls import path
from . import views
from .views import ThankYouView, ContactFormView, TeacherCreateView, TeacherListView, TeacherDetailView, TeacherUpdateView, TeacherDeleteView

app_name = 'my_app'
# domain.com/my_app/......

urlpatterns = [
    path('', views.index, name='index'),
    path('variable/', views.variable_view, name='variable'),
    path('rental_review', views.rental_review, name='rental_review'),
    path('thank_you', ThankYouView.as_view(), name='thank_you'),
    path('contact_us', ContactFormView.as_view(), name='contact'),
    path('teacher_form', TeacherCreateView.as_view(), name='teacher_form'),
    path('teacher_lists', TeacherListView.as_view(), name='teacher_lists'),
    path('teacher_details/<int:pk>',
         TeacherDetailView.as_view(), name='teacher_detail'),
    path('update_teacher/<int:pk>',
         TeacherUpdateView.as_view(), name='update_teacher'),
    path('delete_teacher/<int:pk>',
         TeacherDeleteView.as_view(), name='delete_teacher')
]
