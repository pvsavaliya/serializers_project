from django.contrib import admin
from apis.account.models import *
# Register your models here.

admin.site.register(UserDetail)
admin.site.register(EmailOTP)
admin.site.register(Comment)
admin.site.register(tag)