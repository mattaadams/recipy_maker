# Generated by Django 4.0.4 on 2022-06-10 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0006_alter_recipe_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='image',
            field=models.ImageField(default='default_food.png', upload_to='recipe_pics'),
        ),
    ]
