# Generated by Django 2.1 on 2018-09-06 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='maplist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mapName', models.CharField(max_length=60)),
                ('mapDesc', models.TextField()),
                ('mapLat', models.CharField(max_length=20)),
                ('mapLng', models.CharField(max_length=20)),
                ('mapTel', models.CharField(max_length=20)),
                ('mapAddr', models.CharField(max_length=60)),
            ],
        ),
    ]
