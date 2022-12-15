from django.contrib import admin
from .models import User,job,appliedjob

# Register your models here.
admin.site.register(User)
admin.site.register(job)
admin.site.register(appliedjob)
