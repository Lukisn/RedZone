# Generated by Django 2.0.3 on 2018-03-09 10:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0006_auto_20180309_0940'),
    ]

    operations = [
        migrations.RenameField(
            model_name='membership',
            old_name='date_left',
            new_name='date_released',
        ),
    ]
