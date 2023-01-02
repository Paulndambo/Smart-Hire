from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.

SPECIALTY_CHOICES = (
    ("backend", "Backend Developer"),
    ("frontend", "Frontend Developer"),
    ("fullstack", "Fullstack Developer"),
    ("product", "Product Developer/Engineer"),
    ("database", "Database Engineer/Developer/Administrator"),
    ("devops", "DevOps Engineer"),
    ("cloud", "Cloud Engineer/Architect/Developer"),
    ("designer", "Product Designer/Web Designer"),
    ("android", "Android App Developer"),
    ("ios", "iOS App Developer"),
    ("cross_platform", "Cross Platform App Developer"),
)

PROFESSIONAL_TITLE_CHOICES = (
    ("developer", "Software Developer/Engineer"),
    ("designer", "Product Designer/Web Designer"),
)

SENIORITY_CHOICES = (
    ("junior", "Junior/Entry Level"),
    ("mid_level", "Mid-Level"),
    ("senior", "Senior"),
    ("principal", "Principal"),
)
class Candidate(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255, null=True, blank=True)
    zip_code = models.CharField(max_length=255, null=True, blank=True)
    country = models.CharField(max_length=255, null=True, blank=True)
    photo = models.ImageField(upload_to="profile_photos/", null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    professional_summary = models.TextField(null=True, blank=True)
    seniority = models.CharField(max_length=255, choices=SENIORITY_CHOICES, null=True, blank=True)
    professional_title = models.CharField(max_length=255, choices=PROFESSIONAL_TITLE_CHOICES, null=True)
    specialty = models.CharField(max_length=255, null=True, blank=True, choices=SPECIALTY_CHOICES)
    years_of_experience = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name + " " + self.last_name


GRADUATION_STATUS_CHOICES = (
    ("graduated", "Graduated"),
    ("not_graduated", "Not Graduated"),
    ("continuing", "Continuing"),
)

DEGREE_STATUS_CHOICES = (
    ("completed", "Completed"),
    ("not_completed", "Not Completed"),
    ("started", "Started"),
    ("not_started", "Not Started"),
)



class Education(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE, related_name="education")
    school = models.CharField(max_length=255)
    degree = models.CharField(max_length=255, null=True, blank=True)
    major = models.CharField(max_length=255, null=True, blank=True)
    degree_status = models.CharField(max_length=255, choices=DEGREE_STATUS_CHOICES, null=True, blank=True)
    major_status = models.CharField(max_length=255, null=True, blank=True)
    date_joined = models.DateField(null=True, blank=True)
    graduation_date = models.DateField(null=True, blank=True)
    graduation_status = models.CharField(max_length=255, choices=GRADUATION_STATUS_CHOICES, null=True, blank=True)
    certificate = models.FileField(upload_to="education_certificates/", null=True, blank=True)
    years_of_experience = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.candidate.first_name + " " + self.candidate.last_name 


SKILL_CATEGORY_CHOICES = (
    ("primary", "Primary Skills"),
    ("secondary", "Secondary Skills"),
)

class Skill(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE, related_name="skills")
    title = models.CharField(max_length=255)
    years_of_experience = models.FloatField(default=0)
    years_of_profession_experience = models.FloatField(default=0)
    skill_category = models.CharField(max_length=255, choices=SKILL_CATEGORY_CHOICES, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.candidate.first_name 


class Experience(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE, related_name="experiences")
    employer = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    skills = models.JSONField(default=[])
    relevant_skills = models.ManyToManyField(Skill)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.candidate.first_name + " " + self.candidate.last_name 



#class Job(models.Model):
#    passe