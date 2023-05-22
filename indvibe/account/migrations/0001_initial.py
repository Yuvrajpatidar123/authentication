# Generated by Django 4.1.4 on 2023-05-09 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contactus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=55)),
                ('email', models.EmailField(max_length=25)),
                ('mobile', models.CharField(max_length=15)),
                ('desc', models.CharField(max_length=1000)),
            ],
        ),
    ]
