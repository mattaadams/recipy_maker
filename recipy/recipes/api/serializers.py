from rest_framework import serializers
from recipes.models import Recipe, Ingredient, Comment


class IngredientListSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source="recipe.author", read_only=True)

    class Meta:
        model = Ingredient
        fields = ['name',
                  'recipe',
                  'author',
                  'id',
                  ]


class IngredientCreateUpdateSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False, write_only=False)

    class Meta:
        model = Ingredient
        fields = ['name', 'id']


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


class RecipeIngredientListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ingredient
        fields = ['name']


class RecipeCommentListSerializer(serializers.ModelSerializer):
    author = serializers.CharField(read_only=True)

    class Meta:

        model = Comment
        fields = [
            'id',
            'author',
            'body',
        ]


class RecipeListSerializer(serializers.ModelSerializer):
    ingredients = RecipeIngredientListSerializer(many=True, read_only=True)
    author = serializers.CharField(read_only=True)
    # detail_url = serializers.HyperlinkedIdentityField(
    #     view_name='recipe-api-detail',
    #     lookup_field='pk'
    # )

    class Meta:

        model = Recipe
        fields = [
            'id',
            'author',
            'title',
            'description',
            'ingredients',
            'instructions',
            'favorites'
        ]


class RecipeCreateUpdateSerializer(serializers.ModelSerializer):
    ingredients = IngredientCreateUpdateSerializer(many=True)
    author = serializers.CharField(read_only=True)
    image_url = serializers.URLField(required=False, allow_null=True)

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

        ingredients_data = validated_data.pop("ingredients")   # updated data
        remove_items = {item.id: item for item in instance.ingredients.all()}  # old data

        # This loop is needed if you have ID set to read_only, probably better way to implement this.
        # for idx, item in enumerate(remove_items):
        #     try:
        #         ingredients_data[idx]["id"] = item
        #     except:
        #         continue

        for ingredient_data in ingredients_data:
            item_id = ingredient_data.get("id", None)

            if item_id is None:
                # new item so create this
                instance.ingredients.create(**ingredient_data)
            elif remove_items.get(item_id, None) is not None:

                # update this item
                instance_item = remove_items.pop(item_id)

                Ingredient.objects.filter(id=instance_item.id).update(**ingredient_data)
            else:  # this  condition is only used if the id is writable
                if len(list(remove_items)) > 0:
                    old_id = list(remove_items.keys())[0]
                    ingredient_data['id'] = old_id
                    remove_items.pop(old_id)
                    Ingredient.objects.filter(id=old_id).update(**ingredient_data)
                else:
                    ingredient_data.pop('id')
                    instance.ingredients.create(**ingredient_data)

        for item in remove_items.values():
            item.delete()

        for field in validated_data:
            setattr(instance, field, validated_data.get(field, getattr(instance, field)))
        instance.save()

        return instance


class RecipeDetailSerializer(serializers.ModelSerializer):
    ingredients = RecipeIngredientListSerializer(many=True, read_only=True)
    author = serializers.CharField(read_only=True)
    favorite_count = serializers.IntegerField(source='favorites.count', read_only=True)
    comments = RecipeCommentListSerializer(many=True, read_only=True)

    class Meta:

        model = Recipe
        fields = [
            'id',
            'author',
            'title',
            'description',
            'ingredients',
            'instructions',
            'date_posted',
            'favorites',
            'favorite_count',
            'comments'
        ]


class RecipeFavoriteSerializer(serializers.ModelSerializer):
    favorites = serializers.CharField(read_only=True)
    favorite_count = serializers.IntegerField(source='favorites.count', read_only=True)

    class Meta:

        model = Recipe
        fields = [
            'favorites',
            'favorite_count'
        ]


class CommentListSerializer(serializers.ModelSerializer):
    author = serializers.CharField(read_only=True)
    recipe_title = serializers.CharField(source="recipe.title", read_only=True)

    class Meta:

        model = Comment
        fields = [
            'id',
            'author',
            'body',
            'recipe',
            'recipe_title'
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
