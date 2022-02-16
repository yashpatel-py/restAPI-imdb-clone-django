from tkinter.tix import Tree
from rest_framework import permissions

class IsAdminOrReadOnly(permissions.IsAdminUser):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS: # If not admin then show only data
            return True
        else:
            return bool(request.user and request.user.is_staff) # If admin then allow to edit ot delete data

class IsReviewUserOrReadOnly(permissions.BasePermission):
    '''
    This class is made for the review_creater
    
    Which means the user who have created the review can edit else can only see the reviews
    '''
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            '''
                This will check permissions for readonly request
            '''
            return True
        else:
            '''
            Else it will check permissions for write request

            -->  else part will compare the review user and loggedin user and if both are equal then it will give permission to PUT, DELETE
            '''
            return obj.review_user == request.user