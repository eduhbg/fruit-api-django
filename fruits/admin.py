from django.contrib import admin
from fruits.models import Fruit
from fruits.models import Region


class Fruits(admin.ModelAdmin):
    list_display = ('id', 'name', 'region')
    list_display_links = ('id', 'name')
    serach_fields = ('name', 'region')


class Regions(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    serach_fields = ('name')


admin.site.register(Fruit, Fruits)
admin.site.register(Region, Regions)