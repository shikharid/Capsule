from rest_framework.permissions import BasePermission
from problems.models import Assignment


class IsStudent(BasePermission):

    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated() and not request.user.is_faculty


class IsFaculty(BasePermission):

    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated() and request.user.is_faculty


class IsOwner(BasePermission):

    def has_permission(self, request, view):

        assignment_id = view.kwargs.get('assignment_id', None)
        try:
            Assignment.objects.get(id=assignment_id, faculty_id=request.user)
            return request.user and request.user.is_authenticated() and request.user.is_faculty
        except Assignment.DoesNotExist:
            return False