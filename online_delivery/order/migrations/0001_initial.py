# Generated by Django 2.1.5 on 2019-02-14 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customer', '0001_initial'),
        ('restaurant', '0002_auto_20190214_1920'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bill_amount', models.IntegerField()),
                ('address', models.TextField()),
                ('city', models.CharField(max_length=50)),
                ('pincode', models.IntegerField(max_length=6)),
                ('c_id', models.ForeignKey(on_delete='DO_NOTHING', to='customer.Customer')),
                ('r_id', models.ForeignKey(on_delete='DO_NOTHING', to='restaurant.Restaurant')),
            ],
        ),
    ]
