from django.urls import path, include
from django.contrib import admin
from app1 import views

app_name= 'pc'

urlpatterns = [
    path('about-us/',views.index, name='About'),
    path('admissions/',views.admissions, name='Admissions'),
    path('contact-us/',views.contact, name='Contact'),
    path('curriculum/',views.curriculum, name='Curriculum'),
    path('fees/',views.fees, name='Fees'),
]