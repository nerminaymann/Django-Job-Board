from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.Job_List,name='Job_List'),
    path('post-job/', views.Post_Job, name='post_job'),
    path('<str:slug>', views.Job_Detail,name='job_detail'),
]