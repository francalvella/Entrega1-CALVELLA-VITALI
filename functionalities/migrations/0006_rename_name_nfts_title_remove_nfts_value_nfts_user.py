# Generated by Django 4.0.3 on 2022-04-17 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('functionalities', '0005_nfts_smart_contracts'),
    ]

    operations = [
        migrations.RenameField(
            model_name='nfts',
            old_name='name',
            new_name='title',
        ),
        migrations.RemoveField(
            model_name='nfts',
            name='value',
        ),
        migrations.AddField(
            model_name='nfts',
            name='user',
            field=models.CharField(default='unknown', max_length=15),
        ),
    ]
