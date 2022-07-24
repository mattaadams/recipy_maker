from rest_framework import serializers
from django.contrib.auth.models import User
from recipes.models import Recipe


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username',
            'password',
            'email',
        ]


class UserListSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'favorites'
        ]


class UserDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'favorites'
        ]


class UserFavoriteRecipeListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Recipe
        fields = ['title', 'favorites']
