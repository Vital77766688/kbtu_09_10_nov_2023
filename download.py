import pickle
import json
import requests
from exceptions import StatusCodeError


headers = {
    'authority': 'krisha.kz',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    # 'referer': 'https://krisha.kz/map/arenda/kvartiry/almaty-medeuskij/',
    'sec-ch-ua': '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}


def download_fake_data(url: str, page: int) -> list:
    filename = f"mock/data_{url.split('/')[-2]}"
    with open(filename, 'rb') as file:
        data = pickle.load(file)
    limit = 20
    offset = (page - 1) * limit
    result = data[offset:offset+limit]
    if len(result) == 0:
        return [], True
    return [
        {
            "id": advert['id'],
            "district": url.split('/')[-2],
            "title": advert['title'],
            "address": advert['addressTitle'],
            "rooms": advert['rooms'],
            "square": advert['square'],
            "price": advert['price'],
            # "images": [photo['src'] for photo in advert['photos'][:4]],
            "lat": advert['map']['lat'],
            "lon": advert['map']['lon']
        } for advert in result # if len(advert['photos']) > 0
    ], False


def download_data(url: str, page: int) -> list:
    resp = requests.get(url, headers=headers, params={'page': page})
    if resp.status_code != 200:
        raise StatusCodeError(resp.status_code, resp.reason)
    data = json.loads(resp.text)['adverts']
    if len(data) == 0:
        return [], True
    return [
        {
            "id": advert['id'],
            "district": url.split('/')[-2],
            "title": advert['title'],
            "address": advert['addressTitle'],
            "rooms": advert['rooms'],
            "square": advert['square'],
            "price": advert['price'],
            # "images": [photo['src'] for photo in advert['photos'][:4]],
            "lat": advert['map']['lat'],
            "lon": advert['map']['lon']
        } for advert in data.values() # if len(advert['photos']) > 0
    ], False
