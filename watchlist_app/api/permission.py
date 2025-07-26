from rest_framework import permissions

class IsReviewerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow reviewers to edit their reviews.
    """
    
    def has_object_permission(self, request, view, obj):
        # Allow read-only access for all users
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # Allow write access only for the reviewer
        # return request.user and request.user.is_authenticated and request.user == view.get_object().reviewer
        return obj.reviewer == request.user 