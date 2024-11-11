from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def about(request):
    return render(request, 'about.html')

def appointment(request):
    return render(request, 'appointment.html')

def contact(request):
    return render(request, 'contact.html')

def feature(request):
    return render(request, 'feature.html')

def index(request):
    return render(request, 'index.html')

def service(request):
    return render(request, 'service.html')

def team(request):
    return render(request, 'team.html')

def testimonial(request):
    return render(request, 'testimonial.html')

def not_found(request):
    return render(request, '404.html')
