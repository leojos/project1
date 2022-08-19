from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages 
# from base.models import displayusername

def index(request):
    return render(request,'index.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['name']
        email = request.POST['email']
        password1 = request.POST['p1']
        password2 = request.POST['p2']
        if password1==password2 :
             if User.objects.filter(username=username).exists():
                messages.info(request,'Username Taken')
                return redirect('/')
             elif User.objects.filter(email=email).exists():
                messages.info(request,'Email Taken')
                return redirect('/')
             else:
                user=User.objects.create_user(username=username,first_name=first_name,email=email,password=password1)
                user.save()
                messages.info(request,'user created')
                return redirect('/')
        else:
             messages.info(request,'Password not matching')
             return redirect('/')
    else:
        return render(request,'index.html')

def login(request):
    if 'username' in request.session:
      return redirect('canprofile')
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            if username=="admin":
                request.session['username'] = username
                auth.login(request, user)
                return redirect('admin')
            else:
                request.session['username'] = username
                auth.login(request, user)
                return redirect('canprofile')
        else:
                messages.info(request,'Invalid Credentials')
                return redirect('/')
    return render(request,'index.html')

def canprofile(request):
    if 'username' in request.session:
      return render(request,'canprofile.html')
    return render(request,'index.html')

def logout(request):
    if 'username' in request.session:
        request.session.flush()
        #auth.logout(request)
    return redirect('login')

def updaterecord(request, id):
  first_name = request.POST['name']
  email = request.POST['email']
  password = request.POST['password']
  user = User.objects.get(id=id)
  user.first_name = first_name
  user.email = email
  user.password = password
  user.save()
  return redirect('canprofile')

def avljobs(request):
    if 'username' in request.session:
      return render(request,'avljobs.html')
    return render(request,'index.html')

def appljobs(request):
    if 'username' in request.session:
      return render(request,'appljobs.html')
    return render(request,'index.html')

def canactivity(request):
    if 'username' in request.session:
      return render(request,'canactivity.html')
    return render(request,'index.html')

def apptitude(request):
    if 'username' in request.session:
      return render(request,'apptitude.html')
    return render(request,'index.html')

def gd(request):
    if 'username' in request.session:
      return render(request,'gd.html')
    return render(request,'index.html')

def interview(request):
    if 'username' in request.session:
      return render(request,'interview.html')
    return render(request,'index.html')

def admin(request):
    if 'username' in request.session:
      return render(request,'admin.html')
    return render(request,'index.html')

def adregister(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['name']
        email = request.POST['email']
        password1 = request.POST['p1']
        password2 = request.POST['p2']
        if password1==password2 :
             if User.objects.filter(username=username).exists():
                messages.info(request,'Username Taken')
                return redirect('admin')
             elif User.objects.filter(email=email).exists():
                messages.info(request,'Email Taken')
                return redirect('admin')
             else:
                user=User.objects.create_user(username=username,first_name=first_name,email=email,password=password1)
                user.save()
                messages.info(request,'user created')
                return redirect('admin')
        else:
             messages.info(request,'Password not matching')
             return redirect('admin')
    else:
        return render(request,'index.html')


def authdelete(request):
  username = request.POST['username']
  member = User.objects.get(username=username)
  member.delete()
  return redirect('admin')

def jobpost(request):
  # username = request.POST['username']
  return render(request,'jobpost.html')

def avlcandidates(request):
  # username = request.POST['username']
  return render(request,'avlcandidates.html')

def comprofile(request):
  return render(request,'comprofile.html')

def comactivity(request):
    # if 'username' in request.session:
    return render(request,'comactivity.html')
# def showusername(request):
#   displayname=User.objects.all()
#   return redirect('admin',{'displayusername':displayname})