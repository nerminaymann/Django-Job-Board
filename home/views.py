from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render
from django.http import HttpResponse
from accounts.models import Profile
from .filters import JobFilterr
from job.models import Job, Category
from job.filters import JobFilter


# Create your views here.


@login_required(login_url='login')
def index(request):
    profile=Profile.objects.get(user=request.user)
    jobs=Job.objects.all()
    categories=Category.objects.all()

    myfilterr = JobFilterr(request.GET, queryset=jobs)
    myfilter= JobFilter(request.GET, queryset=jobs)

    if myfilterr.is_valid():
        myfilter = myfilterr
        jobs = myfilterr.qs
        # return render(request, 'home/home_job_list.html',{'jobs':jobs})


    context = {'profile':profile,
               'categories':categories,
               'jobs':jobs,
               'myfilterr':myfilterr,
               'myfilter':myfilter}
    return render(request,'home/home.html',context)

