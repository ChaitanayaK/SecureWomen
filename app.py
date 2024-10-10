from flask import Flask, request, jsonify
import requests
import re
import math
from geopy.geocoders import Nominatim

app = Flask(__name__)

def haversine(coord1, coord2):
    R = 6371.0
    lat1, lon1 = coord1
    lat2, lon2 = coord2
    lat1 = math.radians(lat1)
    lon1 = math.radians(lon1)
    lat2 = math.radians(lat2)
    lon2 = math.radians(lon2)
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = R * c
    return distance

def extract_coordinates(html_text):
    meta_tag_match = re.search(r'<meta content="https://maps\.google\.com/maps/api/staticmap\?.*?markers=([^&"]+)', html_text)
    if meta_tag_match:
        markers = meta_tag_match.group(1)
        coordinates = markers.split('%7C')
        decoded_coordinates = [coord.replace('%2C', ',').split(',') for coord in coordinates]
        decoded_coordinates = [(float(coord[0]), float(coord[1])) for coord in decoded_coordinates]
        return decoded_coordinates
    else:
        return None

def getNearestStation(myLocation: tuple):
    geolocator = Nominatim(user_agent="geoapi")
    for zoom in ['10', '15', '20']:
        url = f"https://www.google.com/maps/search/police+station+near+me/@{myLocation[0]},{myLocation[1]},{zoom}z"

        response = requests.get(url)

        coordinates_list = extract_coordinates(response.text)

        if coordinates_list is None:
            return None
        
        min_distance = float('inf')
        closest_policestation = None
        for coordinates in coordinates_list:
            distance = haversine(myLocation, coordinates)
            if distance < min_distance:
                min_distance = distance
                closest_policestation = coordinates

        location = geolocator.reverse(closest_policestation, exactly_one=True)

        return (min_distance, location.address, (location.latitude, location.longitude))

@app.route('/', methods=['POST'])  
def receive_data():
    latitude = float(request.args.get('latitude'))
    longitude = float(request.args.get('longitude'))

    response = getNearestStation((latitude, longitude))

    return jsonify({
        'distance': response[0],
        'police_station': response[1],
        'coordinates': response[2]
    })

if __name__ == "__main__":
    app.run(debug=True)
