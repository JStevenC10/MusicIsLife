# Generated by Django 4.1.3 on 2023-01-31 02:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicApp', '0003_remove_song_link_song_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
