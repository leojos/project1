from email.mime import application
from operator import countOf
from django.shortcuts import render, redirect
from .forms import SignUpForm, LoginForm
from django.contrib.auth import authenticate, login
from django.contrib import auth
from django.contrib import messages
from .models import User
from .models import job
from .models import blog
from .models import feedback
from .models import appliedjob
from .models import categ
from .models import internship
from .models import classdetails
from .models import training
from .models import resumme
from .models import scheduling
from django.contrib.auth.decorators import login_required
from django import forms
from django.db.models.functions import Now
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import nltk
import re
from nltk.corpus import stopwords
import pyttsx3
from django.http import HttpResponseNotFound
from twilio.rest import Client
# from faunadb import query as q
# import pytz
# from faunadb.objects import Ref
# from faunadb.client import FaunaClient
# import hashlib
# import datetime
# client = FaunaClient(secret="SECRET_KEY")
# indexes = client.query(q.paginate(q.indexes()))
# from django.shortcuts import render_to_response
# Create your views here.
nltk.download('stopwords')
set(stopwords.words('english'))

def index(request):
    cat=categ.objects.all()
    return render(request, 'index.html',{'cat':cat})
# def dash(request):
#     return render(request,"dash.html")

# def createresume(request):
#     if request.method=="POST":
#         username=request.session["user"]["username"]
#         full_name=request.POST.get("name")
#         address=request.POST.get("address")
#         phone=request.POST.get("phone")
#         email=request.POST.get("email")
#         about_you=request.POST.get("about")
#         education=request.POST.get("education")
#         career=request.POST.get("career")
#         job_1__start=request.POST.get("job-1__start")
#         job_1__end=request.POST.get("job-1__end")
#         job_1__details=request.POST.get("job-1__details")
#         job_2__start=request.POST.get("job-2__start")
#         job_2__end=request.POST.get("job-2__end")
#         job_2__details=request.POST.get("job-2__details")
#         job_3__start=request.POST.get("job-3__start")
#         job_3__end=request.POST.get("job-3__end")
#         job_3__details=request.POST.get("job-3__details")
#         references=request.POST.get("references")
#         try:
#             resume = client.query(q.get(q.match(q.index("resume_index"), username)))
#             quiz = client.query(q.update(q.ref(q.collection("Resume_Info"),resume["ref"].id()), {
#                 "data": {
#                     "user":username,
#                     "full_name": full_name,
#                     "address": address,
#                     "phone": phone,
#                     "email":email,
#                     "about_you":about_you,
#                     "education":education,
#                     "career":career,
#                     "job_1__start":job_1__start,
#                     "job_1__end":job_1__end,
#                     "job_1__details":job_1__details,
#                     "job_2__start":job_2__start,
#                     "job_2__end":job_2__end,
#                     "job_2__details":job_2__details,
#                     "job_3__start":job_3__start,
#                     "job_3__end":job_3__end,
#                     "job_3__details":job_3__details,
#                 }
#             }))
#             messages.add_message(request, messages.INFO, 'Resume Info Edited Successfully. Download Resume Now')
#             return redirect("App:createresume")
#         except:
#             quiz = client.query(q.create(q.collection("Resume_Info"), {
#                 "data": {
#                     "user":username,
#                     "full_name": full_name,
#                     "address": address,
#                     "phone": phone,
#                     "email":email,
#                     "about_you":about_you,
#                     "education":education,
#                     "job_1__start":job_1__start,
#                     "job_1__end":job_1__end,
#                     "job_1__details":job_1__details,
#                     "job_2__start":job_2__start,
#                     "job_2__end":job_2__end,
#                     "job_2__details":job_2__details,
#                     "job_3__start":job_3__start,
#                     "job_3__end":job_3__end,
#                     "job_3__details":job_3__details,
#                 }
#             }))
#             messages.add_message(request, messages.INFO, 'Resume Info Saved Successfully. Download Resume Now')
#             return redirect("App:resumes")
#     else:
#         try:
#             resume_info = client.query(q.get(q.match(q.index("resume_index"), request.session["user"]["username"])))["data"]
#             context={"resume_info":resume_info}
#             return render(request,"createresume.html",context)
#         except:
#             return render(request,"createresume.html")

# def resumes(request):
#     try:
#         resume_info = client.query(q.get(q.match(q.index("resume_index"), request.session["user"]["username"])))["data"]
#         context={"resume_info":resume_info}
#         return render(request,"resume.html",context)
#     except:
#         return render(request,"resume.html")

def my_form(request):
    engine = pyttsx3.init()
    engine.say('Hello, Welcome to the feedback section.')
    engine.runAndWait()
    return render(request,'form.html')
 

def my_post(request):
        if request.method == 'POST':
                stop_words = stopwords.words('english')
                # my contribution
                stop_words.remove('very')
                stop_words.remove('not')
                
                #convert to lowercase
                text1 = request.POST['text1'].lower()
                
                # my contribution
                text_final = ''.join(i for i in text1 if not i.isdigit())
                net_txt=re.sub('[^a-zA-Z0-9\n]', ' ',text_final)
                
                #remove stopwords    
                processed_doc1 = ' '.join([i for i in net_txt.split() if i not in stop_words])

                sa = SentimentIntensityAnalyzer()
                dd = sa.polarity_scores(text=processed_doc1)
                compound = round((1 + dd['compound'])/2, 2)
                final=compound*100
                
                if "enough" in text1 or "sufficient" in text1 or "ample" in text1 or "abudant" in text1:
                   engine = pyttsx3.init()
                   engine.say('You liked us by'+str(final)+'% Thank you for your valuable response')
                   engine.runAndWait()
                   feeds = feedback(feedback=text1,percentage=final,good=True,bad=True,neutral=False)
                   feeds.can_id =request.user
                   feeds.save()
                   return render(request,'form.html',{'final': final,'text1':net_txt})
                   
                elif final == 50:
                   engine = pyttsx3.init()
                   engine.say('Please enter an adequate resposnse, Thank You')
                   engine.runAndWait()
                   return render(request,'form.html',{'final': final,'text1':net_txt})
                else:
                   engine = pyttsx3.init()
                   engine.say('You liked us by'+str(final)+'% Thank you for your valuable response')
                   engine.runAndWait()
                   if final > 50:
                      feeds = feedback(feedback=text1,percentage=final,good=False,bad=True,neutral=True)
                      feeds.can_id =request.user
                      feeds.save()
                      return render(request,'form.html',{'final': final,'text1':net_txt})
                   elif final < 50:
                      feeds = feedback(feedback=text1,percentage=final,bad=False,good=True,neutral=True)
                      feeds.can_id =request.user
                      feeds.save()
                      return render(request,'form.html',{'final': final,'text1':net_txt})
                   else:
                       feeds = feedback(feedback=text1,percentage=final)
                       feeds.can_id =request.user
                       feeds.save()
                       return render(request,'form.html',{'final': final,'text1':net_txt})
        else:
           return redirect('my_form')

def feedbacks(request):
    feed=feedback.objects.all()
    context = {'feed': feed}
    return render(request,"feedbackview.html", context)

def moreblogs(request):
    feed=blog.objects.all()
    context = {'feed': feed}
    return render(request,"moreblogs.html", context)

def graph(request):
    cat=categ.objects.all()
    return render(request,"graph.html",{'cat':cat})



def register(request):
    msg = None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            
            if not username.isalpha():
                messages.error(request,'First Name must only be letters. Number or other special character are not allowed')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.error(request,'Email Taken')
                return redirect('register')
            else:
               user = form.save()
               msg = 'user created'
               return redirect('login')

           
        else:
            msg = 'form is not valid'
    else:
        form = SignUpForm()
    return render(request,'register.html', {'form': form, 'msg': msg})


# def login(request):
#     form = LoginForm(request.POST or None)
#     msg = None
#     if request.method == 'POST':
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             user = authenticate(username=username, password=password)
#             if user is not None and user.is_admin:
#                 if user.is_admin=='True':
#                     request.sessions['u']='ADMIN'
#                 # login(request, user)
#                 return redirect('admin')
#             elif user is not None and user.is_candidate:
#                 if user.is_candidate=='True':
#                     request.sessions['u']='Candidate'
#                 # login(request, user)
#                 return redirect('candidate')
#             elif user is not None and user.is_company:
#                 # login(request, user)
#                 return redirect('company')
#             else:
#                 msg= 'invalid credentials'
#         else:
#             msg = 'error validating form'
#     return render(request, 'login.html', {'form': form, 'msg': msg})


def login(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_admin:
                request.session['usr']=user.username
                auth.login(request, user)
                #login(request, user)
                return redirect('admin')
            elif user is not None and user.is_candidate:
                request.session['can']=user.username
                auth.login(request, user)
                #login(request, user)
                return redirect('candidate')
            elif user is not None and user.is_company:
                request.session['cmp']=user.username
                auth.login(request, user)
                #login(request, user)
                return redirect('company')
            else:
                msg= 'invalid credentials'
        else:
            msg = 'error validating form'
    return render(request, 'login.html', {'form': form, 'msg': msg})

def admin(request):
    if 'usr' in request.session:
       data = job.objects.all()
       data = job.objects.filter(status=1).count()
       data1 = User.objects.all()
       data1 = User.objects.filter(is_candidate=1).count()
       data2 = User.objects.all()
       data2 = User.objects.filter(is_company=1).count()
      #  data1 = job.objects.all()
      #  if request.method == 'POST':
      #   cmpid=request.POST['cmpid']
      #   data1= appliedjob.objects.filter(jobs_id_id=cmpid)
       context = {'data': data,'data1':data1,'data2':data2}
       return render(request,"admin.html", context)
    return render(request,'index.html')
    # return render(request,'admin.html')

def admincom(request):
    if 'usr' in request.session:
      #  data = job.objects.all()
       data = User.objects.filter(is_company=1)
      #  data1 = User.objects.all()
      #  data1 = User.objects.filter(is_company=1).values_list('id',flat=True)
      #  for i in data1 :
      #       data = job.objects.filter(cmp_id_id=i)
      #  data1 = job.objects.all()
      #  if request.method == 'POST':
      #   cmpid=request.POST['cmpid']
      #   data1= appliedjob.objects.filter(jobs_id_id=cmpid)
       context = {'data': data}
       return render(request,"admincom.html", context)
    return render(request,'index.html')
    # return render(request,'admin.html')

def admincan(request):
    if 'usr' in request.session:
       data = appliedjob.objects.all()
       data1 = User.objects.filter(is_candidate=1)
       
      #  data1 = job.objects.all()
      #  if request.method == 'POST':
      #   cmpid=request.POST['cmpid']
      #   data1= appliedjob.objects.filter(jobs_id_id=cmpid)
       context = {'data': data,'data1': data1}
       return render(request,"admincan.html", context)
    return render(request,'index.html')
    # return render(request,'admin.html')


def candidate(request):
    if 'can' in request.session:
      return render(request,'candidate.html')
    return render(request,'index.html')
    # return render(request,'candidate.html')


def company(request):
    if 'cmp' in request.session:
      return render(request,'company.html')
    return render(request,'index.html')
    # return render(request,'company.html')

def avljobs(request):
     if 'can' in request.session:
       data = job.objects.all()
       
       #  data1 = User.objects.all()
       data1 = User.objects.filter(is_company=True)
       data2 = User.objects.all()
       
       data3 = job.objects.all()
       data3 = job.objects.filter(lastdate__gt=Now())
       
       data4 = job.objects.all()
       data5 = appliedjob.objects.all()

       data6 = User.objects.filter(is_company=True)

       if request.method == 'POST':
        # num=request.POST['text']
        st=request.POST.get('number')
        compname=request.POST.get('compname')
        loc=request.POST.get('loc')
        if st!=None:
          data3 = job.objects.filter(job_title=st,lastdate__gt=Now())
        elif compname!=None:
          # data2 = User.objects.filter(username=compname).values('id')
          data2 = User.objects.filter(username=compname).values_list('id',flat=True)
          for i in data2 :
            data3 = job.objects.filter(cmp_id_id=i,lastdate__gt=Now())
        elif loc!=None:
            data2 = User.objects.filter(location=loc).values_list('id',flat=True)
            for i in data2 :
             data3 = job.objects.filter(cmp_id_id=i,lastdate__gt=Now())
          # data2 = User.objects.filter(username=compname).values_list(flat=True)
          # for i in data2:
          #   print(i)
          # data3 = job.objects.filter(cmp_id_id=data2)
          # data = job.objects.filter(job_title=st)

       context = {'data': data,'data1':data1,'data2':data2,'data3':data3,'data4':data4,'data5':data5,'data6':data6}
       return render(request,"avljobs.html", context)
     return render(request,'index.html')

def comppage(request):
  
    data = job.objects.all()
    if request.method == 'POST':
      cmpid=request.POST['cmpid']
      data = job.objects.filter(job_id=cmpid)
      context = {'data': data}
      return render(request, 'comppage.html', context)
    return render(request,'index.html')

def comppages(request):
  if 'can' in request.session:
    data = job.objects.all()
    if request.method == 'POST':
      cmpid=request.POST['cmpid']
      jobid=request.POST['jobid']
      data = job.objects.filter(cmp_id=cmpid,job_id=jobid)
      context = {'data': data}
      return render(request, 'comppage.html', context)

  return render(request,'index.html')

def canpage(request):
  
    data = appliedjob.objects.all()
    if request.method == 'POST':
      canid=request.POST.get('canid')
      jobid=request.POST['jobid']
      data = appliedjob.objects.filter(can_id_id=canid,jobs_id=jobid)
      context = {'data': data}
      return render(request, 'canpage.html', context)
    return render(request,'index.html')

def appliedjobs(request):
     if 'can' in request.session:
       data = appliedjob.objects.all()
       dat1 = job.objects.all()
       data1 = job.objects.filter(lastdate__gt=Now())
      #  user=User.objects.all()
      #  user=User.objects.filter(id=appliedjob.can_id_id)
      #  data = appliedjob.objects.filter(User.id==User.id)
       context = {'data': data,'data1': data1}
       return render(request,"appliedjobs.html",context)
     return render(request,'index.html')
    # return render(request,'company.html')

def jobpost(request):
   if 'cmp' in request.session:
        return render(request,'jobpost.html')
        # messages.error(request,'Admin has not approved you yet!!')
        # return render(request,'company.html')
   return render(request,'index.html')

def logout(request):
    auth.logout(request)
    return redirect('index')

def updaterecord(request, id):
 if 'can' in request.session:
  if request.method == 'POST':
    username = request.POST['username']
    email = request.POST['email']
    phone = request.POST['phone']
    address = request.POST['address']
    about = request.POST['about']
    skills = request.POST['skills']
  #   password = request.POST['password']
    user = User.objects.get(id=id)
    user.username = username
    user.email = email
    user.phone = phone
    user.address = address
    user.about = about
    user.skills = skills
  #   user.password = password
    user.save()
    return redirect('candidate')

def updatecan(request, id):
   if 'can' in request.session:
      image = request.FILES.get('avatar')
      user = User.objects.get(id=id)
      user.image = image
      user.save()
      return redirect('candidate')

def updatecom(request, id):
   if 'cmp' in request.session:
      username = request.POST['username']
      email = request.POST['email']
      about = request.POST['about']
      phone = request.POST['phone']
      address = request.POST['address']
      recru = request.POST['recru']
      loc = request.POST['loc']
    #   password = request.POST['password']
      user = User.objects.get(id=id)
      user.username = username
      user.email = email
      user.about = about
      user.phone = phone
      user.location = loc
      user.address = address
      user.recruiter = recru
    #   user.password = password
      user.save()
      return redirect('company')

def updateco(request, id):
   if 'cmp' in request.session:
      image = request.FILES.get('img')
      user = User.objects.get(id=id)
      user.image = image
      user.save()
      return redirect('company')

def updatec(request, id):
   if 'cmp' in request.session:
      proof = request.FILES.get('proof')
      user = User.objects.get(id=id)
      user.proof = proof
      user.save()
      return redirect('company')

def postjob(request):
 if 'cmp' in request.session:
  if request.method == 'POST':
        job_title = request.POST['title']
        salary  = request.POST['salary']
        experience = request.POST['experience']
        lastdate = request.POST['date']
        vacancies = request.POST['vacancies']
        job_description = request.POST['desc']
        desti = request.POST['desti']
        member = job(job_title=job_title,salary=salary,experience=experience,lastdate=lastdate,vacancies=vacancies,job_description=job_description,desti=desti)
        # instance=member.save()
        member.cmp_id =request.user
        member.save()
        return redirect('jobpost')
        # else:
        #      messages.info(request,'Password not matching')
        #      return redirect('/')
  else:
       return render(request,'index.html')
 return render(request,'index.html')

def acts(request):
    if 'cmp' in request.session:
      #  user = User.objects.all()
       data = job.objects.all()
      #  data = job.objects.get(cmp_id_id=User.id)
       context = {'data': data}
       return render(request,"acts.html", context)
    return render(request,'index.html')
    # return render(request,'company.html')

def authdeletecom(request):
  username = request.POST['username']
  member = User.objects.get(username=username)
  member.status=True
  member.save()
  return redirect('admincom')

def adminapprove(request):
  username = request.POST.get('username')
  member = User.objects.get(username=username)
  member.approved=True
  member.save()
  return redirect('admincom')

def authdeletecan(request):
  username = request.POST['username']
  member = User.objects.get(username=username)
  member.status=True
  member.save()
  return redirect('admincan')

# def jobdelete(request):
#   if 'can' in request.session:
#     jobid = request.POST['jobid']
#     member = appliedjob.objects.get(jobs_id_id=jobid)
#     member.status=False
#     member.save()
#     return redirect('appliedjobs')

def applyjob(request):
  if 'can' in request.session:
    if request.method == 'POST':
      idvalue = request.POST['idvalue']
      member=appliedjob()
      member.can_id =request.user
      member.jobs_id =job.objects.get(job_id=idvalue)
      member.save()
      return redirect('avljobs')
  return render(request,'index.html')


def avlcandidates(request):
    if 'cmp' in request.session:
      #  canid=request.POST['canid']
       data = appliedjob.objects.all()
       data = appliedjob.objects.filter(accept=True,reject=True)
      #  data1=User.objects.all()
      #  data1 = User.objects.filter(id=data.can_id_id)

      #  data = appliedjob.objects.filter(jobs_id_id=job.job_id)
      #  user=job.objects.all()
      #  user=User.objects.filter(id=appliedjob.can_id_id)
      #  data = appliedjob.objects.filter(User.id==User.id)
       context = {'data': data}
       return render(request,"avlcandidates.html",context)
    return render(request,'index.html')
    # return render(request,'company.html')

def acceptedcan(request):
    if 'cmp' in request.session:
      #  canid=request.POST['canid']
       data = appliedjob.objects.all()
       data = appliedjob.objects.filter(accept=False)
      #  data1=User.objects.all()
      #  data1 = User.objects.filter(id=data.can_id_id)

      #  data = appliedjob.objects.filter(jobs_id_id=job.job_id)
      #  user=job.objects.all()
      #  user=User.objects.filter(id=appliedjob.can_id_id)
      #  data = appliedjob.objects.filter(User.id==User.id)
       context = {'data': data}
       return render(request,"acceptedcan.html",context)
    return render(request,'index.html')

def acceptedcom(request):
    if 'can' in request.session:
      #  canid=request.POST['canid']
       data = appliedjob.objects.all()

       data = appliedjob.objects.filter(accept=False)
      #  data1=User.objects.all()
      #  data1 = User.objects.filter(id=data.can_id_id)

      #  data = appliedjob.objects.filter(jobs_id_id=job.job_id)
      #  user=job.objects.all()
      #  user=User.objects.filter(id=appliedjob.can_id_id)
      #  data = appliedjob.objects.filter(User.id==User.id)
       context = {'data': data}
       return render(request,"acceptedcom.html",context)
    return render(request,'index.html')

def comaccept(request):
    if 'cmp' in request.session:
       accept= request.POST['accept']
       data = appliedjob.objects.get(application_id=accept)
       data.accept=False
       data.save()
       return redirect('avlcandidates')
    return render(request,'index.html')
    # return render(request,'company.html')

def comreject(request):
    if 'cmp' in request.session:
       reject= request.POST['reject']
       data = appliedjob.objects.get(application_id=reject)
       data.reject=False
       data.save()
       return redirect('avlcandidates')
    return render(request,'index.html')
    # return render(request,'company.html')

def aptitude(request):
    if 'can' in request.session:
      return render(request,'aptitude.html')
    return render(request,'index.html')

def gd(request):
    if 'can' in request.session:
      return render(request,'gd.html')
    return render(request,'index.html')

def interview(request):
    if 'can' in request.session:
      return render(request,'interview.html')
    return render(request,'index.html')

def anf(request):
      return render(request,'AnF.html')

def pnt(request):
      return render(request,'PnT.html')

def dna(request):
      return render(request,'DnA.html')

def wnt(request):
      return render(request,'WnT.html')

def ent(request):
      return render(request,'EnT.html')

def rnf(request):
      return render(request,'RnF.html')

def dnm(request):
      return render(request,'DnM.html')

def snm(request):
      return render(request,'SnM.html')

def resume(request):
      return render(request,'resume.html')

def blogpost(request):
      return render(request,'blogpost.html')

def resum(request):
      return render(request,'resum.html')

def appti(request):
      return render(request,'appti.html')

def convince(request):
      return render(request,'convince.html')

def blogg(request):
    if request.method == 'POST':
        name = request.POST['name']
        link  = request.POST['link']
        title = request.POST['title']
        blogs = request.POST['blogs']
        image = request.FILES.get('pic')
        member = blog(name=name,link=link,title=title,blogs=blogs,img=image)
        member.save()
        return redirect('blogpost')
    return redirect('index')

def adminnew(request):
      return render(request,'adminnew.html')

def addcat(request):
      if request.method == 'POST':
        cat = request.POST['cat']
        image = request.FILES.get('p')
        member = categ(categname=cat,img=image)
        member.save()
        return redirect('admin')

def fullblog(request):
    if request.method == 'POST':
        full = request.POST['full']
        feed=blog.objects.filter(b_id=full)
        context = {'feed': feed}
        return render(request,"fullblog.html", context)

def intern(request):
      if request.method == 'POST':
        tit = request.POST['tit']
        cap = request.POST['cap']
        durno = request.POST['durno']
        durex = request.POST['durex']
        edate = request.POST['edate']
        image = request.FILES.get('p')
        member = internship(title=tit,caption=cap,durno=durno,durex=durex,enddate=edate,img=image)
        member.save()
        return redirect('admin')

def moreinterns(request,id):
    feed=internship.objects.all()
    more=classdetails.objects.filter(candi_id=id)
    context = {'feed': feed,'more':more}
    return render(request,"moreinterns.html", context)

def interndetails(request,id):
    ptime= request.POST['ptime']
    pday= request.POST['pday']
    inid= request.POST['inid']
    # caid= request.POST['caid']
    user = classdetails(candi_id_id=id,inter_id_id=inid,interndate=pday,interntimes=ptime)
    user.save()
    return redirect('candidate')

def classdetail(request):
    inid= request.POST['inid']
    caid= request.POST['caid']
    more=classdetails.objects.filter(candi_id=caid,inter_id=inid)
    feed=internship.objects.filter(intern_id=inid)
    can=User.objects.get(id=caid)
    inter=internship.objects.get(intern_id=inid)
    # user = classdetails(candi_id=caid,inter_id=inid,interndate,interntimes)
    # user.save()
    return render(request,'classdetails.html',{'can':can.username,'inter':inter.title,'interid':inter.intern_id,'more':more,'feed':feed,'mo':inid,'mor':caid})

def train(request):
    typ= request.POST.get('type')
    pday= request.POST['pday']
    ptime= request.POST['ptime']
    caid= request.POST['caid']
    user = training(can_id_id=caid,typ=typ,train_date=pday,train_time=ptime)
    user.save()
    return redirect('candidate')

def activity(request):
  if 'can' in request.session:
    acti=training.objects.filter(can_id=request.user)
    acti2=classdetails.objects.filter(candi_id=request.user)
    acti3=scheduling.objects.filter(can_id=request.user.id)
    return render(request,'activity.html',{'acti':acti,'acti2':acti2,'acti3':acti3})

def map(request):
    return render(request,'map.html')

def setdate(request):
    jobid= request.POST['jobid']
    canid= request.POST['canid']
    return render(request,'setdate.html')

def res(request):
    r=resumme.objects.all()
    return render(request,'res.html',{'r':r})

def resdetails(request):
    return render(request,'resdetails.html')

def resubmit(request):
    username= request.POST['username']
    pos= request.POST['pos']
    co= request.POST['co']
    email= request.POST['email']
    col= request.POST['col']
    plus= request.POST['plus']
    scho= request.POST['scho']
    pro= request.POST['pro']
    certi= request.POST['certi']
    achi= request.POST['achi']
    intern= request.POST['intern']
    ref= request.POST['ref']
    phone= request.POST['phone']
    address= request.POST['address']
    stre= request.POST['stre']
    skills= request.POST['skills']
    lang= request.POST['lang']
    hob= request.POST['hob']
    soli= request.POST['soli']
    country= request.POST['country']
    dob= request.POST['dob']
    gen= request.POST['gen']
    user = resumme(name=username,position=pos,email=email,carobj=co,college=col,plus=plus,ten=scho,projects=pro,certi=certi,achi=achi,interns=intern,refe=ref,phone=phone,address=address,strength=stre,skills=skills,lang=lang,hob=hob,soci=soli,coun=country,dob=dob,gender=gen)
    user.save()
    return redirect('res')

def sche(request):
    timm= request.POST['timm']
    ty= request.POST['ty']
    tim= request.POST['tim']
    caid= request.POST['caid']
    canid= request.POST['canid']
    user = scheduling(user_id_id=caid,train_date=tim,typp=ty,can_id=canid,dura=timm)
    user.save()
    ac=User.objects.filter(id=canid)
    account_sid = "ACbe5a012071ff14a371492b37cd98f240"
    auth_token = "2d296dcfc02cb8fcf25e6fc0f20e424b"
    client = Client(account_sid, auth_token)
    message = client.messages.create(
    body="Hello from JobSnatch {ac.username}",
    from_="+15076085128",
    to="+917025484895"
    )

    print(message.sid)
    return redirect('acceptedcan')