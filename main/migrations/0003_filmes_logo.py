# Generated by Django 4.0.4 on 2022-05-17 17:39

from django.db import migrations, models
import main.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_filmes_banner'),
    ]

    operations = [
        migrations.AddField(
            model_name='filmes',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to=main.models.upload_image_logo),
        ),
    ]
