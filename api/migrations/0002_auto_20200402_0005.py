# Generated by Django 3.0.5 on 2020-04-01 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='address',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='company',
            name='description',
            field=models.TextField(default=''),
        ),
    ]
