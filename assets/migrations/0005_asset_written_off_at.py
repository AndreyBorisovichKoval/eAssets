# Generated by Django 5.0.2 on 2024-02-25 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0004_alter_useraction_action'),
    ]

    operations = [
        migrations.AddField(
            model_name='asset',
            name='written_off_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]