from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .models import Contact

import telebot
from django.core.exceptions import PermissionDenied
from django.conf import settings
from django.http import HttpResponse as HTTPResponse


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
        new_contact_text = f"New message from {name} ({email}): {message}"
        new_contact_bot(new_contact_text)
        return render(request, "contact.html", {"message": "Thank you for reaching out to us!"})
    return render(request, "contact.html")


def explore(request):
    return render(request, "explore.html")


# =============================BOT VIEWS================================
TOKEN = settings.TELEGRAM_BOT_TOKEN
tbot = telebot.TeleBot(TOKEN)

MANAGERS = [5504582776, 59681342]


@csrf_exempt
def bot(request):
    if request.content_type == 'application/json':
        json_str = request.body.decode('UTF-8')
        update = telebot.types.Update.de_json(json_str)
        tbot.process_new_updates([update])
        return HTTPResponse("")
    else:
        raise PermissionDenied


@tbot.message_handler(commands=['start'])
def greet_new_member(message):
    tbot.send_message(message.chat.id, "Welcome to UZSA!")
    print(message.chat.id)


def new_contact_bot(text):
    for manager in MANAGERS:
        tbot.send_message(manager, text)


def set_webhook():
    tbot.remove_webhook()
    tbot.set_webhook(url="https://uzsa.org/uzsa_bot/")
    print("Webhook set!")


set_webhook()
