from rest_framework import serializers

from mainapp.models import Order


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"


class OrderCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = (
            "apartment_number", 
            "pet_name", 
            "pet_breed", 
            "walk_date", 
            "walk_time", 
            "walker"
        )
