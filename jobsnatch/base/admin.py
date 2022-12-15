from django.contrib import admin
from base.models import reg
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

class regInline(admin.StackedInline):
    model = reg
    can_delete = False
    verbose_name_plural = 'reg'

class customizeuser(UserAdmin):
    inlines = (regInline, )

admin.site.register(User)
#admin.site.register(User, customizeuser)
