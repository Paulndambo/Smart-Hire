from rest_framework.routers import DefaultRouter
from django.urls import path, include

from. import views

router = DefaultRouter()
router.register("candidate-profiles", views.CandidateProfileViewSet, basename="candidate-profiles")
router.register("candidates", views.CandidateModelViewSet, basename="candidates")
router.register("education", views.EducationViewSet, basename="education")
router.register("skills", views.SkillViewSet, basename="skills")
router.register("experience", views.ExperienceViewSet, basename="experience")
#router.register("jobs-matching-candidate", views.JobsMatchingCandidateViewSet, basename="jobs-matching-candidate")

urlpatterns = [
    path("", include(router.urls)),
    path("jobs-matching-candidate/", views.JobsMatchingCandidateAPIView.as_view(), name="jobs-matching-candidate"),
    path("candidates-matching-job/", views.CandidatesMatchingJobAPIView.as_view(), name="candidates-matching-job"),
]
