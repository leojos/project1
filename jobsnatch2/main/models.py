from distutils.command.upload import upload
from email.policy import default
from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime



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
    location= models.CharField(max_length=100,null=True)
    siteurl= models.CharField(max_length=100,null=True)
    fullname=models.CharField(max_length=100,null=True)


    # def __str__(self) :
    #     return {{self.id}}
class job(models.Model):
    job_id = models.AutoField(primary_key=True)
    job_title = models.CharField(max_length=100)
    salary = models.BigIntegerField(default=0)
    experience = models.CharField(max_length=100,blank=True, null=True)
    experiencein = models.CharField(max_length=100,blank=True, null=True)
    startdate =  models.DateField()
    lastdate =  models.DateField()
    vacancies = models.IntegerField(blank=True, null=True)
    job_description = models.TextField()
    cmp_id = models.ForeignKey(User ,default=None,on_delete=models.CASCADE)
    status=models.BooleanField('status', default=True)
    desti = models.CharField(max_length=100,null=True,)
    expl =  models.CharField(max_length=100,null=True,)
    tper = models.CharField(max_length=100,null=True,)
    plper = models.CharField(max_length=100,null=True,)
    cper = models.CharField(max_length=100,null=True,)
    jobtype=models.CharField(max_length=100,null=True,)
    qualification=models.CharField(max_length=100,null=True,)
    
    
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
    
    @property
    def loc(self):
        return self.cmp_id.location


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
    
    @property
    def loc(self):
        return self.jobs_id.loc
    
    @property
    def desti(self):
        return self.jobs_id.desti


class feedback(models.Model):
    f_id = models.AutoField(primary_key=True)
    can_id = models.ForeignKey(User ,default=None,on_delete=models.CASCADE)
    status=models.BooleanField('status', default=True) 
    feedback=models.TextField(null=True)
    percentage=models.FloatField(blank=True, null=True)
    good=models.BooleanField('good', default=True)
    bad=models.BooleanField('bad', default=True)
    neutral=models.BooleanField('neutral', default=True)
    rating=models.CharField(max_length=100,null=True,)


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
    img=models.ImageField(null=True,blank=True,upload_to="img/")
    pp=models.CharField(max_length=100,null=True)
    professsion=models.CharField(max_length=100,null=True)

class categ(models.Model):
    categ_id = models.AutoField(primary_key=True)
    status=models.BooleanField('status', default=True) 
    categname=models.CharField(max_length=100,null=True)
    img=models.ImageField(null=True,blank=True,upload_to="img/")

class internship(models.Model):
    intern_id = models.AutoField(primary_key=True)
    status=models.BooleanField('status', default=True) 
    title=models.CharField(max_length=100,null=True)
    durno = models.IntegerField(blank=True, null=True)
    durex = models.CharField(max_length=100,null=True)
    stdate =  models.DateField()
    enddate =  models.DateField()
    caption=models.CharField(max_length=100,null=True)
    img=models.ImageField(null=True,blank=True,upload_to="img/")
    category=models.CharField(max_length=100,null=True)
    stipend=models.IntegerField(blank=True, null=True)
    location=models.CharField(max_length=100,null=True)
    moreinfo=models.TextField(null=True)
    whoapply=models.TextField(null=True)
    onoff=models.CharField(max_length=100,null=True)
    certificate=models.BooleanField('status', default=True) 
    tim=models.CharField(max_length=100,null=True)

class classdetails(models.Model):
    in_id=models.AutoField(primary_key=True)
    status=models.BooleanField('status', default=True) 
    candi_id=models.ForeignKey(User ,default=None,on_delete=models.CASCADE)
    inter_id=models.ForeignKey(internship ,default=None,on_delete=models.CASCADE)
    interndate =  models.DateField(default=datetime.now, blank=True)
    interntimes = models.CharField(max_length=100,null=True,default=0)
    
    @property
    def canid(self):
      return self.candi_id.id
    
    @property
    def inid(self):
      return self.inter_id.title
    
class training(models.Model):
        train_id = models.AutoField(primary_key=True)
        status=models.BooleanField('status', default=True) 
        can_id=models.ForeignKey(User ,default=None,on_delete=models.CASCADE)
        typ=models.CharField(max_length=100,null=True)
        train_date =  models.DateField()
        train_time = models.CharField(max_length=100,null=True,default=0)

        @property
        def canid(self):
            return self.can_id.id

class resumme(models.Model):
    res_id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=100,blank=True)
    position=models.CharField(max_length=100,blank=True)
    email=models.EmailField(blank=True, null=True)
    carobj=models.TextField(blank=True)
    college=models.CharField(max_length=100,blank=True)
    colcourse=models.CharField(max_length=100,blank=True)
    colpy=models.CharField(max_length=100,blank=True)
    plus=models.CharField(max_length=100,blank=True)
    plusmarks=models.CharField(max_length=100,blank=True)
    pluspy=models.CharField(max_length=100,blank=True)
    ten=models.CharField(max_length=100,blank=True)
    schomarks=models.CharField(max_length=100,blank=True)
    schopy=models.CharField(max_length=100,blank=True)
    projects=models.TextField(blank=True)
    certi=models.TextField(blank=True)
    achi=models.TextField(blank=True)
    interns=models.TextField(blank=True)
    refe=models.TextField(blank=True)
    phone=models.IntegerField(blank=True, null=True,default=0)
    address=models.TextField(blank=True)
    strength=models.TextField(null=True,blank=True)
    skills=models.TextField(null=True,blank=True)
    lang=models.TextField(null=True,blank=True)
    hob=models.TextField(null=True,blank=True)
    soci=models.CharField(max_length=100,blank=True)
    coun=models.CharField(max_length=100,blank=True)
    status=models.BooleanField('status', default=0) 
    dob=models.DateField()
    gender=models.CharField(max_length=100,null=True)
    user_id=models.IntegerField(blank=True, null=True)

class scheduling(models.Model):
        sche_id = models.AutoField(primary_key=True)
        status=models.BooleanField('status', default=True) 
        user_id=models.ForeignKey(User ,default=None,on_delete=models.CASCADE)
        com_id=models.IntegerField(blank=True, null=True)
        typp=models.CharField(max_length=100,null=True)
        dura=models.CharField(max_length=100,null=True)
        train_date =  models.DateTimeField()
        acc=models.BooleanField('status', default=False) 
        dec=models.BooleanField('status', default=True) 
        reason=models.TextField(null=True,blank=True)
        can_date =  models.DateTimeField(null=True)
        approvedd=models.BooleanField('approveds', default=False)
        

        @property
        def name(self):
            return self.user_id.username
        
class offer(models.Model):
    offer_id=models.AutoField(primary_key=True)
    cann_id=models.IntegerField(blank=True, null=True)
    comm_id=models.IntegerField(blank=True, null=True)
    status=models.BooleanField('status', default=True) 

class offerr(models.Model):
    offer_id=models.AutoField(primary_key=True)
    cann_id=models.IntegerField(blank=True, null=True)
    comm_id=models.ForeignKey(User ,default=None,on_delete=models.CASCADE)
    status=models.BooleanField('status', default=True) 

    @property
    def id(self):
        return self.comm_id

    @property
    def email(self):
        return self.comm_id.email
    
    @property
    def about(self):
        return self.comm_id.about
    
    @property
    def image(self):
        return self.comm_id.image
    
    @property
    def username(self):
        return self.comm_id.username
    
    @property
    def phone(self):
        return self.comm_id.phone
    
    @property
    def address(self):
        return self.comm_id.address
    
    @property
    def recruiter(self):
        return self.comm_id.recruiter
    
    @property
    def cat(self):
        return self.comm_id.cat
    
    @property
    def loc(self):
        return self.comm_id.location


class wishlist(models.Model):
    wi_id=models.AutoField(primary_key=True)
    checkk=models.BooleanField('checkk', default=False) 
    cann_id=models.IntegerField(blank=True, null=True)
    comm_id=models.IntegerField(blank=True, null=True)
    jobb_id=models.IntegerField(blank=True, null=True)
