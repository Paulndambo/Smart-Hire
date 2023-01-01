from rest_framework import serializers
from .models import Candidate, Education, Skill, Experience


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
    class Meta:
        model = Candidate
        fields = "__all__"

