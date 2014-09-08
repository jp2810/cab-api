import requests
import json
from config import uber_server_token

def get_products():
    url = 'https://api.uber.com/v1/products'

    parameters = {
        'server_token': uber_server_token,
        'latitude': 37.775818,
        'longitude': -122.418028,
    }

    response = requests.get(url, params=parameters)

    print response.status_code
    data = response.json

    for product in data['products']:
        print product


def get_fares_between_coordinates(latA, lngA, latB, lngB):
    url = 'https://api.uber.com/v1/estimates/price'

    parameters = {
        'server_token': uber_server_token,
        'start_latitude': latA,
        'start_longitude': lngA,
        'end_latitude': latB,
        'end_longitude': lngB
    }

    response = requests.get(url, params=parameters)

    if response.status_code != 200:
         return 'false'

    data = response.json

    result = []
    for price in data['prices']:
        row = {
            'name': price['localized_display_name'],
            'estimate': price['estimate']
        }
        
        result.append(row)

    return result

def book_cab():
    url = 'https://events.uber.com/mobile/event'

    parameters = {
        "deviceLanguage": "en_IN",
        "app": "client",
        "location": [
            77.5998388,
            12.9108645
        ],
        "epoch": 1409943100430,
        "deviceModel": "Micromax A116",
        "locationHorizontalAccuracy": 0,
        "clientUuid": "028e7d7b-dffb-4d8a-939b-08448ff9174a",
        "version": "3.11.1",
        "libraryVersion": "3.11.1",
        "locationAltitude": 0,
        "device": "android",
        "sessionHash": "06ac5c18-fce7-462d-b9a9-97111d26557f",
        "eventName": "RequestVehicleRequest",
        "parameters": {
            "expenseTrip": False,
            "duration": 4,
            "pickupLocation": {
                "type": "geocodmanual",
                "id": "52e167c5-f026-4a75-9de9-adfffd27967f",
                "longitude": 77.5998474,
                "latitude": 12.9108876,
                "distance": 0
            },
            "vehicleViewId": "1228",
            "reason": "geocodmanual",
            "page": "device",
            "requestGuid": "4175600f-c3c2-44b7-8fc2-26fac386424b",
            "method": "destinationSet",
            "useCredits": True,
            "destinationLocation": {
                "address_components": [],
                "type": "backfill",
                "formatted_address": "Koramangala Layout, Bengaluru, Karnataka, India",
                "id": "",
                "relevance": "",
                "referenceType": "google_places",
                "reference": "ChIJLfyY2E4UrjsRVq4AjI7zgRY",
                "longitude": 77.62710779999999,
                "latitude": 12.9279232,
                "distance": 0
            },
            "multiplier": 1
        },
        "deviceOS": "4.2.1",
        "deviceId": "911304254247970",
        "locationVerticalAccuracy": 0
    }

    response = requests.post(url, params=parameters)

    print response.status_code
    data = response.json

    for price in data['prices']:
        print price['localized_display_name']
        print price['estimate']