# Generated by Django 4.2.6 on 2023-10-30 04:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='list',
            old_name='owner',
            new_name='Usuario',
        ),
    ]
