# Generated by Django 3.1.1 on 2020-09-25 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=30)),
                ('product_dec', models.CharField(max_length=300)),
                ('publish_date', models.DateTimeField()),
            ],
        ),
    ]
