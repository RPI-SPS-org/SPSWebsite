from django.http import HttpResponse
from django.shortcuts import render

#replace return HttpResponse
# return render(request, 'homepage/homepage.html')

def home(request):
    return render(request, 'homepage.html')

def aboutUs(request):
    return render(request, 'aboutus.html')

def contact(request):
    return render(request, 'contact.html')

def leadership(request):
    return render(request, 'leadership.html')

def outreach(request):
    return render(request, 'outreach.html')

def demos(request):
    return render(request, 'demos.html')

def schedule(request):
    return render(request, 'schedule.html')

def resources(request):
    return render(request, 'resources.html')
