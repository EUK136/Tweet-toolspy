import requests

def getUser():
    id = input('Introduce el nombre de usuario: ')
    r = requests.get(f'https://api.twitter.com/2/users/by/username/{id}', headers={'Authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAAKIGNgEAAAAA%2FHm01Yp1vS4gKfQqlwdRT4xdroI%3DanyAJ4PXrWUhfKHwEjAIGtYMu9bg1A6Yf7vzqwBBpvLO975Vs3'})

    if r.status_code == 200:
        respuesta = r.json()
        print(respuesta)
    else:
        print(f'Se ha producido un error -> {r.status_code}')

    print()