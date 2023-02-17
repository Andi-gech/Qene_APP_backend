from rest_framework import permissions
from .models import Enroll,Profile,Course
class ISADMINORREADONLY(permissions.BasePermission):
    def has_permission(self, request,view):
        course_id = view.kwargs.get('pk')
        if request.method in permissions.SAFE_METHODS:
            return True
        elif request.method =='POST':
            return bool(request.user and request.user.is_staff)
        else :
            if request.user.is_staff:
                (teacher,created)=Profile.objects.get_or_create(user_id=request.user.id)
             
                return Course.objects.filter(id=course_id ,Teacher=teacher ).exists()

           
class ISENrolled(permissions.BasePermission):
    def has_permission(self, request, view):
        course_id = view.kwargs.get('courses_pk')
        (student,created)=Profile.objects.get_or_create(user_id=request.user.id)
        if request.user.is_staff:
            return Course.objects.filter(id=course_id ,Teacher=student ).exists()
        else :
            if not course_id:
                return False
            return Enroll.objects.filter(course_id=course_id, student=student).exists()
class ISMYcourse(permissions.BasePermission):
    def has_permission(self, request, view):
        not_staff=not request.user.is_staff
        return not_staff

