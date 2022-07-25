from django import forms
from .models import Comment, Ingredient, Recipe
from django.forms import inlineformset_factory


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body', 'recipe']
        labels = {
            'body': 'New comment',
        }

        widgets = {
            'recipe': forms.TextInput(attrs={'type': 'hidden'}),
            'body': forms.Textarea(attrs={'rows': 2, 'cols': 2}),

        }


class UpdateCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body', 'recipe']
        labels = {
            'body': 'Update comment',
        }

        widgets = {
            'recipe': forms.TextInput(attrs={'type': 'hidden'}),
            'body': forms.Textarea(attrs={'rows': 2, 'cols': 2}),

        }


class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ['name',  'recipe']
        widgets = {
            # 'quantity': forms.TextInput(attrs={'placeholder': 'e.g. 2 cups'}),
            'name': forms.TextInput(attrs={'placeholder': 'e.g. 2 cups Milk', 'style': 'width:40%'}),

        }

    # def __init__(self, *args, **kwargs):
    #     super(IngredientForm, self).__init__(*args, **kwargs)
    #     self.fields['name'].required = False


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
                attrs={'placeholder': 'Enter description here', 'rows': 5, }),
            'image_url': forms.URLInput(
                attrs={'placeholder': 'https://'}),
            'instructions': forms.Textarea(
                attrs={'placeholder': 'Enter instructions here', 'rows': 5, }),
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
    can_delete=True,
    can_order=False
)
