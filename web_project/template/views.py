from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic
from django.utils.safestring import mark_safe
from datetime import datetime

from template.models import *
from template.utils import Calendar

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

def calendar(request):
    return render(request, 'calendar.html')

def resources(request):
    return render(request, 'resources.html')


class CalendarView(generic.ListView):
    model = Event
    template_name = 'schedule.html'

    def get_context_data(self, **keyword_args):
        context = super.get_context_data(**keyword_args)
        d = get_date(self.request.GET.get('day', None))
        cal = Calendar(d.year, d.month)

        # Call the formatmonth method, which returns our calendar as a table
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        return context

def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return date(year, month, day=1)
    return datetime.today()