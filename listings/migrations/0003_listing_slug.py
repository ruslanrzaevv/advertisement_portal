# Generated by Django 5.0.6 on 2024-07-13 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0002_category_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='slug',
            field=models.SlugField(default=None, null=True),
        ),
    ]