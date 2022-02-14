from rest_framework import serializers
from fruits.models import Region, Fruit


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ['id', 'name']


class FruitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fruit
        fields = ['id', 'name', 'region']