from rest_framework import permissions

class  IsCreatedByOrReadOny(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        ## if you did: return True --> everyone has permission
        ## if you did: return False --> effectivly lock down the app
        # return obj.created_by == request.user

        ## allow anyone for a get request
        if request.method in permissions.SAFE_METHODS:
            return True
        print(obj.created_by==request.user)
        return obj.created_by == request.user
