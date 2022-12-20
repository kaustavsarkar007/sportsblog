# Generated by Django 4.1.1 on 2022-12-12 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CricPost',
            fields=[
                ('slug', models.CharField(max_length=50)),
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.TextField(max_length=120)),
                ('author', models.CharField(max_length=50)),
                ('content', models.TextField()),
                ('timestamp', models.DateField(blank=True)),
            ],
        ),
    ]
