# Generated by Django 3.1 on 2020-08-22 07:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('experience', models.DecimalField(decimal_places=2, max_digits=4)),
                ('photo', models.ImageField(upload_to='teachers')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Home.location')),
            ],
        ),
    ]
