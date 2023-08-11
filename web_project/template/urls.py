# template / urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about", views.aboutUs, name="about"),
    path("outreach", views.outreach, name="outreach"),
    path("schedule", views.schedule, name="schedule"),
    path("resources", views.resources, name="resources"),
    path("leadership", views.leadership, name='leadership'),
    path("contact", views.contact, name="contact"),
    path("calendar", views.CalendarView.as_view(), name="calendar"),
]
