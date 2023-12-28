from django.shortcuts import render
from .models import Job

# Create your views here.

def Job_List(request):
    jobs= Job.objects.all()
    context = {'jobs':jobs}
    return render(request,'job/job_list.html',context)



def Job_Detail(request,id):
    job = Job.objects.filter(id=id).first()
    context = {'job': job}
    return render(request, 'job/job_detail.html', context)
