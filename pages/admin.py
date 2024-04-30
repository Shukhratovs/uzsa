from django.contrib import admin

from .models import Contact, Event


class ContactAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "message")


class EventAdmin(admin.ModelAdmin):
    list_display = ("title", "date", "time", "location")


admin.site.register(Contact, ContactAdmin)
admin.site.register(Event, EventAdmin)
