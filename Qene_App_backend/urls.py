"""Qene_App_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include
from django.urls import path
from mainapp import views
from rest_framework.routers import SimpleRouter
from rest_framework_nested import routers
from django.conf import settings
from django.conf.urls.static import static
router=routers.DefaultRouter()
router.register('courses',views.CourseVIewSet)

router.register('mycourse',views.MyCourseViewSet,basename='mycourse')
router.register('profile',views.ProfileViewSet,basename='profile')

courses_router=routers.NestedSimpleRouter(router,'courses',lookup='courses')
courses_router.register('outline',views.CourseOutlineViewSet,basename='outline')
course_Detail_router=routers.NestedSimpleRouter(courses_router,'outline',lookup='outline')
course_Detail_router.register('contents',views.CourseDetailViewset,basename='contents')
course_quiz_router=routers.NestedSimpleRouter(courses_router,'outline',lookup='outline')
course_quiz_router.register('quize',views.QuizVIewSet,'quiz')
quiz_questions_router=routers.NestedSimpleRouter(course_quiz_router,'quize',lookup='quize')
quiz_questions_router.register('question',views.QuestionsViewSet,'question')
question_answer_router=routers.NestedSimpleRouter(quiz_questions_router,'question',lookup='question')
question_answer_router.register('answer',views.AnswerViewSet,'answer')



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
     path('', include(courses_router.urls)),
     path('',include(course_Detail_router.urls)),
     path('',include(course_quiz_router.urls)),
     path('',include(quiz_questions_router.urls)),
     path('',include(question_answer_router.urls)),
     path('auth/', include('djoser.urls')),
     path('auth/', include('djoser.urls.jwt')),
  

    
    
    
    

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
