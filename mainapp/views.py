from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from rest_framework.permissions import IsAuthenticated
from .models import Profile
from rest_framework.mixins import CreateModelMixin,RetrieveModelMixin,UpdateModelMixin
from rest_framework.decorators import action
from rest_framework.response import Response

from .pagination import defaultPagination
from rest_framework.filters import SearchFilter,OrderingFilter
from .models import Course,Enroll,course_outlines,Course_details,Quiz,Questions,Answer
from rest_framework.viewsets import ModelViewSet,GenericViewSet
from .permitions import ISADMINORREADONLY,ISENrolled
from .serializers import CourseSerializer,EnrolSerializer,CourseOutlineSerializer,CoursedetailSerializer,QuizSerializer,QuestionSERializer,AnswerSerilizer,ProfileSerializer
# Create your views here.
class CourseVIewSet(ModelViewSet):
    queryset=Course.objects.all()
    serializer_class=CourseSerializer
    filter_backends=[SearchFilter,OrderingFilter]
    pagination_class=defaultPagination
    search_fields=['Course_name','description']
    ordering_fields=['Course_name']
    permission_classes=[ISADMINORREADONLY]

    


class MyCourseViewSet(ModelViewSet):
    permission_classes=[IsAuthenticated]
    def get_queryset(self):
        (student,created)=Profile.objects.get_or_create(user_id=self.request.user.id)
        print(self.request.user.id)
        return Enroll.objects.filter(student=student)
   
    serializer_class=EnrolSerializer
    def get_serializer_context(self):
        return {
            'userid':self.request.user.id
        }

class CourseOutlineViewSet(ModelViewSet):
    permission_classes=[IsAuthenticated,ISADMINORREADONLY,ISENrolled]

    def get_queryset(self):
       
        return course_outlines.objects.filter(course=self.kwargs['courses_pk'])
    
    serializer_class=CourseOutlineSerializer
    def get_serializer_context(self):
        return {
            'course_id':self.kwargs['courses_pk']
        }

class CourseDetailViewset(ModelViewSet):
    permission_classes=[IsAuthenticated,ISADMINORREADONLY]
    def get_queryset(self):
       
        return Course_details.objects.filter(courseoutlinee_id=self.kwargs['outline_pk'])
    
    serializer_class=CoursedetailSerializer
    def get_serializer_context(self):
        return {
            'courseoutlinee_id':self.kwargs['outline_pk']
        }
    


class QuizVIewSet(ModelViewSet):
    permission_classes=[IsAuthenticated,ISADMINORREADONLY]
    def get_queryset(self):
        return Quiz.objects.filter( courseoutlines_id=self.kwargs['outline_pk'])
    serializer_class=QuizSerializer
    def get_serializer_context(self):
        return {
            'courseoutlines_id':self.kwargs['outline_pk']
        }
class QuestionsViewSet(ModelViewSet):
    permission_classes=[IsAuthenticated,ISADMINORREADONLY]
    def get_queryset(self):
        return Questions.objects.filter(quiz_id=self.kwargs['quize_pk'])
    serializer_class=QuestionSERializer
    def get_serializer_context(self):
        return {
            'quiz_id':self.kwargs['quize_pk']
        }

class AnswerViewSet(ModelViewSet):
    permission_classes=[IsAuthenticated,ISADMINORREADONLY]
    def get_queryset(self):
        return Answer.objects.filter(question_id=self.kwargs['question_pk'])
    serializer_class=AnswerSerilizer
    def get_serializer_context(self):
        return {
            'question_id':self.kwargs['question_pk']
        }
class ProfileViewSet(CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,GenericViewSet):
    permission_classes=[IsAuthenticated]
    queryset=Profile.objects.all()
    serializer_class=ProfileSerializer
    @action(detail=False,methods=['GET','PUT'])
    def me(self ,request):
        (profile,created)=Profile.objects.get_or_create(user_id=request.user.id)
        if request.method =='GET':
            serilizer=ProfileSerializer(profile)
            return Response(serilizer.data)
        elif request.method=='PUT':
            serilizer=ProfileSerializer(profile,data=request.data)
            serilizer.is_valid(raise_exception=True)
            serilizer.save()
            return Response(serilizer.data)
        


