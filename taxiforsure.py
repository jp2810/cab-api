import requests
import json

def get_fares(dist):
    # Tata indica Non AC, dist in km
    data = []
    row = {
        'name': 'Taxi Indica Non AC'
    }

    if dist <= 10:
        row['estimate'] = 200
    else:
        row['estimate'] = round((dist - 10) * 10, 2)

    data.append(row)

    return data
