from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('attendance/', views.attendance, name='attendance'),
    path('students/', views.students, name='students'),
    path('contact/', views.contact, name='contact'),
]