from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name= 'index'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register, name='register'),
    path('admin', views.admin, name='admin'),
    path('candidate', views.candidate, name='candidate'),
    path('company/', views.company, name='company'),
    path('jobpost/', views.jobpost, name='jobpost'),
    # path('/jobpost/comprofile', views.company, name='company'),
    path('avljobs', views.avljobs, name='avljobs'),
    path('appliedjobs', views.appliedjobs, name='appliedjobs'),
    path('avlcandidates', views.avlcandidates, name='avlcandidates'),
    path('updaterecord/<int:id>', views.updaterecord, name='updaterecord/<int:id>'),
    path('company/updatecom/<int:id>', views.updatecom, name='updatecom/<int:id>'),
    path('company/updateco/<int:id>', views.updateco, name='updateco/<int:id>'),
    path('company/updatec/<int:id>', views.updatec, name='updatec/<int:id>'),
    path('updatecan/<int:id>', views.updatecan, name='updatecan/<int:id>'),
    path('postjob', views.postjob, name='postjob'),
    # path('company/comactivity/<int:id>', views.comactivity, name='comactivity/<int:id>'),
    path('authdeletecom', views.authdeletecom, name='authdeletecom'),
    path('authdeletecan', views.authdeletecan, name='authdeletecan'),
    # path('jobelete', views.jobdelete, name='jobdelete'),
    path('applyjob', views.applyjob, name='applyjob'),
    path('comppage', views.comppage, name='comppage'),
    path('comppages', views.comppages, name='comppages'),
    path('canpage', views.canpage, name='canpage'),
    path('comaccept', views.comaccept, name='comaccept'),
    path('comreject', views.comreject, name='comreject'),
    path('acceptedcan', views.acceptedcan, name='acceptedcan'),
    path('acceptedcom', views.acceptedcom, name='acceptedcom'),
    path('admincom', views.admincom, name='admincom'),
    path('admincan', views.admincan, name='admincan'),
    path('adminapprove', views.adminapprove, name='adminapprove'),
    path('aptitude', views.aptitude, name='aptitude'),
    path('gd', views.gd, name='gd'),
    path('interview', views.interview, name='interview'),
    path('my_form', views.my_form, name='my_form'),
    path('my_post', views.my_post, name='my_post'),
    path('anf', views.anf, name='anf'),
    path('pnt', views.pnt, name='pnt'),
    path('dna', views.dna, name='dna'),
    path('wnt', views.wnt, name='wnt'),
    path('ent', views.ent, name='ent'),
    path('rnf', views.rnf, name='rnf'),
    path('dnm', views.dnm, name='dnm'),
    path('snm', views.snm, name='snm'),
    path('resume', views.resume, name='resume'),
    path('blogpost', views.blogpost, name='blogpost'),
    path('resum', views.resum, name='resum'),
    path('appti', views.appti, name='appti'),
    path('convince', views.convince, name='convince'),
    path('blogg', views.blogg, name='blogg'),
    path('feedbacks', views.feedbacks, name='feedbacks'),
    path('moreblogs', views.moreblogs, name='moreblogs'),
    path('fullblog', views.fullblog, name='fullblog'),
    path('graph', views.graph, name='graph'),
    path('adminnew', views.adminnew, name='adminnew'),
    path('addcat', views.addcat, name='addcat'),
    path('intern', views.intern, name='intern'),
    path('moreinterns/<int:id>', views.moreinterns, name='moreinterns/<int:id>'),
    path('interndetails/<int:id>', views.interndetails, name='interndetails/<int:id>'),
    path('classdetail', views.classdetail, name='classdetail'),
    path('train', views.train, name='train'),
    path('activity', views.activity, name='activity'),
    path('map', views.map, name='map'),
    path('setdate', views.setdate, name='setdate'),
    path('res', views.res, name='res'),
    path('resdetails', views.resdetails, name='resdetails'),
    path('resubmit', views.resubmit, name='resubmit'),
    path('sche', views.sche, name='sche'),
    path('interdate', views.interdate, name='interdate'),
    path('scheaccept', views.scheaccept, name='scheaccept'),
    path('schedec', views.schedec, name='schedec'),
    path('notifi/<int:id>', views.notifi, name='notifi/<int:id>'),
    # path("createresume", views.createresume, name="createresume"),
    # path("resumes", views.resumes, name="resumes"),
    # path("dash", views.dash, name="dash"),
    
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