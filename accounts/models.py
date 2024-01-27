from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(default='default_profile_pic.jpeg',upload_to='profile_pics/',)
    name = models.CharField(max_length=60,null=True)
    bio = models.TextField(max_length=500,null=True,blank=True)
    city = models.CharField(max_length=60,null=True)
    phone_number = models.BigIntegerField(blank=True,null=True)
    position = models.CharField(max_length=60,null=True)
    experience = models.IntegerField(blank=True,null=True)
    skills = models.TextField(max_length=500,null=True,blank=True)
    age = models.IntegerField(blank=True,null=True)
    date_of_birth = models.DateField(blank=True,null=True)
    education = models.TextField(max_length=200,blank=True,null=True)
    github_website = models.URLField(blank=True,null=True)
    linkedin_website = models.URLField(blank=True,null=True)
    facebook_website = models.URLField(blank=True,null=True)
    summary = models.TextField(max_length=500,null=True,blank=True)
    resume = models.FileField(upload_to='User Resumes/',blank=True,null=True)
    # slug = models.SlugField(blank=True,null=True)
    #
    # def save(self,*args,**kwargs):
    #     self.slug = slugify(self.user)
    #     super(Profile,self).save(*args,**kwargs)

    def __str__(self):
        return str(self.user)

#SIGNAL
#create new User -----> create new empty profile


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()

