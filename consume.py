import requests


class API():

    def __init__(self, username=None, password=None):
        self.username = username
        self.password = password
        if self.username:
            self.header = self.__get_token()

    def __get_token(self):
        my_user = {'username': self.username, 'password': self.password}
        token = requests.post('http://127.0.0.1:8000/api/auth/token/', my_user).json()
        my_auth_token = token.get('access')
        my_header = {'Authorization': f'Token {my_auth_token}'}
        return my_header

    def get_recipes(self, page_n=1,search_keyword=""):
        recipe_list_endpoint = requests.get(
            f'http://127.0.0.1:8000/api/recipes/?page={page_n}&search={search_keyword}').json()
        return recipe_list_endpoint['results']

    def get_one_recipe(self, recipe_id=1):
        recipe_list_endpoint = requests.get(
            f'http://127.0.0.1:8000/api/recipes/{recipe_id}').json()
        return recipe_list_endpoint

    def create_recipe(self, title, description, ingredient_list, instructions, image_url=None):
        my_recipe = {
            "title": title,
            "description": description,
            "ingredients": [{"name": ingredient} for ingredient in ingredient_list],
            "instructions": instructions,
            "image_url": image_url
        }
        recipe_create_endpoint = requests.post(
            f'http://127.0.0.1:8000/api/recipes/create', json=my_recipe, headers=self.header).json()
        return recipe_create_endpoint

    def get_users(self, page_n=1,search_keyword=""):
        user_list_endpoint = requests.get(
            f'http://127.0.0.1:8000/api/users/?page={page_n}&search={search_keyword}').json()
        return user_list_endpoint['results']

    def get_one_user(self, user_id=1):
        user_list_endpoint = requests.get(
            f'http://127.0.0.1:8000/api/users/{user_id}').json()
        return user_list_endpoint

    def create_user(self, username, email, email2, password):
        my_user = {
            "username": username,
            "email": email,
            "email2": email2,
            "password": password
        }
        user_list_endpoint = requests.post(
            'http://127.0.0.1:8000/api/users/register', json=my_user).json()
        return user_list_endpoint

    def favorite_recipe(self, recipe_id):

        user_list_endpoint = requests.post(
            f'http://127.0.0.1:8000/api/recipes/{recipe_id}/favorite', headers=self.header).json()
        return user_list_endpoint
