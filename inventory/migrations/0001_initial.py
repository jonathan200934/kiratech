# Generated by Django 4.1.3 on 2022-11-22 09:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=500)),
                ('note', models.TextField(blank=True)),
                ('stock', models.IntegerField()),
                ('availability', models.BooleanField()),
                ('supply', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='inventory.supplier')),
            ],
        ),
    ]
