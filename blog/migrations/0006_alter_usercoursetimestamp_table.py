# Generated by Django 4.0.5 on 2022-09-04 20:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_usercoursetimestamp'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='usercoursetimestamp',
            table='timestamps',
        ),
    ]
