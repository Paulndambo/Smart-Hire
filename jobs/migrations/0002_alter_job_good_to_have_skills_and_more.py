# Generated by Django 4.1.1 on 2023-01-01 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='good_to_have_skills',
            field=models.JSONField(default=[]),
        ),
        migrations.AlterField(
            model_name='job',
            name='primary_skills',
            field=models.JSONField(default=[]),
        ),
        migrations.AlterField(
            model_name='job',
            name='secondary_skills',
            field=models.JSONField(default=[]),
        ),
    ]
