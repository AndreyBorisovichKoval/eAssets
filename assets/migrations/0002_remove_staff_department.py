# Generated by Django 5.0.2 on 2024-02-16 05:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='staff',
            name='department',
        ),
    ]