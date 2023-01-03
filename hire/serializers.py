from rest_framework import serializers
from .models import Candidate, Education, Skill, Experience
from jobs.models import Job


class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = "__all__"


class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = "__all__"


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = "__all__"


class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = "__all__"


class CandidateProfileSerializer(serializers.ModelSerializer):
    skills = serializers.SerializerMethodField()
    experiences = serializers.SerializerMethodField()
    education = serializers.SerializerMethodField()
    
    class Meta:
        model = Candidate
        fields = "__all__"

    def get_skills(self, obj):
        return obj.skills.values()

    def get_experiences(self, obj):
        return obj.experiences.values()

    def get_education(self, obj):
        return obj.education.values()


class JobsMatchingCandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = "__all__"