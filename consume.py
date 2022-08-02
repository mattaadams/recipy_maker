import requests

my_user = {'username': 'admin', 'password': '1477'}

#recipe_list = requests.get('http://127.0.0.1:8000/api/recipes').text

token = requests.post('http://127.0.0.1:8000/api/auth/token/', my_user).json()

my_auth_token = token.get('access')

my_header = {'Authorization': 'Token {}'.format(my_auth_token)}

recipe_create_endpoint = requests.get('http://127.0.0.1:8000/api/recipes/create', headers=my_header).text

print(recipe_create_endpoint)
