# Generated by Django 4.1.3 on 2022-12-09 00:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('musicApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='song',
            old_name='listen',
            new_name='link',
        ),
    ]
