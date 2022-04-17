from django.contrib import admin
from .models import Student, User

# Register your models here.
admin.site.register(User)
admin.site.register(Student)