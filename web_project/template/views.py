from django.http import HttpResponse
from django.shortcuts import render

#replace return HttpResponse
# return render(request, 'homepage/homepage.html')

def home(request):
    return render(request, 'homepage.html')

def aboutUs(request):
    return HttpRespone("Placeholder")

def outreach(request):
    return HttpRespone("Placeholder")

def demos(request):
    return HttpRespone("Placeholder")

def schedule(request):
    return HttpRespone("Placeholder")

def resources(request):
    return HttpRespone("Placeholder")