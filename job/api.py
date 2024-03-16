from urllib import response

from rest_framework import viewsets, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Job
from .serializers import JobSerializer

@api_view(['GET'])
def get_jobs(request):
    jobs= Job.objects.all()
    data = JobSerializer(jobs, many=True).data
    return Response({'data':data,'status':'success'})

@api_view(['GET'])
def get_job_detail(request,job_id):
    job = Job.objects.get(id=job_id)
    data = JobSerializer(job).data
    return Response({'data':data,'status':'success'})

#_______________________CLASS BASED VIEWS_____________________


#VEIW_SETS

# class JobViewSet(viewsets.ModelViewSet):
#     queryset = Job.objects.all()
#     serializer_class = JobSerializer

class JobList(generics.ListCreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

class JobDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    lookup_field = 'id'






