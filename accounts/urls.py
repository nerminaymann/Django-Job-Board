from django.urls import path, include
from . import views


urlpatterns = [
    path('signup/', views.SignUp,name='signup'),
    # path('login/', views.login,name='login'),
    path('profile/', views.Get_Profile, name='profile'),
    path('update_profile/', views.Update_Profile, name='update_profile'),
]