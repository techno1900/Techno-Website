# Generated by Django 5.0.4 on 2024-04-28 12:27

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("services", "0002_remove_packagecontent_package"),
    ]

    operations = [
        migrations.AddField(
            model_name="package",
            name="package_title",
            field=models.ManyToManyField(blank=True, to="services.packagecontent"),
        ),
    ]
