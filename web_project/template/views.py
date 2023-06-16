from django.http import HttpResponse
from django.shortcuts import render

#replace return HttpResponse
# return render(request, 'homepage/homepage.html')

def home(request):
    return render(request, 'homepage.html')

def aboutUs(request):
    return HttpResponse("Placeholder")

def outreach(request):
    return HttpResponse("Placeholder")

def demos(request):
    return HttpResponse("Placeholder")

def schedule(request):
    return HttpResponse("Placeholder")

def resources(request):
    return HttpResponse("Placeholder")