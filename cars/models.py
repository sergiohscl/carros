from django.db import models


class Brand(models.Model):
    name = models.CharField(max_length=75)

    class Meta:
        db_table = 'Brand'
        verbose_name = 'Marca'
        verbose_name_plural = 'Marcas'

    def __str__(self) -> str:
        return self.name


class Car(models.Model):
    model = models.CharField(max_length=75)
    brand = models.ForeignKey(
        Brand, on_delete=models.PROTECT,
        related_name='car_brand'
    )
    factory_year = models.IntegerField(blank=True, null=True)
    model_year = models.IntegerField(blank=True, null=True)
    plate = models.CharField(max_length=10, blank=True, null=True)
    value = models.FloatField(blank=True, null=True)
    photo = models.ImageField(upload_to="cars/", blank=True, null=True)
    bio = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'car'
        verbose_name = 'Carro'
        verbose_name_plural = 'Carros'

    def __str__(self) -> str:
        return self.model


class CarInventory(models.Model):
    cars_count = models.IntegerField()
    cars_value = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'car_inventory'
        verbose_name = 'Inventário'
        verbose_name_plural = 'Inventário de Carros'
        ordering = ['-created_at']

    def __str__(self) -> str:
        return f'{self.cars_count} - {self.cars_value}'
