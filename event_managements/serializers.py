from rest_framework import serializers
from .models import Troupe, Event

class TroupeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Troupe
        fields = '__all__'

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'