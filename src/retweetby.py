import requests

def getRetweet():
    id = input('Introduce ID del Tweet: ')
    r = requests.get(f'https://api.twitter.com/2/tweets/{id}/retweeted_by', headers={'Authorization': 'Bearer '})

    if r.status_code == 200:
        respuesta = r.json()
        print(respuesta)
    else:
        print(f'Se ha producido un error -> {r.status_code}')


    print()
