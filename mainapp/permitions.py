from rest_framework import permissions
from .models import Enroll,Profile
class ISADMINORREADONLY(permissions.BasePermission):
    def has_permission(self, request,view):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return bool(request.user and request.user.is_staff)
class ISENrolled(permissions.BasePermission):
    def has_permission(self, request, view):
        course_id = view.kwargs.get('courses_pk')
        if not course_id:
            return False
        (student,created)=Profile.objects.get_or_create(user_id=request.user.id)
        return Enroll.objects.filter(course_id=course_id, student=student).exists()
