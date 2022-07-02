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
        fields = ['name',  'recipe']
        widgets = {
            # 'quantity': forms.TextInput(attrs={'placeholder': 'e.g. 2 cups'}),
            'name': forms.TextInput(attrs={'placeholder': 'e.g. 2 cups Milk'}),

        }


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'image', 'image_url', 'description', 'instructions', 'author']
        exclude = ['author']

        labels = {
            "image": "Upload an Image (Optional)",
            "image_url": "Or paste image URL:"
        }
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Recipe Name'}),
            'description': forms.Textarea(
                attrs={'placeholder': 'Enter description here'}),
            'image_url': forms.URLInput(
                attrs={'placeholder': 'https://'}),
            'instructions': forms.Textarea(
                attrs={'placeholder': 'Enter instructions here'}),
        }

    def __init__(self, *args, **kwargs):
        super(RecipeForm, self).__init__(*args, **kwargs)
        self.fields['image_url'].required = False
        self.fields['image'].required = False


RecipeInlineFormSet = inlineformset_factory(
    Recipe,
    Ingredient,
    form=IngredientForm,
    extra=1,
    can_delete=False,
    can_order=False
)
