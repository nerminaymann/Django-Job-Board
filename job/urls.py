from django.urls import path, include
from . import views
from . import api


urlpatterns = [
    path('', views.Job_List,name='Job_List'),
    path('post-job/', views.Post_Job, name='post_job'),
    path('<str:slug>', views.Job_Detail,name='job_detail'),

    #API
    path('api/jobs/', api.get_jobs,name='get_jobs-api'),
    path('api/job/<int:job_id>', api.get_job_detail, name='get_job-detail_api'),

    #CLASS_BASED_VIEWS_generics
    path('api/v2/jobs/',api.JobList.as_view(),name='job-list-api'),
    path('api/v2/job/<int:id>', api.JobDetail.as_view(), name='get_job-detail_api'),
    # path('api/v3/jobs/',api.JobViewSet.as_view),

]