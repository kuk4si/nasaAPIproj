import requests
from django.conf import settings


class NasaApi:
    _API = settings.API_KEY

    def __init__(self):
        pass

    @classmethod
    def get_asteroids_neows(cls, start_date):
        endpoint = 'https://api.nasa.gov/neo/rest/v1/feed'
        query_params = {'api_key': cls._API, 'start_date': start_date}
        response = requests.get(endpoint, params=query_params).json()
        # test = requests.get(endpoint, params=query_params)
        # print(test.url)
        items = {}
        for i in response['near_earth_objects']:
            asteroids_list = []
            for x in response['near_earth_objects'][i]:
                asteroids_list.append(x)
            items.update({i: asteroids_list})
        return items

    @classmethod
    def get_neo_lookup(cls, id):
        endpoint = f'https://api.nasa.gov/neo/rest/v1/neo/{id}?api_key={cls._API}'
        response = requests.get(endpoint)
        print(response.url)
        if response.status_code != 200:
            print('error')
            return False
        else:
            return response.json()

    @classmethod
    def get_mars_rover_photos(cls, date):
        endpoint = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos'
        query_params = {'api_key': cls._API, 'earth_date': date}
        response = requests.get(endpoint, params=query_params)
        print(response.url)
        if response.status_code != 200:
            print('error')
            return False
        else:
            if not response.json()['photos']:
                print('Нет фотографий')
            else:
                return response.json()
