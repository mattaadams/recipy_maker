# Generated by Django 4.1 on 2022-08-31 04:01

from django.db import migrations, models
import users.validators


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='profile_pics', validators=[users.validators.validate_file_extension, users.validators.file_size]),
        ),
    ]
