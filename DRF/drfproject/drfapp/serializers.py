from rest_framework import serializers
from drfapp.models import *

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model=Products
        fields= "__all__"   


        # exclude=["stock"]
        # fields= ["id", "name"]


class OrderSerializer(serializers.ModelSerializer):
    # product=ProductSerializer()
    class Meta:
        model=Orders
        fields="__all__"
        # depth=1

#nested Serializer


class CarousalSerializer(serializers.ModelSerializer):

    class Meta:
        model=Carousal
        fields= "__all__" 
        