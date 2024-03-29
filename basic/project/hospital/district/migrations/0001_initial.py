# Generated by Django 4.2 on 2024-02-01 17:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("division", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Districts",
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
                ("name", models.CharField(max_length=400)),
                (
                    "div_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="division.divisions",
                    ),
                ),
            ],
        ),
    ]
