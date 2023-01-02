from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status, generics
from jobs.serializers import JobSerializer, EmployerSerializer
from jobs.models import Job, Employer
from rest_framework.viewsets import ModelViewSet
# Create your views here.
class EmployeeModelViewSet(ModelViewSet):
    queryset = Employer.objects.all()
    serializer_class = EmployerSerializer


class JobModelViewSet(ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer