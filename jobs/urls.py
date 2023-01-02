from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .import views

router = DefaultRouter()
router.register("employers", views.EmployeeModelViewSet, basename="employers")
router.register("jobs", views.JobModelViewSet, basename="jobs")

urlpatterns = [ 
    path("", include(router.urls)),
]