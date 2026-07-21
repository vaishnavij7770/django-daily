from django.contrib import admin
from .models import student, teacher, emp, users, heroes, members
# Register your models here.

admin.site.register([student,teacher,emp,users,heroes,members])

