# Generated by Django 3.1.1 on 2020-10-06 14:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_orderupdate'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orders',
            old_name='msg_id',
            new_name='order_id',
        ),
    ]
