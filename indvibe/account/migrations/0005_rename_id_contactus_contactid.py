# Generated by Django 4.1.4 on 2023-05-09 15:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_alter_contactus_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactus',
            old_name='id',
            new_name='contactid',
        ),
    ]
