# Generated by Django 4.0.3 on 2022-04-16 23:57

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('functionalities', '0004_coin_info'),
    ]

    operations = [
        migrations.CreateModel(
            name='NFTs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('value', models.FloatField()),
                ('info', ckeditor.fields.RichTextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Smart_contracts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('case', models.CharField(max_length=15)),
                ('info', ckeditor.fields.RichTextField(blank=True, null=True)),
            ],
        ),
    ]
