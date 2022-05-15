
from rest_framework import serializers

from user.serializers import AddressGlobalSerializer, CustomUserSerializer
from .models import EventMain, EventFeature, EventAttender


# The main use of serializers is to enable us send JSON
# responses back to the client containing all the useful informations

class EventFeatureSerializer(serializers.ModelSerializer):
    eventmain = serializers.CharField(read_only=True)
    eventmain_id = serializers.IntegerField(write_only=True)
    

    class Meta:
        model = EventFeature
        fields = "__all__"

    


class EventMainSerializer(serializers.ModelSerializer):
    author = serializers.CharField(required=False) #CustomUserSerializer(read_only=True) now it returns only the email address
    author_email = serializers.ReadOnlyField(source="author.email")
    author_id = serializers.IntegerField(write_only=True) # Hepls us to specify the User Id we are interested in using 
    address_info = AddressGlobalSerializer(read_only=True)
    address_info_id = serializers.IntegerField(write_only=True)
    event_features = EventFeatureSerializer(read_only=True, many=True)
    attenders = serializers.SerializerMethodField("get_attenders")

    class Meta:
        model = EventMain
        fields = "__all__"

    def get_attenders(self, obj):
        attenders = obj.event_attenders.all().count()
        return attenders

class EventAttenderSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(write_only=True)
    user = CustomUserSerializer(read_only=True)
    eventmain = serializers.CharField(read_only=True)
    eventmain_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = EventAttender
        fields = "__all__"