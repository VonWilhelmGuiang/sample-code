# Generated by Django 4.2.4 on 2023-08-23 16:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Polls',
            new_name='Votes',
        ),
    ]
