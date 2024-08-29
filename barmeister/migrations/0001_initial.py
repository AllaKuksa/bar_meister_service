# Generated by Django 5.1 on 2024-08-29 14:30

import barmeister.models
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Ingredient",
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
                ("name", models.CharField(max_length=100, unique=True)),
                (
                    "unit",
                    models.CharField(
                        choices=[
                            ("grams", "G"),
                            ("milliliters", "Ml"),
                            ("slice", "Slice"),
                            ("piece", "Piece"),
                        ],
                        max_length=50,
                    ),
                ),
                ("quantity", models.DecimalField(decimal_places=0, max_digits=5)),
            ],
            options={
                "unique_together": {("name", "unit", "quantity")},
            },
        ),
        migrations.CreateModel(
            name="CocktailRecipe",
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
                ("name", models.CharField(max_length=100, unique=True)),
                ("description", models.TextField(blank=True, null=True)),
                (
                    "cocktail_type",
                    models.CharField(
                        choices=[
                            ("Low-Alcoholic", "Low Alcoholic"),
                            ("Non-Alcoholic", "Non Alcoholic"),
                            ("Strong", "Strong"),
                        ],
                        max_length=100,
                    ),
                ),
                ("quantity", models.PositiveIntegerField()),
                (
                    "taste",
                    models.CharField(
                        choices=[
                            ("Sweet", "Sweet"),
                            ("Sour", "Sour"),
                            ("Bitter", "Bitter"),
                            ("Salty", "Salty"),
                            ("Creamy", "Creamy"),
                        ],
                        max_length=100,
                    ),
                ),
                (
                    "cocktail_base",
                    models.CharField(
                        choices=[
                            ("Vodka", "Vodka"),
                            ("Brandy", "Brandy"),
                            ("Whiskey", "Whiskey"),
                            ("Gin", "Gin"),
                            ("Tequila", "Tequila"),
                            ("Rum", "Rum"),
                            ("Wine", "Wine"),
                            ("Sparkling Wine", "Sparkling Wine"),
                            ("Juice", "Juice"),
                        ],
                        max_length=100,
                    ),
                ),
                (
                    "group",
                    models.CharField(
                        choices=[
                            ("Long Drink", "Long Drink"),
                            ("Short Drink", "Short Drink"),
                            ("Shot", "Shot"),
                            ("Sour", "Sour"),
                            ("Classic", "Classic"),
                            ("Hot", "Hot"),
                        ],
                        max_length=100,
                    ),
                ),
                ("how_to_make", models.TextField()),
                ("preparation_time", models.IntegerField(help_text="Time in minutes")),
                (
                    "preparation_method",
                    models.CharField(
                        choices=[
                            ("Build", "Build"),
                            ("Shake", "Shake"),
                            ("Stir", "Stir"),
                            ("Blend", "Blend"),
                            ("Layer", "Layer"),
                            ("Heat", "Heat"),
                        ],
                        max_length=100,
                    ),
                ),
                (
                    "difficulty",
                    models.CharField(
                        choices=[
                            ("Easy", "Easy"),
                            ("Medium", "Medium"),
                            ("Hard", "Hard"),
                        ],
                        max_length=100,
                    ),
                ),
                (
                    "photo",
                    models.ImageField(
                        upload_to=barmeister.models.photo_cocktail_file_path
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(blank=True, null=True)),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                ("ingredients", models.ManyToManyField(to="barmeister.ingredient")),
            ],
        ),
    ]
