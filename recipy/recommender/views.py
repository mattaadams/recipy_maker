from django.shortcuts import render
from .models import Recommender
from recipes.models import Recipe, User
from django.views.generic import ListView
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.forms.models import model_to_dict
import pandas as pd
from sklearn.neighbors import NearestNeighbors
from django.contrib.auth.mixins import LoginRequiredMixin

class RecommenderListView(LoginRequiredMixin,ListView):
    model = Recipe
    template_name = 'recommender/recommended_recipes.html'
    context_object_name = 'recipes'

    def get_queryset(self):
        n_favorites = Recipe.objects.filter(favorites=self.request.user.id)
        if len(n_favorites) < 10:
            return None
             
        recipe_list = Recipe.objects.all()

        rec_list = []
        for recipe in recipe_list:
            recipe_id = model_to_dict(recipe).get('id')
            fav_users = model_to_dict(recipe).get('favorites')
            fav_user_ids = [u.id for u in fav_users]
            rec_list.append([recipe_id, fav_user_ids])

        df = pd.DataFrame(rec_list, columns=['id', 'favorites']).explode('favorites')
        df_crosstab = pd.crosstab(index=df['id'], columns=df['favorites'])
        matrix = df_crosstab.to_numpy()
        favorites_vector  = self._get_favs_vector(df_crosstab,self.request.user.id)
        most_similar_dict = self._get_recommendations(matrix,df_crosstab,self.request.user.id)
        recs = list(most_similar_dict.keys())

        return Recipe.objects.filter(id__in=recs).order_by('-date_posted')

    def _get_user_favorites(self,df,user_id):
        return df.index[df[user_id]==True].tolist()

    def _get_favs_vector(self,df,user_id):
        favs_vector = []
        col_values = df.columns.values.tolist()
        favorites_list = self._get_user_favorites(df,user_id)
        for col in col_values:
            if col in favorites_list:
                favs_vector.append(1)
            else:
                favs_vector.append(0)
        return favs_vector

    def _get_recommendations(self,matrix,df,user_id):
        results = []
        knn_model = NearestNeighbors(metric='cosine',algorithm='brute')
        fit_model = knn_model.fit(matrix)
        for recipe_id in self._get_user_favorites(df,user_id)[-10:]:
            input_ = df.loc[recipe_id].values.reshape(1,-1)
            distances,indices = fit_model.kneighbors(input_, n_neighbors=10)
            distances = distances.flatten().tolist()
            indices = indices.flatten().tolist()
            for i in range(len(distances)):
                if indices[i] not in self._get_user_favorites(df,user_id) and distances[i] > 0.1:
                    results.append([indices[i],distances[i]])

        res = pd.DataFrame(results,columns=['indices','distances']).groupby(['indices']).sum()
        res = res.sort_values(by=['distances'],ascending=False)
        most_similar = res.head(9)
        most_similar_dict = pd.Series(most_similar.distances.values,index=most_similar.index).to_dict()
        return most_similar_dict


