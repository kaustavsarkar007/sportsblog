# Generated by Django 4.1.1 on 2022-12-12 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cricket', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cricpost',
            name='timestamp',
            field=models.DateTimeField(blank=True),
        ),
    ]
