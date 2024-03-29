from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, redirect
from django.contrib.auth.decorators import login_required

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin
from django.views.generic.edit import FormMixin
from django.contrib.auth.models import User
from django.views.generic import (ListView,
                                  DetailView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView,
                                  TemplateView,
                                  View)
from .models import Recipe, Comment, Ingredient
from .forms import UpdateCommentForm, CommentForm, RecipeForm, IngredientForm, RecipeInlineFormSet
from django.urls import reverse
from django.http import HttpResponseRedirect, QueryDict, HttpResponse


# Class based Views (CBVs)
# DEFAULTS:
# template_name: <app>/<model>_<viewtype>.html (lowercase)
# context_object_name: object_list

# Check django docs to see which methods are in generic views
# ex. View does not have get_object()

class RecipeListView(ListView):
    model = Recipe
    template_name = 'recipes/home.html'
    context_object_name = 'recipes'
    ordering = ['-date_posted']
    paginate_by = 12


class UserRecipeListView(ListView):
    model = Recipe
    template_name = 'recipes/user_recipes.html'
    context_object_name = 'recipes'
    paginate_by = 12

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Recipe.objects.filter(author=user).order_by('-date_posted')

# replaced by below, keeping as ref..
# class FavoriteAddView(LoginRequiredMixin, View):
#     template_name = 'recipes/recipe_detail.html'

#     def get(self, request, *args, **kwargs):
#         recipe = Recipe.objects.get(id=kwargs['id'])

#         if recipe.favorites.filter(id=self.request.user.id).exists():
#             recipe.favorites.remove(self.request.user)
#         else:
#             recipe.favorites.add(self.request.user)
#         return HttpResponseRedirect(self.request.META['HTTP_REFERER'])


class FavoriteAddView(LoginRequiredMixin, DetailView):
    template_name = 'recipes/recipe_detail.html'
    model = Recipe

    def get(self, request, *args, **kwargs):
        recipe = self.get_object()

        if recipe.favorites.filter(id=self.request.user.id).exists():
            recipe.favorites.remove(self.request.user)
        else:
            recipe.favorites.add(self.request.user)
        return HttpResponseRedirect(self.request.META['HTTP_REFERER'])


class RecipeDetailView(FormMixin, DetailView):
    model = Recipe
    form_class = CommentForm
    fav = False

    def get_success_url(self):
        return reverse('recipe-detail', kwargs={'pk': self.object.id})

    def get_context_data(self, **kwargs):
        recipe = self.get_object()
        if recipe.favorites.filter(id=self.request.user.id).exists():
            self.fav = True

        context = super(RecipeDetailView, self).get_context_data(**kwargs)
        context['form'] = CommentForm(initial={'recipe': self.object})
        context['fav'] = self.fav
        context['title'] = recipe.title
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        instance = form.save()
        instance.author = self.request.user
        instance.save()
        return super(RecipeDetailView, self).form_valid(form)

    # def put(self, request, *args, **kwargs):
    #     data = QueryDict(self.request.body).dict()
    #     comment = Comment.objects.get(id=kwargs['pk'])
    #     context = {'comment': comment}
    #     form = CommentForm(data, instance=comment)
    #     if form.is_valid():
    #         form.save()
    #         return render(self.request, 'recipes/partials/comment_detail.html', context)
    #     context['form'] = form
    #     return render(self.request, 'recipes/partials/edit_comment_form.html', context)

    # def delete(self, request, *args, **kwargs):
    #     Comment.objects.get(id=kwargs['pk']).delete()
    #     return render(self.request, 'recipes/partials/comment_detail.html')


@login_required
def comment_detail(request, pk, recipe_id):
    comment = get_object_or_404(Comment, pk=pk)
    form = UpdateCommentForm(instance=comment)
    context = {}
    context['comment'] = comment
    context['recipe_id'] = recipe_id
    if request.method == 'GET':
        return render(request, 'recipes/partials/comment_detail.html', context)
    elif request.method == 'PUT':
        data = QueryDict(request.body).dict()
        form = UpdateCommentForm(data, instance=comment)
        if form.is_valid():
            if request.user.id == comment.author.id:
                form.save()
                return render(request, 'recipes/partials/comment_detail.html', context)
    elif request.method == 'DELETE':
        if request.user.id == comment.author.id:
            Comment.objects.get(pk=pk).delete()
        return render(request, 'recipes/partials/comment_detail.html')


@login_required
def comment_delete(request, pk, recipe_id):
    comment = get_object_or_404(Comment, pk=pk)
    form = UpdateCommentForm(instance=comment)
    context = {}
    context['comment'] = comment
    context['recipe_id'] = recipe_id
    context['form'] = form
    return render(request, "recipes/partials/delete_comment.html", context)


@login_required
def comment_edit_form(request, pk, recipe_id):
    comment = get_object_or_404(Comment, pk=pk)
    form = UpdateCommentForm(instance=comment)
    context = {}
    context['comment'] = comment
    context['recipe_id'] = recipe_id
    context['form'] = form
    return render(request, "recipes/partials/edit_comment_form.html", context)


class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    form_class = RecipeForm

    def get(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        ingredient_form = RecipeInlineFormSet()
        return self.render_to_response(
            self.get_context_data(
                form=form,
                ingredient_form=ingredient_form))

    def post(self, request, *args, **kwargs):

        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        ingredient_form = RecipeInlineFormSet(self.request.POST)
        if (form.is_valid() and ingredient_form.is_valid()):
            return self.form_valid(form, ingredient_form)
        else:
            return self.form_invalid(form, ingredient_form)

    def form_valid(self, form, ingredient_form):
        form.instance.author = self.request.user
        self.object = form.save()
        ingredient_form.instance = self.object
        ingredient_form.save()
        return super().form_valid(form)

    def form_invalid(self, form, ingredient_form):
        return self.render_to_response(
            self.get_context_data(
                form=form,
                ingredient_form=ingredient_form))


class RecipeUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Recipe
    form_class = RecipeForm

    def get_context_data(self, **kwargs):
        context = super(RecipeUpdateView, self).get_context_data(**kwargs)
        if self.request.POST:
            context['form'] = RecipeForm(self.request.POST, instance=self.object)
            context['ingredient_form'] = RecipeInlineFormSet(self.request.POST, instance=self.object)

        else:
            context['form'] = RecipeForm(instance=self.object)
            context['ingredient_form'] = RecipeInlineFormSet(instance=self.object)
        return context

    def post(self, request, *args, **kwargs):

        self.object = self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        ingredient_form = RecipeInlineFormSet(self.request.POST, instance=self.object)
        if (form.is_valid() and ingredient_form.is_valid()):
            return self.form_valid(form, ingredient_form)
        else:
            return self.form_invalid(form, ingredient_form)

    def form_valid(self, form, ingredient_form):
        form.instance.author = self.request.user
        self.object = form.save()
        ingredient_form.instance = self.object
        ingredient_form.save()
        return super().form_valid(form)

    def form_invalid(self, form, ingredient_form):
        return self.render_to_response(
            self.get_context_data(
                form=form,
                ingredient_form=ingredient_form))

    def test_func(self):
        recipe = self.get_object()
        if self.request.user.id == recipe.author.id:
            return True
        return False


class RecipeDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Recipe
    success_url = '/'

    def test_func(self):
        recipe = self.get_object()
        if self.request.user.id == recipe.author.id:
            return True
        return False
