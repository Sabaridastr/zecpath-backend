from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import JobSerializer
from services.job_service import get_all_jobs, create_job


class JobListAPI(APIView):
    def get(self, request):
        jobs = get_all_jobs()
        serializer = JobSerializer(jobs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class JobCreateAPI(APIView):
    def post(self, request):
        serializer = JobSerializer(data=request.data)

        if serializer.is_valid():
            job = create_job(serializer.validated_data)
            return Response(JobSerializer(job).data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TestAPI(APIView):
    def get(self, request):
        return Response(
            {
                "message": "API working",
                "status": "success"
            },
            status=status.HTTP_200_OK
        )