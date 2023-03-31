# Generated by Django 4.1.3 on 2023-03-31 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicApp', '0005_alter_song_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='gender',
            field=models.CharField(choices=[('RAP', 'rap'), ('ROCK', 'rock'), ('REGAETTON', 'regaeton'), ('REGGUE', 'reggue'), ('BALADAS', 'baladas'), ('SALSA', 'salsa'), ('SALSA-CHOKE', 'salsa-choke'), ('BACHATA', 'bachata'), ('COUNTRY', 'country')], default='RAP', max_length=50),
        ),
    ]
