from django.shortcuts import render
# from .forms import SignUpForm, LoginForm

# Create your views here.
def index(request):
    return render(request, 'index.html')
    


def register(request):
    return render(request, 'register.html')
    # msg = None
    # if request.method == 'POST':
    #     form = SignUpForm(request.POST)
    #     if form.is_valid():
    #         user = form.save()
    #         msg = 'user created'
    #         return redirect('login')
    #     else:
    #         msg = 'form is not valid'
    # else:
    #     form = SignUpForm()
    # return render(request,'register.html', {'form': form, 'msg': msg})


def login(request):
    return render(request, 'login.html')
    # form = LoginForm(request.POST or None)
    # msg = None
    # if request.method == 'POST':
    #     if form.is_valid():
    #         username = form.cleaned_data.get('username')
    #         password = form.cleaned_data.get('password')
    #         user = authenticate(username=username, password=password)
    #         if user is not None and user.is_admin:
    #             request.session['usr']=user.username
    #             auth.login(request, user)
    #             #login(request, user)
    #             return redirect('admin')
    #         elif user is not None and user.is_candidate:
    #             request.session['can']=user.username
    #             auth.login(request, user)
    #             #login(request, user)
    #             return redirect('candidate')
    #         elif user is not None and user.is_company:
    #             request.session['cmp']=user.username
    #             auth.login(request, user)
    #             #login(request, user)
    #             return redirect('company')
    #         else:
    #             msg= 'invalid credentials'
    #     else:
    #         msg = 'error validating form'
    # return render(request, 'login.html', {'form': form, 'msg': msg})