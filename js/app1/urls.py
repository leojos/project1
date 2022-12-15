from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name= 'index'),
    path('login/', views.login, name='login'),
    # path('logout/', views.logout, name='logout'),
    path('register/', views.register, name='register'),
    # path('admin', views.admin, name='admin'),
    # path('candidate/', views.candidate, name='candidate'),
    # path('company/', views.company, name='company'),
    # path('jobpost/', views.jobpost, name='jobpost'),
    # # path('/jobpost/comprofile', views.company, name='company'),
    # path('avljobs', views.avljobs, name='avljobs'),
    # path('candidate/updaterecord/<int:id>', views.updaterecord, name='updaterecord/<int:id>'),
    # path('company/updatecom/<int:id>', views.updatecom, name='updatecom/<int:id>'),
    # path('postjob', views.postjob, name='postjob'),
    # path('comactivity', views.comactivity, name='comactivity'),
    # path('authdelete', views.authdelete, name='authdelete'),
]