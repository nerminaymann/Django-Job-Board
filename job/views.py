from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.urls import reverse

from .models import Job
from .forms import ApplyForm,JobForm

# Create your views here.

def Job_List(request):
    jobs= Job.objects.all()

    #SHOW 4 JOBS PER PAGE
    paginator=Paginator(jobs,4)
    page_number=request.GET.get('page')
    page_obj=paginator.get_page(page_number)

    context = {
               'jobs':page_obj
               }
    return render(request,'job/job_list.html',context)

# def Job_Detail(request,id):
#     job = Job.objects.filter(id=id).first()
#
#     #job = Job.objects.get(id=id)
#     context = {'job': job}
#     return render(request, 'job/job_detail.html', context)

def Job_Detail(request,slug):
    job = Job.objects.filter(slug=slug).first()
    if request.method == 'POST':
        form = ApplyForm(request.POST,files=request.FILES)
        print("donee")
        if form.is_valid():
            my_form = form.save(commit=False)
            my_form.job=job
            my_form.save()
            print("donee22")
    else:
        form = ApplyForm()
    context = {'job': job,'form':form}
    return render(request, 'job/job_detail.html', context)

def Post_Job(request):
    if request.method == 'POST':
        form = JobForm(request.POST,files=request.FILES)

        if form.is_valid():
            my_form = form.save(commit=False)
            my_form.owner = request.user
            my_form.save()
            return redirect(reverse("Job_List"))
    else:
        form = JobForm()
    context = {'form':form}
    return render(request, 'job/post_job.html', context)
