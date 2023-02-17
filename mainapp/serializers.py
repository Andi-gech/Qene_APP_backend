from rest_framework import serializers
from django.shortcuts import get_object_or_404
from .models import Course,Profile,Course_details,Enroll,course_outlines,Quiz,Questions,Answer
from djoser.serializers import UserCreateSerializer as BaseUSercreateSerializer,UserSerializer as baseuserSerilizer

class CourseSerializer(serializers.ModelSerializer):
    Teacher=serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model=Course
        fields=['id','Course_name','Teacher','description']
    def save(self, **kwargs):
        (teacher,created)=Profile.objects.get_or_create(user_id=self.context['userid'])
        if teacher:
            self.validated_data['Teacher'] = teacher
        return super().save(**kwargs)
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=Profile
        fields=['id','user','role','profile_pic']

class CoursedetailSerializer(serializers.ModelSerializer):
    courseoutlinee=serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model=Course_details
        fields=['id','courseoutlinee','text_content','code_content','image_content']
    def save(self, **kwargs):
       
       courseoutline=get_object_or_404(course_outlines, id=self.context['courseoutlinee_id'])
       if courseoutline:
            self.validated_data['courseoutlinee'] = courseoutline
       return super().save(**kwargs)
class CourseOutlineSerializer(serializers.ModelSerializer):
    course=serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model=course_outlines
        fields=['course','course_module_name','date','id','is_completed']
    def save(self, **kwargs):
       
       course=get_object_or_404(Course, id=self.context['course_id'])
       if course:
            self.validated_data['course'] = course
       return super().save(**kwargs)
class EnrolSerializer(serializers.ModelSerializer):
    student=serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model=Enroll
        fields=['id','course','student']
    def save(self, **kwargs):
        (student,created)=Profile.objects.get_or_create(user_id=self.context['userid'])
        if student:
            self.validated_data['student'] = student
        return super().save(**kwargs)
class QuizSerializer(serializers.ModelSerializer):
     courseoutlines=serializers.PrimaryKeyRelatedField(read_only=True)
     class Meta:
        model=Quiz
        fields=['id','courseoutlines','date']
     def save(self, **kwargs):
       courseoutline=get_object_or_404(course_outlines, id=self.context['courseoutlines_id'])
       if courseoutline:
            self.validated_data['courseoutlines'] = courseoutline
       return super().save(**kwargs)
class QuestionSERializer(serializers.ModelSerializer):
    quiz=serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model=Questions
        fields=['id','quiz','text','code','weight']
    def save(self, **kwargs):
       quiz=get_object_or_404(Quiz, id=self.context['quiz_id'])
       if quiz:
            self.validated_data['quiz'] = quiz
       return super().save(**kwargs)
class AnswerSerilizer(serializers.ModelSerializer):
    question=serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model=Answer
        fields=['id','question','choice_text','is_correct']
    def save(self, **kwargs):
       question=get_object_or_404(Questions, id=self.context['question_id'])
       if question:
            self.validated_data['question'] = question
       return super().save(**kwargs)
    

   
class UserCreateSerializer(BaseUSercreateSerializer):
    class Meta(BaseUSercreateSerializer.Meta):
        fields=['id','username','password','email','first_name','last_name']
class UserSerializer(baseuserSerilizer):
    class Meta(baseuserSerilizer.Meta):
        fields=['id','username','email','first_name','last_name']

