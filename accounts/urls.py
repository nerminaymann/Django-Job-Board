from django.urls import path, include
from . import views


urlpatterns = [
    path('signup/', views.SignUp,name='signup'),
    # path('login/', views.login,name='login'),
    # path('logout/', views.logout,name='logout'),
    path('profile/', views.Get_Profile, name='profile'),
    path('profile/<str:profile>', views.Get_Others_Profile, name='others_profile'),
    path('update_profile/', views.Update_Profile, name='update_profile'),
]