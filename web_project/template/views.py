from django.http import HttpResponse

#replace return HttpResponse
# return render(request, 'homepage/homepage.html')

def home(request):
    return HttpResponse("Hello, Django!")

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