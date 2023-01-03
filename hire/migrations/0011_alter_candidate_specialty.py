# Generated by Django 4.1.1 on 2023-01-02 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hire', '0010_alter_experience_skills'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='specialty',
            field=models.CharField(blank=True, choices=[('backend', 'Backend Developer'), ('frontend', 'Frontend Developer'), ('fullstack', 'Fullstack Developer'), ('product', 'Product Developer/Engineer'), ('database', 'Database Engineer/Developer/Administrator'), ('devops', 'DevOps Engineer'), ('cloud', 'Cloud Engineer/Architect/Developer'), ('designer', 'Product Designer/Web Designer'), ('android', 'Android App Developer'), ('ios', 'iOS App Developer'), ('cross_platform_app', 'Cross Platform App Developer')], max_length=255, null=True),
        ),
    ]
