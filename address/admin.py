# -*- coding: utf-8 -*-
from django.contrib import admin

from address import models


@admin.register(models.Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(models.Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(models.City)
class CityAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(models.District)
class DistrictAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(models.Street)
class StreetAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(models.House)
class HouseAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(models.Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ['country', 'region', 'city', 'district', 'street', 'house']
