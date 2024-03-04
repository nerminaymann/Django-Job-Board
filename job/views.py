from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.urls import reverse
from accounts.models import Profile
from .models import Job, Category
from .forms import ApplyForm,JobForm
from .filters import JobFilter
# Create your views here.

@login_required(login_url='login')
def Job_List(request):
    jobs= Job.objects.all()
    profile= Profile.objects.get(user=request.user)
    user_profile = Profile.objects.get(user=request.user)
    categories= Category.objects.all()

    #Filters
    myfilter = JobFilter(request.GET, queryset=jobs)
    if myfilter.is_valid():
        # myfilterr= myfilter
        jobs = myfilter.qs
    #SHOW 4 JOBS PER PAGE
    paginator=Paginator(jobs,4)
    page_number=request.GET.get('page')
    page_obj=paginator.get_page(page_number)

    context = {
        'jobs': page_obj,
        'profile': profile,
        'user_profile': user_profile,
        'categories': categories,
        'myfilter':myfilter,
               }
    return render(request,'job/job_list.html',context)

# @login_required(login_url='login')
# def Filter_Jobs(request,category):
#     jobs= Job.objects.filter(category__id=category)
#     profile= Profile.objects.get(user=request.user)
#     paginator = Paginator(jobs, 4)
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
#     context = {
#         'jobs': page_obj,
#         'profile': profile,
#     }
#     return render(request, 'job/job_list.html', context)

# def Job_Detail(request,id):
#     job = Job.objects.filter(id=id).first()
#
#     #job = Job.objects.get(id=id)
#     context = {'job': job}
#     return render(request, 'job/job_detail.html', context)

@login_required(login_url='login')
def Job_Detail(request,slug):
    profile= Profile.objects.get(user=request.user)
    user_profile = Profile.objects.get(user=request.user)
    job = Job.objects.filter(slug=slug).first()
    if request.method == 'POST':
        form = ApplyForm(request.POST,files=request.FILES)
        print("donee")
        if form.is_valid():
            my_form = form.save(commit=False)
            my_form.job=job
            my_form.user_id=request.user.id
            my_form.save()
            print("donee22")
    else:
        form = ApplyForm()
    context = {'job': job,'form':form,'profile':profile,'user_profile':user_profile }
    return render(request, 'job/job_detail.html', context)

@login_required(login_url='login')
def Post_Job(request):
    profile= Profile.objects.get(user=request.user)
    user_profile = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        form = JobForm(request.POST,files=request.FILES)

        if form.is_valid():
            my_form = form.save(commit=False)
            my_form.owner = request.user
            my_form.save()
            return redirect(reverse("Job_List"))
    else:
        form = JobForm()
    context = {'form':form,'profile':profile,'user_profile':user_profile }
    return render(request, 'job/post_job.html', context)
