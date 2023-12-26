from django.db import models

# Create your models here.

#THE CHOICES
Job_Type=[("Part Time","Part Time"),("Full Time","Full Time")]
Job_Nature=[("Remote","Remote"),("Hybrid","Hybrid"),("On Site","On Site")]
class Job(models.Model):
    title = models.CharField(max_length=100)
    # location =
    job_type = models.CharField(max_length=30,choices=Job_Type,default='')
    job_nature = models.CharField(max_length=30,choices=Job_Nature,default='')
    desc = models.TextField(max_length=1000)
    published_at = models.DateTimeField(auto_now=True)
    #NUMBER OF APPLICATIONS RECIEVED
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experience =models.IntegerField(default=1)



    def __str__(self):
        return self.title
