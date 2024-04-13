from django.shortcuts import render

from .models import Contact


# Create your views here.
def index(request):
    return render(request, "index.html")


def events(request):
    return render(request, "events.html")


def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        new_contact = Contact(name=name, email=email, message=message)
        new_contact.save()
        return render(request, "contact.html", {"message": "Thank you for reaching out to us!"})
    return render(request, "contact.html")


def explore(request):
    return render(request, "explore.html")