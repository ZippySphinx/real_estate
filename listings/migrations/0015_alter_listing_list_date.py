# Generated by Django 3.2.4 on 2021-07-03 07:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0014_alter_listing_list_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='list_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 7, 3, 12, 58, 58, 450573)),
        ),
    ]
