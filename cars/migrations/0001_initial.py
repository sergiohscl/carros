# Generated by Django 5.0.3 on 2024-03-30 14:02

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Car",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("model", models.CharField(max_length=75)),
                ("brand", models.CharField(max_length=75)),
                ("factory_year", models.IntegerField(blank=True, null=True)),
                ("model_year", models.IntegerField(blank=True, null=True)),
                ("value", models.FloatField(blank=True, null=True)),
            ],
            options={
                "verbose_name": "Carro",
                "verbose_name_plural": "Carros",
                "db_table": "car",
            },
        ),
    ]
