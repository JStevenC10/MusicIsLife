# Generated by Django 4.1.3 on 2023-01-12 20:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('musicApp', '0002_rename_listen_song_link'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='link',
        ),
        migrations.AddField(
            model_name='song',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
