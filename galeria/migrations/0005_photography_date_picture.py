# Generated by Django 4.1 on 2023-04-21 01:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("galeria", "0004_photography_published"),
    ]

    operations = [
        migrations.AddField(
            model_name="photography",
            name="date_picture",
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]