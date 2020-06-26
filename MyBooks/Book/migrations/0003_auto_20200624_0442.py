# Generated by Django 2.2.4 on 2020-06-24 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Book', '0002_auto_20200624_0428'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='datetime',
        ),
        migrations.AddField(
            model_name='book',
            name='created',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='modified',
            field=models.DateTimeField(null=True),
        ),
    ]
