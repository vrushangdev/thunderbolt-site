# Generated by Django 2.2.2 on 2019-06-15 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='replied',
            field=models.BooleanField(default=False),
        ),
    ]
