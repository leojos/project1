from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name= 'index'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register, name='register'),
    path('admin', views.admin, name='admin'),
    path('candidate/', views.candidate, name='candidate'),
    path('company/', views.company, name='company'),
    path('jobpost/', views.jobpost, name='jobpost'),
    # path('/jobpost/comprofile', views.company, name='company'),
    path('avljobs', views.avljobs, name='avljobs'),
    path('appliedjobs', views.appliedjobs, name='appliedjobs'),
    path('avlcandidates', views.avlcandidates, name='avlcandidates'),
    path('candidate/updaterecord/<int:id>', views.updaterecord, name='updaterecord/<int:id>'),
    path('company/updatecom/<int:id>', views.updatecom, name='updatecom/<int:id>'),
    path('postjob', views.postjob, name='postjob'),
    path('comactivity', views.comactivity, name='comactivity'),
    path('authdelete', views.authdelete, name='authdelete'),
    path('jobelete', views.jobdelete, name='jobdelete'),
    path('applyjob', views.applyjob, name='applyjob'),

    path('reset_password/',
    auth_views.PasswordResetView.as_view(template_name ='password_reset.html'),
    name="reset_password"),

    path('reset_password_sent/',
    auth_views.PasswordResetDoneView.as_view(template_name ='password_reset_sent.html'),
    name='password_reset_done'),

    path('reset/<uidb64>/<token>/',
    auth_views.PasswordResetConfirmView.as_view(template_name ='password_reset_form.html'),
    name='password_reset_confirm'),

    path('reset_password_complete/',
    auth_views.PasswordResetCompleteView.as_view(template_name ='password_reset_done.html'),
    name='password_reset_complete')
]