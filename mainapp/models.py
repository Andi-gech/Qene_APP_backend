from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    ROLE = [
        ('admin', 'Admin'),
        ('student', 'Student'),
        ('teacher', 'Teacher'),
    ]
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic=models.TextField()
    role = models.CharField(
        max_length=10,
        choices=ROLE,
        default='student',
    )
    def __str__(self) :
        return self.user.username

class Course(models.Model):
    Course_name=models.CharField(max_length=255)
    Teacher=models.ForeignKey(Profile,on_delete=models.CASCADE)
    description=models.TextField()
    def __str__(self) :
        return self.Course_name

class Enroll(models.Model):
    student=models.ForeignKey(Profile,on_delete=models.CASCADE)
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    date_enrolled=models.DateTimeField(auto_now=True)
    class Meta:
        unique_together = ('student', 'course')
    def __str__(self) :
        return self.course.Course_name
class course_outlines(models.Model):
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    course_module_name=models.CharField(max_length=255)
    date=models.DateTimeField(auto_now=True)
    is_completed=models.BooleanField(default=False)
    def __str__(self) :
        return self.course_module_name
class Course_details(models.Model):
    date_created=models.DateTimeField(auto_now=True)
    courseoutlinee=models.ForeignKey(course_outlines, on_delete=models.CASCADE)
    text_content=models.TextField(null=True)
    code_content=models.TextField(null=True)
    image_content=models.TextField(null=True)
    def __str__(self) :
        return self.text_content


class Quiz(models.Model):
    courseoutlines=models.ForeignKey(course_outlines,on_delete=models.CASCADE)
    date=models.DateTimeField(auto_now=True)
class Questions(models.Model):
    quiz=models.ForeignKey(Quiz,on_delete=models.CASCADE)
    text=models.TextField(null=True)
    code=models.TextField(null=True)
    weight=models.PositiveIntegerField()
    def __str__(self) :
        return self.text


class Answer(models.Model):
    question=models.ForeignKey(Questions,on_delete=models.CASCADE)
    choice_text=models.TextField()
    is_correct=models.BooleanField(default='false')

    def __str__(self) :
        return self.choice_text



    



