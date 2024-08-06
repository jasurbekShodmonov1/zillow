from rest_framework import serializers
from .models import Property, Listing

class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = '__all__'

class ListingSerializer(serializers.ModelSerializer):
    property = PropertySerializer()

    class Meta:
        model = Listing
        fields = '__all__'
