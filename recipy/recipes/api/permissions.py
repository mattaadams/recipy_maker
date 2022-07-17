from rest_framework.permissions import BasePermission

# how to get obj keys
# example: obj default returns id, but want obj.ingredient.author
# if obj key == ingredient check obj.author = user, else check if obj.ingredient.author = user


class IsOwnerOrReadOnly(BasePermission):
    message = 'You must be the owner of this object.'

    def has_object_permission(self, request, view, obj):
        return obj.author == request.user


class IsParentOwnerOrReadOnly(BasePermission):
    message = 'You must be the owner of this object.'

    def has_object_permission(self, request, view, obj):
        return obj.recipe.author == request.user


class IsCommentOwnerOrReadOnly(BasePermission):
    message = 'You must be the owner of this object.'

    def has_object_permission(self, request, view, obj):
        return obj.author == request.user
