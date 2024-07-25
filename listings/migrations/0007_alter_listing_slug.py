# Generated by Django 5.0.7 on 2024-07-15 13:44

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0006_alter_category_slug_alter_listing_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, null=True, populate_from='title', unique=True),
        ),
    ]
