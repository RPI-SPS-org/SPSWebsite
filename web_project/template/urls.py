from django.urls import path
from template import views

urlpatterns = [
    path("", views.home, name="home"),
]
