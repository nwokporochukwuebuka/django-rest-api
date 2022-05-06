from django.db import models
from user.models import CustomUser, AddressGlobal


# Create your models here.

class EventMain(models.Model):
    # Direct relationship with the User model
    author = models.ForeignKey(CustomUser, related_name='user_events', on_delete=models.CASCADE)
    # Direct relationship with the Address
    address_info = models.ForeignKey(AddressGlobal, related_name='event_address', on_delete=models.CASCADE)

    title = models.CharField(max_length=50, unique=True)

    description = models.TextField()

    date = models.DateField(auto_created=True)

    time = models.TimeField()

    max_seat = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class EventFeature(models.Model):
    # inverse relationship with the main event
    eventmain = models.ForeignKey(EventMain, related_name='event_features', on_delete=models.CASCADE)

    feature_name = models.CharField(max_length=20)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.eventmain.title} - {self.feature_name}"

class EventAttender(models.Model):
    # inverse relationship with the main event
    eventmain = models.ForeignKey(EventMain, related_name='event_attenders', on_delete=models.CASCADE)
    #inverse relationship with the User
    user = models.ForeignKey(CustomUser, related_name='event_attendant', on_delete=models.CASCADE)

    time = models.TimeField()

    created_at = models.DateTimeField(auto_now_add=True)
    
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.eventmain.title} - {self.user.name}"