import requests
import json

def get_fares(dist):
    # mini, dist in km
    data = []
    row = {
        'name': 'mini'
    }
    if dist <= 4:
        row['estimate'] = 100
    else:
        row['estimate'] = round((dist - 4) * 15, 2)

    data.append(row)

    return data

def get_products():
    url = 'https://mapi.olacabs.com/v2_1/location/search'
    headers = {
        'client': 'android',
        'api-key': '@ndroid'
    }

    parameters = {
        'user_id': 'KB9MYF7qSDSo4fNIKLbjY7tcCrmIoRi1JexP7NaisfgMSZICfRPzHT5IXw%2FD%0Aak3k64RfuNjRmCF8em1tgbyD3g%3D%3D%0A',
        'latitude': 12.9106394,
        'longitude': 77.5999182,
        'tag': 'pickup',
        'speed': 0.0,
        'accuracy': 253.0,
        'altitude': 0.0
    }

    response = requests.get(url, params=parameters, headers=headers)

    print response.status_code
    data = response.json
