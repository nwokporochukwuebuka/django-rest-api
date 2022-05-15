from django.contrib import admin
from .models import Dog, EventMain, EventFeature, EventAttender

# Register your models here.
admin.site.register((Dog, EventAttender, EventMain, EventFeature,))