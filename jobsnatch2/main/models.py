from distutils.command.upload import upload
from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

sem=(
    ("null", "null"),
    ("Programming and Tech", "Programming and Tech"),
    ("Accounting and Finance", "Accounting and Finance"),
    ("Data Science and Analytics", "Data Science and Analytics"),
    ("Writing \ Translation", "Writing \ Translation"),
    ("Education \ Training", "Education \ Training"),
    ("Restaurant \ Food Service", "Restaurant \ Food Service"),
    ("Design,Art and Multimedia", "Design,Art and Multimedia"),
    ("Sales \ Markeing", "Sales \ Markeing"),
)

# role=(
#     ("admin", "admin"),
#     ("candidate", "candidateh"),
#     ("company", "company"),
# )
class User(AbstractUser):
    is_admin=models.BooleanField('is_admin',default=False)  
    is_candidate=models.BooleanField('is_candidate',default=False)  
    is_company=models.BooleanField('is_company',default=False)  
    status=models.BooleanField('status', default=0) 
    about=models.TextField(null=True)
    cat=models.CharField(max_length=100,null=True,choices=sem,default=0)
    image=models.ImageField(null=True,upload_to="img/")

    # def __str__(self) :
    #     return {{self.id}}
class job(models.Model):
    job_id = models.AutoField(primary_key=True)
    job_title = models.CharField(max_length=100)
    salary = models.BigIntegerField(default=0)
    experience = models.IntegerField(blank=True, null=True)
    lastdate =  models.DateField()
    vacancies = models.IntegerField(blank=True, null=True)
    job_description = models.TextField()
    cmp_id = models.ForeignKey(User ,default=None,on_delete=models.CASCADE)

class appliedjob(models.Model):
    application_id = models.AutoField(primary_key=True)
    jobs_id = models.ForeignKey(job ,default=None,on_delete=models.CASCADE)
    can_id = models.ForeignKey(User ,default=None,on_delete=models.CASCADE)
    status=models.BooleanField('status', default=True) 



    