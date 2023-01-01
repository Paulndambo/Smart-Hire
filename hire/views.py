from django.shortcuts import render
from hire.models import Candidate, Education, Skill, Experience
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from hire.serializers import CandidateSerializer, CandidateProfileSerializer, EducationSerializer, SkillSerializer, ExperienceSerializer
# Create your views here.
class CandidateProfileViewSet(ModelViewSet):
    queryset = Candidate.objects.all()
    serializer_class = CandidateProfileSerializer

    http_method_names = ["get", "GET"]
