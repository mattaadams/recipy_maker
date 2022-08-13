from django.shortcuts import render
from .models import Recommender
from recipes.models import Recipe, User
from django.views.generic import ListView
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.forms.models import model_to_dict
import pandas as pd
from sklearn.neighbors import NearestNeighbors


class RecommenderListView(ListView):
    model = Recipe
    template_name = 'recommender/recommended_recipes.html'
    context_object_name = 'recipes'

    def get_queryset(self):
        recipe_list = Recipe.objects.all()

        rec_list = []
        for recipe in recipe_list:
            recipe_id = model_to_dict(recipe).get('id')
            fav_users = model_to_dict(recipe).get('favorites')
            fav_user_ids = [u.id for u in fav_users]
            rec_list.append([recipe_id, fav_user_ids])

        df = pd.DataFrame(rec_list, columns=['id', 'favorites']).explode('favorites')
        df_crosstab = pd.crosstab(index=df['id'], columns=df['favorites'])
        matrix = df_crosstab.to_numpy().reshape(1, -1)
        print(matrix)
        # model = read_pickle()
        # pred = model.predict(User_favorites,matrix)
        # recommendation =  Recommender.object.create(user,pred)
        # recommendation.save()

        return Recipe.objects.filter(favorites=self.request.user).order_by('-date_posted')
