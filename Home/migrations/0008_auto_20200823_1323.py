# Generated by Django 3.1 on 2020-08-23 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0007_auto_20200823_1320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='photo',
            field=models.ImageField(upload_to='media'),
        ),
    ]
