from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Count
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from accounts.models import Profile
from .filters import JobFilterr
from job.models import Job, Category
from job.filters import JobFilter


# Create your views here.


@login_required(login_url='login')
def index(request):
    profile=Profile.objects.get(user=request.user)
    profiles=Profile.objects.all()
    jobs=Job.objects.all()
    categories=Category.objects.all()
    # numOfJobs= Job.objects.filter(category=category).count
    # numOfJobs = Job.objects.annotate(total_jobs=Count('category'))
    numOfJobs = Job.objects.annotate(
        num_jobs=Count('category')
    )
    # category = get_object_or_404(Category)
    # joblistnum = jobs.filter(category=category)

    myfilterr = JobFilterr(request.GET, queryset=jobs)
    myfilter= JobFilter(request.GET, queryset=jobs)

    if myfilterr.is_valid():
        # myfilter = myfilterr
        jobs = myfilterr.qs
        # return render(request, 'home/home_job_list.html',{'jobs':jobs})


    context = {'profile':profile,
               'profiles':profiles,
               'categories':categories,
               'numOfJobs': numOfJobs,
               # 'joblistnum':joblistnum,
               # 'category':category,
               'jobs':jobs,
               'myfilterr':myfilterr,
               'myfilter':myfilter
               }
    return render(request,'home/home.html',context)

# @login_required(login_url='login')
# def SearchButton(request):
#     profile=Profile.objects.get(user=request.user)
#     jobs=Job.objects.all()
#     myfilter = JobFilterr(request.GET, queryset=jobs)
#     if myfilter.is_valid():
#         jobs = myfilter.qs
#     paginator = Paginator(jobs, 4)
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
#     context = {'profile':profile,
#                    'jobs':page_obj,
#                    'myfilter':myfilter,}
#     return render(request,'job/job_list.html',context)


def Filter_Job_category(request,category):
    profile = Profile.objects.get(user=request.user)
    jobs = Job.objects.filter(category=category)
    myfilter= JobFilter(request.GET, queryset=jobs)
    if myfilter.is_valid():
        jobs = myfilter.qs

    paginator = Paginator(jobs, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'jobs': page_obj,
        'profile': profile,
        'numOfJobs': jobs,
        'myfilter':myfilter,
    }
    return render(request, 'job/job_list.html', context)

