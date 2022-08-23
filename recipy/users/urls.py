from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from users import views as user_views
from .views import FavoriteRecipeListView
urlpatterns = [
    path('register/', user_views.register, name='register'),
    path('profile/', user_views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('reset_password/',auth_views.PasswordResetView.as_view(template_name="users/password_reset.html"), name='reset_password'),
    path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(template_name="users/password_reset_sent.html"), name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name="users/password_reset_confirm.html"), name='password_reset_confirm'),
    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(template_name="users/password_reset_complete.html"), name='password_reset_complete'),

    path('favorites/', FavoriteRecipeListView.as_view(), name='favorite-recipe'),
    

]
