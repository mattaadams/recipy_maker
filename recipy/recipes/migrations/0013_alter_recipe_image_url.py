# Generated by Django 4.0.4 on 2022-06-19 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0012_recipe_favorites'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='image_url',
            field=models.URLField(blank=True, max_length=300, null=True),
        ),
    ]