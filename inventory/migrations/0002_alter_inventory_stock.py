# Generated by Django 4.1.3 on 2022-11-22 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='stock',
            field=models.IntegerField(default=0),
        ),
    ]
