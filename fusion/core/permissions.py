from rest_framework import permissions


class EsuperUserPost(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method == 'POST':
            if request.user.is_super_user:
                return True
            return False
        return True


class EsuperUserPut(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method == 'PUT':
            if request.user.is_super_user:
                return True
            return False
        return True


class EsuperUserDelete(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method == 'DELETE':
            if request.user.is_super_user:
                return True
            return False
        return True
