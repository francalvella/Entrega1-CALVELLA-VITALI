# Generated by Django 4.0.3 on 2022-04-26 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_user_extension_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_extension',
            name='avatar',
            field=models.ImageField(blank=True, default='avatars/image_6483441_bmK2Skm.JPG', null=True, upload_to='avatars'),
        ),
    ]
