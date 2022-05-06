from rest_framework import serializers

from user.serializers import AddressGlobalSerializer, CustomUserSerializer
from .models import EventMain, EventFeature


# The main use of serializers is to enable us send JSON
# responses back to the client containing all the useful informations

class EventFeatureSerializer(serializers.ModelSerializer):
    eventmain = serializers.CharField(read_only=True)
    eventmain_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = EventFeature
        fields = "__all__"


class EventMainSerializer(serializers.ModelSerializer):
    author = CustomUserSerializer(read_only=True)
    author_id = serializers.IntegerField(write_only=True) # Hepls us to specify the User Id we are interested in using 
    address_info = AddressGlobalSerializer(read_only=True)
    address_info_id = serializers.IntegerField(write_only=True)
    event_features = EventFeatureSerializer(read_only=True, many=True)

    class Meta:
        model = EventMain
        fields = "__all__"