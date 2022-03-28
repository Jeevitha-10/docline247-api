from django.contrib import admin
from .models import Category, User, Doctor
# Register your models here.
admin.site.register(Category)
admin.site.register(User)
admin.site.register(Doctor)
