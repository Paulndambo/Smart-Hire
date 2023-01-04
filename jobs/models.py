from django.db import models
from django.contrib.auth.models import User
# Create your models here.
OWNERSHIP_TYPE = (
    ("public", "Public"),
    ("private", "Private"),
)

EMPLOYEES_RANGE = (
    ("0-10", "0-10"),
    ("10-100", "10-100"),
    ("100-1000", "100-1000"),
    ("1000+", "1000+"),
)


class Employer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=255)
    address = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255, null=True, blank=True)
    zipcode = models.CharField(max_length=255, null=True, blank=True)
    country = models.CharField(max_length=255)
    established = models.DateField(null=True, blank=True)
    ownership_type = models.CharField(max_length=255, choices=OWNERSHIP_TYPE)
    employees_range = models.CharField(max_length=255, choices=EMPLOYEES_RANGE)
    industry = models.CharField(max_length=255, null=True, blank=True, verbose_name='e.g Fintech')
    website = models.CharField(max_length=255, null=True, blank=True)
    twitter = models.CharField(max_length=255, null=True, blank=True)
    facebook = models.CharField(max_length=255, null=True, blank=True)
    instagram = models.CharField(max_length=255, null=True, blank=True)
    linkedin = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


WORK_TYPE_CHOICES = (
    ("full_time", "Full Time"),
    ("part_time", "Part Time"),
    ("contract", "Contract"),
    ("internship", "Internship")
)

WORK_PLACE_TYPE = (
    ("remote", "Remote"),
    ("on_site", "On Site"),
    ("hybrid", "Hybrid"),
)

SENIORITY_CHOICES = (
    ("entry_level", "Entry Level"),
    ("mid_level", "Mid Level"),
    ("senior", "Senior")
)

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
    ("cross_platform_app", "Cross Platform App Developer"),
)

class Job(models.Model):
    employer = models.ForeignKey(Employer, on_delete=models.CASCADE, related_name="jobs")
    title = models.CharField(max_length=255)
    description = models.TextField()
    salary_range = models.CharField(max_length=255, null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    work_type = models.CharField(max_length=255, choices=WORK_TYPE_CHOICES, null=True, blank=True)
    work_place_type = models.CharField(max_length=255, choices=WORK_PLACE_TYPE, null=True, blank=True)
    minimum_experience = models.FloatField(default=0)
    maximum_experience = models.FloatField(null=True, blank=True)
    primary_skills = models.JSONField(null=True, blank=True) # {"name": "Python", "years": 3}
    secondary_skills = models.JSONField(null=True, blank=True)  # {"name": "Java", "years": 3}
    good_to_have_skills = models.JSONField(null=True, blank=True)  # {"name": "Python", "years": 3}
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    category = models.CharField(max_length=255, null=True, blank=True, choices=SPECIALTY_CHOICES)
    seniority = models.CharField(max_length=255, choices=SENIORITY_CHOICES, null=True, blank=True)
    
    def __str__(self):
        return self.title