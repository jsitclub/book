# Generated by Django 2.2.4 on 2020-06-24 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('author', models.CharField(max_length=50)),
                ('translator', models.CharField(blank=True, default='', max_length=50)),
                ('isbn', models.CharField(blank=True, default='', max_length=13)),
                ('page', models.IntegerField(default=0, null=True)),
                ('publisher', models.CharField(blank=True, default='', max_length=50)),
                ('publishdate', models.DateField(blank=True)),
                ('datetime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]