from django.shortcuts import render, redirect
from .forms import SignUpForm, LoginForm
from django.contrib.auth import authenticate, login
from django.contrib import auth
from django.contrib import messages
from .models import User
from .models import job
from .models import appliedjob
from django.contrib.auth.decorators import login_required
from django import forms
# from django.shortcuts import render_to_response
# Create your views here.


def index(request):
    return render(request, 'index.html')


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
       data = User.objects.all()
       data = User.objects.filter(status=False)
       context = {'data': data}
       return render(request,"admin.html", context)
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
       if request.method == 'POST':
        st=request.POST['text']
        num=request.POST['number']
        if st!=None and num!=None:
          data = job.objects.filter(salary=num , job_title=st)
          # data = job.objects.filter(job_title=st)
       context = {'data': data}
       return render(request,"avljobs.html", context)
     return render(request,'index.html')

def appliedjobs(request):
     if 'can' in request.session:
       data = appliedjob.objects.all()
       data = appliedjob.objects.filter(status=True)
      #  user=User.objects.all()
      #  user=User.objects.filter(id=appliedjob.can_id_id)
      #  data = appliedjob.objects.filter(User.id==User.id)
       context = {'data': data}
       return render(request,"appliedjobs.html",context)
     return render(request,'index.html')
    # return render(request,'company.html')

def jobpost(request):
   if 'cmp' in request.session:
      return render(request,'jobpost.html')
   return render(request,'index.html')

def logout(request):
    auth.logout(request)
    return redirect('index')

def updaterecord(request, id):
 if 'can' in request.session:
  if request.method == 'POST':
    username = request.POST['username']
    email = request.POST['email']
    about = request.POST['about']
    image = request.FILES.get('avatar')
  #   password = request.POST['password']
    user = User.objects.get(id=id)
    user.username = username
    user.email = email
    user.about = about
    
    user.image = image
  #   user.password = password
    user.save()
    return redirect('candidate')

def updatecom(request, id):
   if 'cmp' in request.session:
      username = request.POST['username']
      email = request.POST['email']
      about = request.POST['about']
      image = request.FILES.get('img')
    #   password = request.POST['password']
      user = User.objects.get(id=id)
      user.username = username
      user.email = email
      user.about = about
      user.image = image
    #   user.password = password
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
        member = job(job_title=job_title,salary=salary,experience=experience,lastdate=lastdate,vacancies=vacancies,job_description=job_description)
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

def comactivity(request):
    if 'cmp' in request.session:
      #  user = User.objects.all()
       data = job.objects.all()
      #  data = job.objects.get(cmp_id_id=User.id)
       context = {'data': data}
       return render(request,"comactivity.html", context)
    return render(request,'index.html')
    # return render(request,'company.html')

def authdelete(request):
  username = request.POST['username']
  member = User.objects.get(username=username)
  member.status=True
  member.save()
  return redirect('admin')

def jobdelete(request):
  if 'can' in request.session:
    jobid = request.POST['jobid']
    member = appliedjob.objects.get(jobs_id_id=jobid)
    member.status=False
    member.save()
    return redirect('appliedjobs')

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
       data = appliedjob.objects.all()
       user=User.objects.all()
      #  user=User.objects.filter(id=appliedjob.can_id_id)
      #  data = appliedjob.objects.filter(User.id==User.id)
       context = {'data': data}
       return render(request,"avlcandidates.html",context)
    return render(request,'index.html')
    # return render(request,'company.html')