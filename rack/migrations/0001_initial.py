# Generated by Django 3.1 on 2021-07-01 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rack',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rack_name', models.CharField(max_length=4, unique=True)),
                ('slug', models.SlugField(max_length=4, unique=True)),
                ('front_image', models.ImageField(upload_to='photos/front_rack')),
                ('back_image', models.ImageField(upload_to='photos/back_rack')),
            ],
        ),
    ]
