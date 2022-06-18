from django import forms
from .models import Comment, Ingredient, Recipe
from django.forms import inlineformset_factory


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'body', 'recipe']

        widgets = {
            'recipe': forms.TextInput(attrs={'type': 'hidden'}),
        }


class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ['name', 'quantity', 'unit', 'recipe']


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'image', 'description', 'instructions', 'author']
        exclude = ['author']


RecipeInlineFormSet = inlineformset_factory(
    Recipe,
    Ingredient,
    form=IngredientForm,
    extra=2,
    can_delete=False,
    can_order=False
)