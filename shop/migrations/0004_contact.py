# Generated by Django 3.1.1 on 2020-10-01 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20200929_1921'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('msg_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=70)),
                ('contact', models.CharField(max_length=20)),
                ('desc', models.CharField(max_length=300)),
            ],
        ),
    ]
