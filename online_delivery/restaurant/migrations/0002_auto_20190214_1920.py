# Generated by Django 2.1.5 on 2019-02-14 13:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='restaurant',
            old_name='town',
            new_name='place',
        ),
    ]
