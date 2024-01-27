from django.contrib import auth
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, ProfileForm, UserForm
from .models import Profile

# Create your views here.


#---------------------------AUTHENTICATION--------------------------
def SignUp(request):
        if request.method == 'POST':
            form = SignUpForm(request.POST)
            if form.is_valid():
                form.save()

                #select the username from the form
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password1')
                user_login= auth.authenticate(username=username, password=password)
                auth.login(request, user_login)
                #it will go to PORIFLE PAGE not HOME
                return redirect('profile')
        else:
            form = SignUpForm()
        context = {'form': form}
        return render(request, 'registration/signup.html', context)

# def login(request):
#     if request.method == 'POST':
#          form = SignInForm(request.POST)
#          if form.is_valid():
#              form.save()
#              username = form.cleaned_data.get('username')
#              password = form.cleaned_data.get('password')
#              user=auth.authenticate(username=username,password=password)
#              if user is not None:
#                  auth.login(request,user)
#                  return redirect('profile/<username>')
#              else:
#                  return redirect('login')
#     else:
#         form = SignInForm()
#     context = {'form': form}
#     return render(request,'registration/login.html',context)

# ---------------------------PROFILE PAGE--------------------------

def Get_Profile(request):
    #to return the current user who's log in the website
    profile = Profile.objects.get(user=request.user)
    return render(request,'accounts/profile.html',{'profile': profile})

def Update_Profile(request):
    profile = Profile.objects.get(user=request.user)
    # user_profile = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, files=request.FILES,instance=profile)

        if profile_form.is_valid() and user_form.is_valid():
            user_form.save()
            myProfile_form = profile_form.save(commit=False)
            myProfile_form.user = request.user
            myProfile_form.save()
            return redirect("profile")
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=profile)


    context = {'profile_form': profile_form, 'user_form': user_form}
    return render(request, 'accounts/update_profile.html', context)

