from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

UserAdmin.list_display += ('area','puesto')

UserAdmin.fieldsets += (('General',{'fields':('area','puesto'),}),)

admin.site.register(User, UserAdmin)
