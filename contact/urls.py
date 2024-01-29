from django.urls import path, include
from . import views


urlpatterns = [
    path('send-messages', views.Send_Message,name='send_messages'),

]