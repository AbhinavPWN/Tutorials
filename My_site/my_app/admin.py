from django.contrib import admin
from my_app.models import Patient, Review, Teacher
# Register your models here.
admin.site.register(Patient)
admin.site.register(Review)
admin.site.register(Teacher)
