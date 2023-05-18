# Generated by Django 4.1.3 on 2023-05-18 14:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('musicApp', '0008_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='song',
        ),
        migrations.AddField(
            model_name='song',
            name='comments',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='musicApp.comment'),
        ),
    ]
