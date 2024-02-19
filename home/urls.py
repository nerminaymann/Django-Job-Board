from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index,name='home'),
    # path('', views.Filter_Job_category,name='home'),
    # path('jobs/', views.SearchButton, name='searchButton'),
    path('jobs/<str:category>/', views.Filter_Job_category, name='filter_job_category'),

]