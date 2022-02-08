from tkinter.tix import Tree
from rest_framework import permissions

class AdminOrReadOnly(permissions.IsAdminUser):
    def has_permission(self, request, view):
        '''
        If we don't add request.method == "GET" then admin can only see the data and edit the data
        AND
        If we add request.method == "GET" the any user can see the data but can't edit the data only admin can edit
        '''
        return request.method == "GET" or bool(request.user and request.user.is_staff)

class ReviewUserOrReadOnly(permissions.BasePermission):
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