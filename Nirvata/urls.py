from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='Nirvata-home'),
    path('about/', views.about, name='Nirvata-about'),
    path('projects/', views.projects, name='Nirvata-projects'),
    path('gallery/', views.gallery, name='Nirvata-gallery'),
    path('donate/', views.donate, name='Nirvata-donate'),
    path('contact/', views.contact, name='Nirvata-contact'), 
]
