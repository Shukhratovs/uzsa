from django.contrib import admin

from .models import CustomUser

admin.site.site_header = "UZSA Admin"
admin.site.register(CustomUser)
