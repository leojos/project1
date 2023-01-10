from distutils.command.upload import upload
from email.policy import default
from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

sem=(
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
    image=models.ImageField(null=True,blank=True,upload_to="img/")
    proof=models.ImageField(null=True,blank=True,upload_to="img/")
    phone=models.IntegerField(blank=True, null=True,default=0)
    address=models.TextField(blank=True)
    recruiter=models.CharField(max_length=100,blank=True)
    skills=models.TextField(null=True,blank=True)
    approved=models.BooleanField('approved', default=False)

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
    status=models.BooleanField('status', default=True)
    
    
    @property
    def id(self):
        return self.cmp_id.id

    @property
    def email(self):
        return self.cmp_id.email
    
    @property
    def stat(self):
        return self.cmp_id.status
    
    @property
    def is_compamy(self):
        return self.cmp_id.is_company
    
    @property
    def about(self):
        return self.cmp_id.about
    
    @property
    def image(self):
        return self.cmp_id.image
    
    @property
    def username(self):
        return self.cmp_id.username
    
    @property
    def phone(self):
        return self.cmp_id.phone
    
    @property
    def address(self):
        return self.cmp_id.address
    
    @property
    def recruiter(self):
        return self.cmp_id.recruiter
    
    @property
    def cat(self):
        return self.cmp_id.cat


class appliedjob(models.Model):
    application_id = models.AutoField(primary_key=True)
    jobs_id = models.ForeignKey(job ,default=None,on_delete=models.CASCADE)
    can_id = models.ForeignKey(User ,default=None,on_delete=models.CASCADE)
    status=models.BooleanField('status', default=True) 
    accept=models.BooleanField('accept', default=True) 
    reject=models.BooleanField('reject', default=True) 
    applied=models.BooleanField('applied', default=True) 

    @property
    def username(self):
        return self.jobs_id.username
    
    @property
    def name(self):
        return self.can_id.username
    
    @property
    def phone(self):
        return self.can_id.phone
    
    @property
    def phones(self):
        return self.jobs_id.phone
    
    @property
    def address(self):
        return self.can_id.address
    
    @property
    def abt(self):
        return self.can_id.about
    

    @property
    def email(self):
        return self.can_id.email
    
    @property
    def emails(self):
        return self.jobs_id.email
    
    @property
    def recruiter(self):
        return self.jobs_id.recruiter
    
    @property
    def job_title(self):
        return self.jobs_id.job_title
    
    @property
    def cmp_id_id(self):
        return self.jobs_id.cmp_id_id
    
    @property
    def lastdate(self):
        return self.jobs_id.lastdate 
    
    @property
    def image(self):
        return self.can_id.image
    
    @property
    def skills(self):
        return self.can_id.skills
    
    @property
    def stat(self):
        return self.can_id.status
    
    @property
    def images(self):
        return self.jobs_id.image
    
    @property
    def cat(self):
        return self.can_id.cat
    
    @property
    def cat1(self):
        return self.jobs_id.cat


class feedback(models.Model):
    f_id = models.AutoField(primary_key=True)
    can_id = models.ForeignKey(User ,default=None,on_delete=models.CASCADE)
    status=models.BooleanField('status', default=True) 
    feedback=models.TextField(null=True)
    percentage=models.FloatField(blank=True, null=True)
    good=models.BooleanField('good', default=True)
    bad=models.BooleanField('bad', default=True)
    neutral=models.BooleanField('neutral', default=True)


    @property
    def username(self):
        return self.can_id.username

class blog(models.Model):
    b_id = models.AutoField(primary_key=True)
    status=models.BooleanField('status', default=True) 
    name=models.CharField(max_length=100,null=True)
    link=models.CharField(max_length=100,null=True)
    title=models.CharField(max_length=100,null=True)
    blogs=models.TextField(null=True)

class categ(models.Model):
    categ_id = models.AutoField(primary_key=True)
    status=models.BooleanField('status', default=True) 
    categname=models.CharField(max_length=100,null=True)
    img=models.ImageField(null=True,blank=True,upload_to="img/")
