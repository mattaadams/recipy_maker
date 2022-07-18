from rest_framework import serializers
from recipes.models import Recipe, Ingredient, Comment


class IngredientListSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source="recipe.author", read_only=True)

    class Meta:
        model = Ingredient
        fields = [
            'id',
            'name',
            'recipe',
            'author'

        ]


class IngredientCreateUpdateSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False, write_only=False)
    recipe_title = serializers.CharField(source="recipe.title", read_only=True)
    author = serializers.CharField(source="recipe.author", read_only=True)
    recipe = serializers.IntegerField(source="recipe.id", read_only=True)

    class Meta:
        model = Ingredient
        fields = [
            'id',
            'name',
            'recipe',
            'recipe_title',
            'author'

        ]


class IngredientDetailSerializer(serializers.ModelSerializer):
    recipe_title = serializers.CharField(source="recipe.title", read_only=True)
    author = serializers.CharField(source="recipe.author", read_only=True)

    class Meta:
        model = Ingredient
        fields = [
            'id',
            'name',
            'recipe',
            'recipe_title',
            'author'
        ]


class RecipeListSerializer(serializers.ModelSerializer):
    ingredients = IngredientListSerializer(many=True, read_only=True)
    author = serializers.CharField(read_only=True)

    class Meta:

        model = Recipe
        fields = [
            'id',
            'author',
            'title',
            'description',
            'ingredients',
            'instructions',
            'date_posted'
        ]


class RecipeCreateUpdateSerializer(serializers.ModelSerializer):
    ingredients = IngredientCreateUpdateSerializer(many=True)
    author = serializers.CharField(read_only=True)
    image_url = serializers.URLField(allow_blank=True, default=None)

    class Meta:

        model = Recipe
        fields = [
            'id',
            'author',
            'title',
            'image_url',
            'description',
            'ingredients',
            'instructions',
        ]

    def create(self, validated_data):
        ingredients_data = validated_data.pop('ingredients')
        recipe = Recipe.objects.create(**validated_data)
        for ingredient_data in ingredients_data:
            Ingredient.objects.create(recipe=recipe, **ingredient_data)
        return recipe

    def update(self, instance, validated_data):
        ingredient_data = validated_data.pop("ingredients")

        remove_items = {item.id: item for item in instance.ingredients.all()}

        for item in ingredient_data:
            item_id = item.get("id", None)

            if item_id is None:
                # new item so create this
                instance.ingredients.create(**item)
            elif remove_items.get(item_id, None) is not None:
                # update this item
                instance_item = remove_items.pop(item_id)
                Ingredient.objects.filter(id=instance_item.id).update(**item)

        for item in remove_items.values():
            item.delete()

        for field in validated_data:
            setattr(instance, field, validated_data.get(field, getattr(instance, field)))
        instance.save()

        return instance


class RecipeDetailSerializer(serializers.ModelSerializer):
    ingredients = IngredientListSerializer(many=True, read_only=True)
    author = serializers.CharField(read_only=True)

    class Meta:

        model = Recipe
        fields = [
            'id',
            'author',
            'title',
            'description',
            'ingredients',
            'instructions',
            'date_posted'
        ]


class CommentListSerializer(serializers.ModelSerializer):
    author = serializers.CharField(read_only=True)

    class Meta:

        model = Comment
        fields = [
            'id',
            'author',
            'body',
            'date_posted',
            'recipe'
        ]


class CommentCreateUpdateSerializer(serializers.ModelSerializer):
    author = serializers.CharField(read_only=True)

    class Meta:

        model = Comment
        fields = [
            'id',
            'author',
            'body',
            'recipe'
        ]


class CommentDetailSerializer(serializers.ModelSerializer):
    author = serializers.CharField(read_only=True)

    class Meta:

        model = Comment
        fields = [
            'id',
            'author',
            'body',
            'date_posted',
            'recipe'
        ]
