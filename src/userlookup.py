import requests
from colorama import Fore, Style, init
init()

def getUser():
    id = input('Introduce el nombre de usuario: ')
    r = requests.get(f'https://api.twitter.com/2/users/by/username/{id}', headers={'Authorization': 'Bearer '})

    if r.status_code == 200:
        respuesta = r.json()
        name = respuesta['data']['name']
        username = respuesta['data']['username']
        print(Style.BRIGHT + f'\n[*] Informacion del usuario:\n', Fore.GREEN + f'Nombre de usuario -> {name}\n Username -> {username}')
    else:
        print(f'Se ha producido un error -> {r.status_code}')

    print()