from django.shortcuts import render
from .models import *

# Pages
def home(request):
    Testimonials = Testimonial.objects.all()
    context = {'testimonials' : Testimonials , 'title':'Home'}
    return render(request, 'Nirvata/index.html',context)

def about(request):
    return render(request, 'Nirvata/about.html',{'title':'About'})

def projects(request):
    Projects = Project.objects.all()
    context = {'projects' : Projects , 'title':'Projects'}
    return render(request, 'Nirvata/projects.html', context)

def gallery(request):
    Photos = GalleryPhoto.objects.all()
    context = {'photos' : Photos , 'title':'Gallery'}
    return render(request, 'Nirvata/gallery.html', context)

def donate(request):
    return render(request, 'Nirvata/donate.html',{'title':'Donate'})

def contact(request):
    return render(request, 'Nirvata/contact.html',{'title':'Contact Us'})
