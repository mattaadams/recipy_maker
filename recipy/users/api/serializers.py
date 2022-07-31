from rest_framework import serializers
from django.contrib.auth.models import User
from recipes.models import Comment
from django.core.exceptions import ValidationError
from django.db.models import Q
from recipes.api.serializers import RecipeListSerializer


class UserCreateSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(label="Email Address")
    email2 = serializers.EmailField(label="Confirm Email")

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'email2',
            'password',
        ]
        extra_kwargs = {"password":
                        {"write_only": True}
                        }

    def validate_email2(self, value):
        data = self.get_initial()
        email1 = data.get('email')
        email2 = value
        if email1 != email2:
            raise ValidationError('Emails must match')
        user_qs = User.objects.filter(email=email2)
        if user_qs.exists():
            raise ValidationError("This user has already registered.")

        return value

    def create(self, validated_data):
        username = validated_data['username']
        email = validated_data['email']
        password = validated_data['password']
        user_obj = User(
            username=username,
            email=email,
        )
        user_obj.set_password(password)
        user_obj.save()
        return validated_data


class UserLoginSerializer(serializers.ModelSerializer):
    token = serializers.CharField(allow_blank=True, read_only=True)
    username = serializers.CharField(required=False, allow_blank=True)
    email = serializers.EmailField(label="Email Address", required=False, allow_blank=True)

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
            'token'
        ]
        extra_kwargs = {"password":
                        {"write_only": True}
                        }

    def validate(self, data):
        user_obj = None
        email = data.get("email", None)
        username = data.get("username", None)
        password = data["password"]
        if not email and not username:
            raise ValidationError("A username or email is required to login.")

        user = User.objects.filter(
            Q(email=email) |
            Q(username=username)
        ).distinct()

        if user.exists() and user.count() == 1:
            user_obj = user.first()
        else:
            raise ValidationError("This username/email is not valid.")

        if user_obj:
            if not user_obj.check_password(password):
                raise ValidationError("Incorrect credentials, please try again.")

        data["token"] = "Some Random Token"

        return data


class UserListSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'favorites'
        ]


class UserCommentListSerializer(serializers.ModelSerializer):
    recipe_title = serializers.CharField(source="recipe.title", read_only=True)

    class Meta:

        model = Comment
        fields = [
            'id',
            'body',
            'recipe',
            'recipe_title'
        ]


class UserDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'favorites',
            'date_joined',
            'is_active',
        ]
