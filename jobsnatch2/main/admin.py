from django.contrib import admin
from .models import User,job,appliedjob,feedback,categ

# Register your models here.
admin.site.register(User)
admin.site.register(job)
admin.site.register(appliedjob)
admin.site.register(feedback)
admin.site.register(categ)
