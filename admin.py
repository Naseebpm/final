from django.contrib import admin
from .models import *
from django.contrib.auth.models import User

# Register your models here.
# admin.site.register(models.Groups)

admin.site.register(Students)
admin.site.register(Books)
admin.site.register(Borrow)
admin.site.register(Category)
admin.site.register(SubCategory)



