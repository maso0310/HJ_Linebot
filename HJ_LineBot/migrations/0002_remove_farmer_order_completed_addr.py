# Generated by Django 3.0.3 on 2020-02-07 12:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HJ_LineBot', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='farmer_order_completed',
            name='addr',
        ),
    ]