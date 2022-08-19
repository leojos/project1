from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path("register", views.register, name='register'),
    path("login", views.login, name='login'),
    path("canprofile", views.canprofile, name='canprofile'),
    path("logout", views.logout, name='logout'),
    path('updaterecord/<int:id>', views.updaterecord, name='updaterecord'),
    path("avljobs", views.avljobs, name='avljobs'),
    path("appljobs", views.appljobs, name='appljobs'),
    path("canactivity", views.canactivity, name='canactivity'),
    path("apptitude", views.apptitude, name='apptitude'),
    path("gd", views.gd, name='gd'),
    path("interview", views.interview, name='interview'),
    path("admin", views.admin, name='admin'),
    path("adregister", views.adregister, name='adregister'),
    path("authdelete", views.authdelete, name='authdelete'),
    path("jobpost", views.jobpost, name='jobpost'),
    path("avlcandidates", views.avlcandidates, name='avlcandidates'),
    path("comprofile", views.comprofile, name='comprofile'),
    path("comactivity", views.comactivity, name='comactivity'),
    # path("showusername", views.showusername, name='showusername'),
]