from django.db import models
from django.db.models import Count
from django.utils.text import slugify
from django.contrib.auth.models import User

# Create your models here.

#THE CHOICES
Job_Type=[("Part Time","Part Time"),("Full Time","Full Time")]
Job_Nature=[("Remote","Remote"),("Hybrid","Hybrid"),("On Site","On Site")]

class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

#IF I WANTED TO STORE THE IMAGE WITH DIFERRENT NAME LIKE id.jpg OR  PositionName.jpg
def Uploaded_Images(instance, filename):
    imgName , extension=filename.split('.')
    return 'job_images/'+instance.title+'.'+extension

class Job(models.Model):
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    location = models.CharField(max_length=50)
    job_type = models.CharField(max_length=30,choices=Job_Type,default='')
    job_nature = models.CharField(max_length=30,choices=Job_Nature,default='')
    desc = models.TextField(max_length=1000)
    published_at = models.DateTimeField(auto_now=True)
    #NUMBER OF APPLICATIONS RECIEVED
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experience =models.IntegerField(default=1)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    job_img = models.ImageField(upload_to=Uploaded_Images)
    slug = models.SlugField(null=True,blank=True)
    #IF I WANTED TO UPLOAD THE IMAGE IN THE PATH 'media/job_images/ewfh.jpg
    # job_img = models.ImageField(upload_to='job_images')

    def count_jobs_of(category):
        return Job.objects.filter(category=category).count()

    #OVERRIVE SAVE METHOD: BEFORE COMPLETING THE SAVE OF CREATING RECORD
    #ADD THE TITLE TO SLUG FIELD AND SLUGIFY IT : PUT(-) BETWEEN TWO WORDS
    def save(self, *args, **kwargs):
        self.slug=slugify(self.title)
        super(Job,self).save(*args, **kwargs)

    def __str__(self):
        return self.title

# Category.objects.annotate(
#     items_count=Count('category__job')
# )

class Apply(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    job = models.ForeignKey(Job,on_delete=models.CASCADE)
    name= models.CharField(max_length=50,null=False)
    email = models.EmailField(max_length=50,null=False)
    website = models.URLField(max_length=100,blank=True)
    cv= models.FileField(upload_to='Apply Resumes',null=False, blank=False)
    cover_letter=models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name

