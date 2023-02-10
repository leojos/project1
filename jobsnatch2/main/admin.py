from django.contrib import admin
from .models import User,job,appliedjob,feedback,categ,blog,internship,classdetails,scheduling,offerr

# Register your models here.
admin.site.register(User)
admin.site.register(job)
admin.site.register(appliedjob)
admin.site.register(feedback)
admin.site.register(categ)
admin.site.register(blog)
admin.site.register(internship)
admin.site.register(classdetails)
admin.site.register(scheduling)
admin.site.register(offerr)