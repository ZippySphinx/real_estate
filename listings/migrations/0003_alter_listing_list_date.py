# Generated by Django 3.2.4 on 2021-07-01 15:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0002_alter_listing_list_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='list_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 7, 1, 21, 11, 53, 367800)),
        ),
    ]
