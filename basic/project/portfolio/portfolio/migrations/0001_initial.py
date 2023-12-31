# Generated by Django 4.2.7 on 2023-12-31 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="About",
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
                ("name", models.CharField(max_length=500)),
                ("dob", models.CharField(max_length=500)),
                ("phone", models.CharField(max_length=500)),
                ("email", models.CharField(max_length=500)),
                ("no_exp", models.CharField(max_length=500)),
                ("no_happy_customers", models.CharField(max_length=500)),
                ("no_project_finished", models.CharField(max_length=500)),
                ("no_digital_awards", models.CharField(max_length=500)),
                ("description", models.TextField(max_length=5000)),
            ],
        ),
    ]
