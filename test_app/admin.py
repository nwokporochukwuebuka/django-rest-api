from django.contrib import admin
from .models import Blog

#from .models import TestModel
# Register your models here.

'''admin.site.register(TestModel)
admin.site.register(ModelX)'''

admin.site.register((Blog, ))