from django.contrib import admin
from home.models import Recipe,Department,StudentId,Student

# Register your models here.
admin.site.register(Recipe)
admin.site.register(Department)
admin.site.register(StudentId)
admin.site.register(Student)