# Generated by Django 3.2.5 on 2021-11-23 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cloud_storage', '0002_auto_20211123_1333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storage',
            name='Image',
            field=models.ImageField(upload_to='pics'),
        ),
    ]