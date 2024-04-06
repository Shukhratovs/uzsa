from django.urls import path

from .views import *

urlpatterns = [
    path("", index, name="index"),
    path("events/", events, name="events"),
    path("contact/", contact, name="contact"),
    path("explore/", explore, name="explore"),
]