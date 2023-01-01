# Generated by Django 4.1.1 on 2023-01-01 20:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Employer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
                ('phone', models.CharField(max_length=255)),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('city', models.CharField(max_length=255)),
                ('state', models.CharField(blank=True, max_length=255, null=True)),
                ('zipcode', models.CharField(blank=True, max_length=255, null=True)),
                ('country', models.CharField(max_length=255)),
                ('established', models.DateField(blank=True, null=True)),
                ('ownership_type', models.CharField(choices=[('public', 'Public'), ('private', 'Private')], max_length=255)),
                ('employees_range', models.CharField(choices=[('0-10', '0-10'), ('10-100', '10-100'), ('100-1000', '100-1000'), ('1000+', '1000+')], max_length=255)),
                ('industry', models.CharField(blank=True, max_length=255, null=True, verbose_name='e.g Fintech')),
                ('website', models.CharField(blank=True, max_length=255, null=True)),
                ('twitter', models.CharField(blank=True, max_length=255, null=True)),
                ('facebook', models.CharField(blank=True, max_length=255, null=True)),
                ('instagram', models.CharField(blank=True, max_length=255, null=True)),
                ('linkedin', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('salary_range', models.CharField(blank=True, max_length=255, null=True)),
                ('location', models.CharField(blank=True, max_length=255, null=True)),
                ('work_type', models.CharField(blank=True, choices=[('full_time', 'Full Time'), ('part_time', 'Part Time'), ('contract', 'Contract'), ('internship', 'Internship')], max_length=255, null=True)),
                ('work_place_type', models.CharField(blank=True, choices=[('remote', 'Remote'), ('on_site', 'On Site'), ('hybrid', 'Hybrid')], max_length=255, null=True)),
                ('mininum_experience', models.FloatField(default=0)),
                ('maximum_experience', models.FloatField(blank=True, null=True)),
                ('primary_skills', models.JSONField(default={})),
                ('secondary_skills', models.JSONField(default={})),
                ('good_to_have_skills', models.JSONField(default={})),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('employer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jobs', to='jobs.employer')),
            ],
        ),
    ]
