from django.urls import path
from .views import JobListAPI, JobCreateAPI, TestAPI

urlpatterns = [
    path('', TestAPI.as_view(), name='test-api'),             # Root API check
    path('jobs/', JobListAPI.as_view(), name='job-list'),     # GET all jobs
    path('jobs/create/', JobCreateAPI.as_view(), name='job-create'),  # POST job
]