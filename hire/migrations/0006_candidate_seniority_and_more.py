# Generated by Django 4.1.1 on 2023-01-02 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hire', '0005_candidate_specialty'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='seniority',
            field=models.CharField(blank=True, choices=[('junior', 'Junior/Entry Level'), ('mid_level', 'Mid-Level'), ('senior', 'Senior'), ('principal', 'Principal')], max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='professional_title',
            field=models.CharField(choices=[('developer', 'Software Developer/Engineer'), ('designer', 'Product Designer/Web Designer')], max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='specialty',
            field=models.CharField(blank=True, choices=[('backend', 'Backend Developer'), ('frontend', 'Frontend Developer'), ('fullstack', 'Fullstack Developer'), ('product', 'Product Developer/Engineer'), ('database', 'Database Engineer/Developer/Administrator'), ('devops', 'DevOps Engineer'), ('cloud', 'Cloud Engineer/Architect/Developer'), ('designer', 'Product Designer/Web Designer'), ('android', 'Android App Developer'), ('ios', 'iOS App Developer'), ('cross_platform', 'Cross Platform App Developer')], max_length=255, null=True),
        ),
    ]