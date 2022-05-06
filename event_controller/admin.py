from django.contrib import admin
from .models import EventMain, EventFeature, EventAttender

# Register your models here.
admin.site.register((EventAttender, EventMain, EventFeature,))