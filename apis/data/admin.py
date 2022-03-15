from django.contrib import admin
from .models import *
# Register your models here.
admin.site.site_header = "product details"
admin.site.register(Company)
admin.site.register(ProductSize)
admin.site.register(Category)

