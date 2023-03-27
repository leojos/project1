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
from .models import offerr
from .models import wishlist
from django.contrib.auth.decorators import login_required
from django import forms
from django.db.models.functions import Now
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import nltk
import re
from nltk.corpus import stopwords
import pyttsx3
from django.http import HttpResponseNotFound,HttpResponseRedirect,FileResponse
from twilio.rest import Client
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
from django.http import HttpResponse
from django.views.generic import View

from main.utils import render_to_pdf #created in step 4

from django.template.loader import get_template

import razorpay
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseBadRequest

from django.http import JsonResponse

# from django.template.loader import get_template
# from xhtml2pdf import pisa
# from io import BytesIO
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
    ab=feedback.objects.filter(good=False).count()
    cd=feedback.objects.filter(bad=False).count()
    ef=feedback.objects.filter(neutral=False).count()
    return render(request, 'index.html',{'cat':cat,'ab':ab,'cd':cd,'ef':ef})

# def pdf_view(request):
#     r=resumme.objects.all()
#     context_dict={'r':r}
#     template = get_template('res.html')
#     html = template.render(context_dict)
#     output = BytesIO()
#     pdf = pisa.CreatePDF(BytesIO(html.encode("UTF-8")), dest=output)
#     if not pdf.err:
#         response = HttpResponse(content_type='application/pdf')
#         response.write(output.getvalue())
#         response['Content-Disposition'] = 'attachment; filename="my_pdf.pdf"'
#         return response
#     return HttpResponse('Error rendering PDF', status=400)

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
       data3 = categ.objects.all().count()
       data4 = internship.objects.all().count()
       data5 = feedback.objects.all().count()
       ab=feedback.objects.filter(good=False).count()
       cd=feedback.objects.filter(bad=False).count()
       ef=feedback.objects.filter(neutral=False).count()
      #  data1 = job.objects.all()
      #  if request.method == 'POST':
      #   cmpid=request.POST['cmpid']
      #   data1= appliedjob.objects.filter(jobs_id_id=cmpid)
       context = {'data': data,'data1':data1,'data2':data2,'data3':data3,'data4':data4,'data5':data5,'ab':ab,'cd':cd,'ef':ef}
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
       data7 = User.objects.filter(is_candidate=True)
       data8 = wishlist.objects.filter(cann_id=request.user.id)
       data9 = wishlist.objects.filter(cann_id=request.user.id).count()
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

       context = {'data': data,'data1':data1,'data2':data2,'data3':data3,'data4':data4,'data5':data5,'data6':data6,'data7':data7,'data8':data8,'data9':data9}
       return render(request,"avljobs.html", context)
     return render(request,'index.html')

def comppage(request):
  
    data = job.objects.all()
    data1 = appliedjob.objects.filter(can_id_id=request.user.id)
    if request.method == 'POST':
      cmpid=request.POST['cmpid']
      data = job.objects.filter(job_id=cmpid)
      context = {'data': data,'data1': data1}
      return render(request, 'comppage.html', context)
    return render(request,'index.html')

def comppage2(request):
    data = offerr.objects.all()
    if request.method == 'POST':
      idd=request.POST['idd']
      data = job.objects.filter(cmp_id=idd)
      context = {'data': data}
      return render(request, 'comppage.html', context)
    return render(request,'index.html')

def comppage3(request):
    if request.method == 'POST':
      cmpid=request.POST['cmpid']
      data = User.objects.filter(id=cmpid)
      context = {'data': data}
      return render(request, 'comppage3.html', context)
    return render(request,'index.html')

def comppage4(request):
  
    data = job.objects.all()
    if request.method == 'POST':
      cmpid=request.POST['cmpid']
      data = job.objects.filter(job_id=cmpid)
      context = {'data': data}
      return render(request, 'comppage3.html', context)
    return render(request,'index.html')

def comppages(request):
  if 'can' in request.session:
    data = job.objects.all()
    if request.method == 'POST':
      cmpid=request.POST['cmpid']
      jobid=request.POST['jobid']
      data = job.objects.filter(cmp_id=cmpid,job_id=jobid)
      context = {'data': data}
      return render(request, 'comppages.html', context)

  return render(request,'index.html')

def canpage(request):
  
    
    if request.method == 'POST':
      canid=request.POST.get('canid')
      jobid=request.POST['jobid']
      data = appliedjob.objects.filter(can_id_id=canid,jobs_id=jobid,accept=True)
      context = {'data': data}
      return render(request, 'canpage.html', context)
    return render(request,'index.html')

def canpage2(request):
  
    
    if request.method == 'POST':
      canid=request.POST.get('canid')
      jobid=request.POST['jobid']
      data = appliedjob.objects.filter(can_id_id=canid,jobs_id=jobid,accept=False)
      context = {'data': data}
      return render(request, 'canpage.html', context)
    return render(request,'index.html')

def canpage3(request):
    if request.method == 'POST':
      canid=request.POST.get('canid')

      data = User.objects.filter(id=canid)
      context = {'data': data}
      return render(request, 'canpage3.html', context)
    return render(request,'index.html')

def canpage4(request):
    if request.method == 'POST':
      canid=request.POST.get('canid')

      data = User.objects.filter(id=canid)
      context = {'data': data}
      return render(request, 'canpage4.html', context)
    return render(request,'index.html')

def appliedjobs(request):
     if 'can' in request.session:
       data = appliedjob.objects.all()
       data1 = job.objects.all()
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
    fullname = request.POST['fullname']
  #   password = request.POST['password']
    user = User.objects.get(id=id)
    user.username = username
    user.email = email
    user.phone = phone
    user.address = address
    user.about = about
    user.skills = skills
    user.fullname = fullname
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
      wu = request.POST['wu']
    #   password = request.POST['password']
      user = User.objects.get(id=id)
      user.username = username
      user.email = email
      user.about = about
      user.phone = phone
      user.location = loc
      user.address = address
      user.recruiter = recru
      user.siteurl = wu
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
        experiencein = request.POST['experiencein']
        startdate = request.POST['sdate']
        lastdate = request.POST['date']
        vacancies = request.POST['vacancies']
        job_description = request.POST['desc']
        desti = request.POST['desti']
        expl = request.POST['expl']
        quali = request.POST.getlist('quali')
        jtype = request.POST.get('jtype')
        tenth = request.POST.get('tenth')
        pltwo = request.POST.get('pltwo')
        crse = request.POST.get('crse')
        for value in quali:
         member = job(job_title=job_title,salary=salary,experience=experience,experiencein=experiencein,startdate=startdate,lastdate=lastdate,vacancies=vacancies,job_description=job_description,desti=desti,expl=expl,jobtype=jtype,qualification=value,tper=tenth,plper=pltwo,cper=crse)
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
      #  jobid=request.POST['jobid']
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
        caty = request.POST['caty']
        image = request.FILES.get('p')
        member = internship(title=tit,caption=cap,durno=durno,durex=durex,enddate=edate,img=image,category=caty)
        member.save()
        return redirect('addin')

def intern1(request):
      if request.method == 'POST':
        tit = request.POST['tit']
        cap = request.POST['cap']
        durno = request.POST['durno']
        durex = request.POST['durex']
        sdate = request.POST['sdate']
        edate = request.POST['edate']
        caty = request.POST['caty']
        loc = request.POST['loc']
        ofon = request.POST['ofon']
        about = request.POST['about']
        stip = request.POST['stip']
        wca = request.POST['wca']
        image = request.FILES.get('p')
        member = internship(title=tit,caption=cap,durno=durno,durex=durex,stdate=sdate,enddate=edate,img=image,category=caty,location=loc,onoff=ofon,stipend=stip,whoapply=wca,moreinfo=about)
        member.save()
        return redirect('inadd')

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
    return redirect('homepage')

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
    return redirect('homepage')

def activity(request):
  if 'can' in request.session:
    acti=training.objects.filter(can_id=request.user,train_date__gt=Now())
    acti2=classdetails.objects.filter(candi_id=request.user,interndate__gt=Now())
    acti3=scheduling.objects.filter(user_id_id=request.user.id)
    acti4=offerr.objects.filter(cann_id=request.user.id)
    return render(request,'activity.html',{'acti':acti,'acti2':acti2,'acti3':acti3,'acti4':acti4})

def map(request):
    return render(request,'map.html')

def setdate(request):
    jobid= request.POST['jobid']
    canid= request.POST['canid']
    return render(request,'setdate.html')



def my_view(request):
    # Retrieve data from the database
            data1=resumme.objects.filter(user_id = request.user.id)
            data2=request.user.image
    # Render an HTML template using the retrieved data
            template = get_template('res.html')
            html = template.render({'data1': data1,'data2': data2})

            # Generate a PDF from the HTML using xhtml2pdf
            response = HttpResponse(content_type='application/pdf')
            response['Content-Disposition'] = 'filename="my_pdf.pdf"'

            pisa_status = pisa.CreatePDF(html, dest=response)
            if pisa_status.err:
                return HttpResponse('Error generating PDF file')
            return response

def my_vi(request):
    # Retrieve data from the database
            data1=User.objects.filter(id = request.user.id)
            data2=request.user.image
    # Render an HTML template using the retrieved data
            template = get_template('new.html')
            html = template.render({'data1': data1,'data2': data2})

            # Generate a PDF from the HTML using xhtml2pdf
            response = HttpResponse(content_type='application/pdf')
            response['Content-Disposition'] = 'filename="my_pdf.pdf"'

            pisa_status = pisa.CreatePDF(html, dest=response)
            if pisa_status.err:
                return HttpResponse('Error generating PDF file')
            return response


# def get(*args, **kwargs):
#         r=resumme.objects.all()
#         data={
#             "r":r,
#         }
#         pdf = render_to_pdf('res.html',data)
#         if pdf:
#             response=HttpResponse(pdf,content_type='application/pdf')
#             # filename = "Report_for_%s.pdf" %(data['id'])
            
#             return response
#         return HttpResponse("Page Not Found")
def res(request):
    data1=resumme.objects.filter(user_id = request.user.id)
    return render(request,'res.html',{'data1':data1})

def resdetails(request):
    return render(request,'resdetails.html')

def resubmit(request):
    username= request.POST['username']
    pos= request.POST['pos']
    co= request.POST['co']
    email= request.POST['email']
    col= request.POST['col']
    colcourse= request.POST['colcourse']
    colpy= request.POST['colpy']
    plus= request.POST['plus']
    plusmarks= request.POST['plusmarks']
    pluspy= request.POST['pluspy']
    scho= request.POST['scho']
    schomarks= request.POST['schomarks']
    schopy= request.POST['schopy']
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
    uid= request.POST['uid']
    userr = resumme(name=username,position=pos,email=email,carobj=co,college=col,plus=plus,ten=scho,projects=pro,certi=certi,achi=achi,interns=intern,refe=ref,phone=phone,address=address,strength=stre,skills=skills,lang=lang,hob=hob,soci=soli,coun=country,dob=dob,gender=gen,user_id=uid,colcourse=colcourse,colpy=colpy,plusmarks=plusmarks,pluspy=pluspy,schomarks=schomarks,schopy=schopy)
    userr.save()
    return redirect('res')

def sche(request):
    timm= request.POST['timm']
    ty= request.POST['ty']
    tim= request.POST['tim']
    caid= request.POST['caid']
    canid= request.POST['canid']
    user = scheduling(user_id_id=canid,train_date=tim,typp=ty,com_id=caid,dura=timm)
    user.save()
    # Download the helper library from https://www.twilio.com/docs/python/install
    account_sid = "ACcaf3a016ba44451632b6b9d52ec003f1"
    auth_token = "b8561c64ea3b53e6c993004e2cf2f593"
    client = Client(account_sid, auth_token)

    message = client.messages.create(
    body="Hello from JobSnatch Your interview date is scheduled kindly do the needful through your portal. Thank You :)",
    from_="+12096892318",
    to="+917306364976"
    )

    print(message.sid)
    return redirect('acceptedcan')

def interdate(request):
    if request.method == 'POST':
     canid= request.POST['canid']
     ca=User.objects.filter(id=canid)
     return render(request,'interdate.html',{'ca':ca,'can':canid})

def scheaccept(request):
    if request.method == 'POST':
        scheu=request.POST['scheu']
        accept=scheduling.objects.get(sche_id=scheu)
        accept.acc=True
        accept.save()
        return redirect('activity')

def schedec(request):
    if request.method == 'POST':
        scheu=request.POST['scheu']
        sc=request.POST['sc']
        tii=request.POST['tii']
        accept=scheduling.objects.get(sche_id=scheu)
        accept.dec=False
        accept.reason=sc
        accept.can_date=tii
        accept.save()
        return redirect('activity')

def sch(request):
    sche=request.POST['sche']
    return render(request,'schedec2.html',{'sche':sche})

def schedec2(request):
    if request.method == 'POST':
        sche=request.POST['sche']
        sc=request.POST['sc']
        tii=request.POST['tii']
        accept=scheduling.objects.get(sche_id=sche)
        accept.dec=False
        accept.reason=sc
        accept.can_date=tii
        accept.save()
        return redirect('activity')
    
def appr1(request):
    if request.method == 'POST':
        appr1=request.POST['appr1']
        accept=scheduling.objects.get(sche_id=appr1)
        accept.approvedd=True
        accept.save()
        return redirect('acceptedcan')

def setstatus(request):
    if request.method == 'POST':
        app=request.POST['app']
        accept=scheduling.objects.get(sche_id=app)
        accept.status=False
        accept.save()
        return redirect('acceptedcan')

def appr2(request):
    if request.method == 'POST':
        appr2=request.POST['appr2']
        accept=scheduling.objects.get(sche_id=appr2)
        accept.approvedd=True
        accept.save()
        return redirect('acceptedcan')
    
def progress(request):

  comp=job.objects.all()
    
  sc=scheduling.objects.filter(user_id_id=request.user.id,approvedd=True,train_date__gt=Now())
  return render(request,'progress.html',{'sc':sc,'comp':comp})


def notifi(request):
     if 'cmp' in request.session:
       
       testt=request.POST.get('test')
       ss=User.objects.filter(id=testt)
       sc=scheduling.objects.filter(com_id=request.user.id,acc=True)
       scc=scheduling.objects.filter(com_id=request.user.id,dec=False)
       return render(request,'notifications.html',{'sc':sc,'scc':scc,'ss':ss})

def compoffer (request):
    if 'cmp' in request.session:
        avl=User.objects.filter(is_candidate=True,cat=request.user.cat)
        return render(request,'compoffer.html',{'avl':avl})

def offercan (request):
    if 'cmp' in request.session:
         canid=request.POST['canid']
         data=User.objects.filter(id=canid)
         return render(request,'offercan.html',{'data':data})

def offerjob (request):
    if 'cmp' in request.session:
         canid=request.POST['canid']
         off=offerr(cann_id=canid)
         off.comm_id=request.user
         off.save()
         return redirect('compoffer')

def addcate(request):
    if 'usr' in request.session:
       return render(request,"addcat.html")
    return render(request,'index.html')
    # return render(request,'admin.html')

def addin(request):
    if 'usr' in request.session:
       ad=categ.objects.all()
       return render(request,"addin.html",{'ad':ad})
    return render(request,'index.html')

def interinfo(request):
    if 'can' in request.session:
       inid=request.POST.get('inid')
       data=internship.objects.filter(intern_id=inid)
       return render(request,"interinfo.html",{'data':data})
    return render(request,'index.html')
    
def inadd(request):
    if 'cmp' in request.session:
       return render(request,"inadd.html")
    return render(request,'index.html')

def idcard(request):
    if 'can' in request.session:
       
       return render(request,"idcard.html")
    return render(request,'index.html')

def pdf(request):
    buf=io.BytesIO()
    c= canvas.Canvas(buf, pagesize=letter, bottomup=0)
    textob= c.beginText()
    textob.setTextOrigin(inch, inch)
    textob.setFont("Helvetica", 14)
    lines = [
        "This is line 1",
        "This is line 2",
        "This is line 3",
        "This is line 4",
    ]

    for line in lines:
        textob.textLine(line)
    

    c.drawText(textob)
    c.showPage()
    c.save()
    buf.seek(0)
    return FileResponse(buf,as_attachment=True,filename='venue.pdf')

# def rating(request):
#     ab=request.POST['rate']
#     cd=feedback.objects.()
#     cd.
    

def wish(request):
    if 'can' in request.session:
        jid=request.POST['jid']
        cmpid=request.POST['cmpid']
        canid=request.POST['canid']
        member = wishlist(checkk=True,cann_id=canid,comm_id=cmpid,jobb_id=jid)
        member.save()
        return redirect('avljobs')

def wiish(request):
    if 'can' in request.session:
        data3 = job.objects.all()
        data3 = job.objects.filter(lastdate__gt=Now())
        data8 = wishlist.objects.filter(cann_id=request.user.id)
        
        return render(request,'widh.html',{'data3':data3,'data8':data8,})

    
razorpay_client = razorpay.Client(
    auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET))
 
 
def homepage(request):
    currency = 'INR'
    amount = 20000  # Rs. 200
 
    # Create a Razorpay Order
    razorpay_order = razorpay_client.order.create(dict(amount=amount,
                                                       currency=currency,
                                                       payment_capture='0'))
 
    # order id of newly created order.
    razorpay_order_id = razorpay_order['id']
    callback_url = 'paymenthandler/'
 
    # we need to pass these details to frontend.
    context = {}
    context['razorpay_order_id'] = razorpay_order_id
    context['razorpay_merchant_key'] = settings.RAZOR_KEY_ID
    context['razorpay_amount'] = amount
    context['currency'] = currency
    context['callback_url'] = callback_url
 
    return render(request, 'homepage.html', context=context)
 
 
# we need to csrf_exempt this url as
# POST request will be made by Razorpay
# and it won't have the csrf token.
@csrf_exempt
def paymenthandler(request):
 
    # only accept POST request.
    if request.method == "POST":
        try:
           
            # get the required parameters from post request.
            payment_id = request.POST.get('razorpay_payment_id', '')
            razorpay_order_id = request.POST.get('razorpay_order_id', '')
            signature = request.POST.get('razorpay_signature', '')
            params_dict = {
                'razorpay_order_id': razorpay_order_id,
                'razorpay_payment_id': payment_id,
                'razorpay_signature': signature
            }
 
            # verify the payment signature.
            result = razorpay_client.utility.verify_payment_signature(
                params_dict)
            if result is not None:
                amount = 20000  # Rs. 200
                try:
 
                    # capture the payemt
                    razorpay_client.payment.capture(payment_id, amount)
 
                    # render success page on successful caputre of payment
                    # return render(request, 'paymentsuccess.html')
                    return redirect('candidate')
                except:
 
                    # if there is an error while capturing payment.
                    return render(request, 'paymentfail.html')
            else:
 
                # if signature verification fails.
                return render(request, 'paymentfail.html')
        except:
 
            # if we don't find the required parameters in POST data
            return HttpResponseBadRequest()
    else:
       # if other than POST request is made.
        return HttpResponseBadRequest()
