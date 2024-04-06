from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, "index.html")


def events(request):
    return render(request, "events.html")


def contact(request):
    return render(request, "contact.html")


def explore(request):
    return render(request, "explore.html")