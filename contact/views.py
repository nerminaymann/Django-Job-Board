from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.shortcuts import render
from accounts.models import Profile
from .models import Information


# Create your views here.

@login_required(login_url='login')
def Send_Message(request):
    profile=Profile.objects.get(user=request.user)
    info=Information.objects.first()
    if request.method == 'POST':
        message=request.POST.get('message')
        email=request.POST.get('email')
        subject=request.POST.get('subject')

        send_mail(subject,
                  message,
                  request.user.email,
                  [email])
    context={'profile':profile,
             'info':info}
    return render(request,'contact/contact.html',context)