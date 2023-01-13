from django.shortcuts import render, get_object_or_404
from hire.models import Candidate, Education, Skill, Experience
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from jobs.models import Job

from .job_matching_functions import job_matching_candidate
from .candidates_matching_job import candidates_matching_job

from hire.serializers import CandidateSerializer, CandidateProfileSerializer, EducationSerializer, SkillSerializer, ExperienceSerializer, JobsMatchingCandidateSerializer
# Create your views here.
class CandidateProfileViewSet(ModelViewSet):
    queryset = Candidate.objects.all()
    serializer_class = CandidateProfileSerializer

    http_method_names = ["get", "GET"]


class CandidateModelViewSet(ModelViewSet):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer


class EducationViewSet(ModelViewSet):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer


class SkillViewSet(ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer


class ExperienceViewSet(ModelViewSet):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer


class JobsMatchingCandidateAPIView(generics.GenericAPIView):
    queryset = Job.objects.all()
    serializer_class = JobsMatchingCandidateSerializer

    def get(self, request, *args, **kwargs):
        candidate_pk = request.query_params.get("candidate_id")
        #email = request.GET.get("email")
        if candidate_pk:
            candidate = get_object_or_404(Candidate, pk=candidate_pk)

            """
            => If the candidate exists, filter jobs
            """
            if candidate is None:
                return Response({"failed": f"No candidate with id: {candidate_pk}"}, status=status.HTTP_404_NOT_FOUND)
            print(candidate)
            #queryset = job_matching_based_on_experience(candidate)
            queryset = self.queryset.filter(
                id__in=job_matching_candidate(candidate))
            serializer = JobsMatchingCandidateSerializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"success": "No jobs match for you"}, status=status.HTTP_200_OK)


class CandidatesMatchingJobAPIView(generics.GenericAPIView):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer

    def get(self, request, *args, **kwargs):
        job_id = request.query_params.get("job_id")

        if job_id:
            job = get_object_or_404(Job, pk=job_id)
            if job:
                candidates = self.queryset.filter(id__in=candidates_matching_job(job))

                print(f"Matching Candidates: {candidates}")

                serialiazer = CandidateSerializer(candidates, many=True)
                return Response(serialiazer.data, status=status.HTTP_200_OK)
        #serialiazer = self.serializer_class(instance=self.get_queryset(), many=True)
        return Response({"message": "No Candidates Matching This Job!"}, status=status.HTTP_200_OK)


