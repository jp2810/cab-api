import math
import numpy

def get_distance_between_cordinates(latA, lngA, latB, lngB):
    lngDelta = lngB - lngA
    sinLatA = math.sin(numpy.deg2rad(latA))
    sinLatB = math.sin(numpy.deg2rad(latB))
    cosLatA = math.cos(numpy.deg2rad(latA))
    cosLatB = math.cos(numpy.deg2rad(latB))
    cosLngDelta = math.cos(numpy.deg2rad(lngDelta))
    sinLngDelta = math.sin(numpy.deg2rad(lngDelta))
    dist = sinLatA * sinLatB
    dist += cosLatA * cosLatB * cosLngDelta
    if (dist >= 0.99999999):
        dist = math.pow((cosLatA * sinLatB) - (sinLatA * cosLatB * cosLngDelta), 2)
        dist += math.pow((cosLatB * sinLngDelta), 2)
        dist = sqrt(dist)
        dist = dist/((sinLatA * sinLatB) + (cosLatA * cosLatB * cosLngDelta))
        dist = atan(dist)
    else:
        dist = math.acos(dist)
    dist = dist * 6378.137
    # Apply correction factor for below and above 2 kms
    if (dist < 2):
        dist *= 1.45
    else:
        dist *= 1.55

    if dist >= 1:
        return round(dist, 2)
    else:
        return round(dist * 1000, 0) / 1000