from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


@login_required(login_url='login')
def index(request):
    return HttpResponse("<h1>Welcome to the home page<h1>")