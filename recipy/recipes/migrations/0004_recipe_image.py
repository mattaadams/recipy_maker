# Generated by Django 4.0.4 on 2022-06-10 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0003_alter_comment_recipe'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='recipe_pics'),
        ),
    ]