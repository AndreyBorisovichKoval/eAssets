# Generated by Django 5.0.2 on 2024-02-13 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='asset',
            name='description',
            field=models.TextField(null=True),
        ),
    ]