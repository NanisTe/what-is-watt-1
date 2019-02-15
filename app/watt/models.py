from django.db import models


class ItemManager(models.Manager):
    pass

class Item(models.Model):
    name = models.CharField(max_length=200)
    power = models.PositiveIntegerField() # kWh/h from CSV or Wh/h
    times_per_hour = models.PositiveIntegerField() # standard usage value
    power_type = models.CharField(max_length=200) # type, electricity, gas, gasoline, diesel, heat,
    unit = models.CharField(max_length=200)
    default_usage = models.FloatField()
    url_data = models.CharField()

    objects = ItemManager()

    def __str__(self):
        return self.name

class Converter(models.Model):
    name = models.CharField(max_length=200)
    unit_in = models.CharField(max_length=200) # TODO define a class of units: with unit type and conversion methods
    unit_out = models.CharField(max_length=200) # TODO define a class of units
    conversion_factor = models.FloatField()
    unit = models.CharField(max_length=200)

    objects = ItemManager()

    def __str__(self):
        return self.name


#TODO define class of kwh to distinguish between electricity and other energy carriers.
