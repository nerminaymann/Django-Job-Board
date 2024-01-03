from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.Job_List),
    path('<str:slug>', views.Job_Detail,name='job_detail'),
]