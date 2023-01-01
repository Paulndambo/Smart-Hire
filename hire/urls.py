from rest_framework.routers import DefaultRouter
from django.urls import path, include

from. import views

router = DefaultRouter()
router.register("candidate-profiles", views.CandidateProfileViewSet, basename="candidate-profiles")

urlpatterns = [
    path("", include(router.urls)),
]
