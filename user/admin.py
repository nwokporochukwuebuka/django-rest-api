from django.contrib import admin
from .models import AddressGlobal, CustomUser, UserProfile

# Register your models here.
admin.site.register((CustomUser, UserProfile, AddressGlobal,))