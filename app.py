import json
import os
from flask import Flask, request
import helper
import ola
import taxiforsure
import uber

app = Flask(__name__)

@app.route('/getestimates', methods=['GET'])
def get_estimates():
    print request.args
    callback = request.args.get('callback', 'callback')
    latA = float(request.args.get('latA', 12.91028))
    lngA = float(request.args.get('lngA', 77.59971))
    latB = float(request.args.get('latB', 12.89107))
    lngB = float(request.args.get('lngB', 77.60395))

    dist = helper.get_distance_between_cordinates(latA, lngA, latB, lngB)
    result = {
        'uber': uber.get_fares_between_coordinates(latA, lngA, latB, lngB),
        'ola': ola.get_fares(dist),
        'taxiforsure': taxiforsure.get_fares(dist)
    }

    return callback + '(%s);' % json.dumps(result)


if __name__ == '__main__':
    app.run(host='0.0.0.0')

