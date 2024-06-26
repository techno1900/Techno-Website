# Generated by Django 5.0.4 on 2024-04-28 09:32

import ckeditor.fields
import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                ("category_name", models.CharField(max_length=200, unique=True)),
                ("created", models.DateTimeField(auto_now_add=True)),
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "categories",
            },
        ),
        migrations.CreateModel(
            name="Post",
            fields=[
                ("title", models.CharField(max_length=200)),
                ("body", ckeditor.fields.RichTextField(blank=True, null=True)),
                (
                    "post_image",
                    models.ImageField(blank=True, null=True, upload_to="blog/"),
                ),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("video", models.CharField(blank=True, max_length=500, null=True)),
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                (
                    "category",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="blog.category",
                    ),
                ),
            ],
        ),
    ]
