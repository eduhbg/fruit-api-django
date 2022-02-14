from rest_framework import viewsets
from fruits.models import Region, Fruit
from fruits.serializer import RegionSerializer, FruitSerializer


class RegionViewSet(viewsets.ModelViewSet):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer


class FruitViewSet(viewsets.ModelViewSet):
    queryset = Fruit.objects.all()
    serializer_class = FruitSerializer