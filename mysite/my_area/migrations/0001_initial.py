# Generated by Django 5.1.2 on 2024-11-02 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Post",
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
                ("title", models.CharField(max_length=30, verbose_name="title")),
                (
                    "todayWord",
                    models.TextField(
                        blank=True, max_length=140, verbose_name="today word"
                    ),
                ),
                ("imgUrl", models.CharField(max_length=100, verbose_name="image url")),
            ],
        ),
    ]