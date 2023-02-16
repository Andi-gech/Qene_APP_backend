from django.contrib import admin
from .models import Profile,Course,Enroll,Course_details,Quiz,Questions,Answer,course_outlines

# Register your models here.
admin.site.register(Profile)
admin.site.register(Course)
admin.site.register(Enroll)
admin.site.register(Course_details)
admin.site.register(Quiz)
admin.site.register(Questions)
admin.site.register(Answer)
admin.site.register(course_outlines)