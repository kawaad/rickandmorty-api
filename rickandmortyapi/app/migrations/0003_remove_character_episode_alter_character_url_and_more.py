# Generated by Django 5.0.6 on 2024-06-13 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_episode_characters_location_residents_fields'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='character',
            name='episode',
        ),
        migrations.AlterField(
            model_name='character',
            name='url',
            field=models.URLField(blank=True, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='episode',
            name='url',
            field=models.URLField(blank=True, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='url',
            field=models.URLField(blank=True, null=True, unique=True),
        ),
    ]
