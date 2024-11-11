from django.conf.urls import handler404
from django.urls import path
from . import views

urlpatterns = [
    path('not_found/', views.not_found, name='not_found'),
    path('about/', views.about, name='about'),
    path('appointment/', views.appointment, name='appointment'),
    path('contact/', views.contact, name='contact'),
    path('feature/', views.feature, name='feature'),
    path('', views.index, name='index'),
    path('service/', views.service, name='service'),
    path('team/', views.team, name='team'),
    path('testimonial/', views.testimonial, name='testimonial'),
]
# Global 404 handler
handler404 = 'clinicapp.views.not_found'