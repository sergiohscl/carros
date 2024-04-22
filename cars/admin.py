from django.contrib import admin
from cars import models


@admin.register(models.Brand)
class Brand(admin.ModelAdmin):
    list_display = ('name', )


@admin.register(models.Car)
class CarAdmin(admin.ModelAdmin):
    list_display = (
        'model', 'brand', 'factory_year',
        'model_year', 'plate', 'value', 'photo'
    )
    search_fields = ('model', 'brand')
