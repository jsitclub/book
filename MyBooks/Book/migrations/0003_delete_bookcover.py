# Generated by Django 2.2.4 on 2020-07-06 04:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Book', '0002_auto_20200706_1317'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BookCover',
        ),
    ]
