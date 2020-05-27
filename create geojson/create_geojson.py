import psycopg2
import hashlib
from datetime import datetime
from geojson import Point, Feature, FeatureCollection, dump

app = Flask(__name__)
conn = psycopg2.connect(dbname="natura_v2", user="ak2195", password="l6kp3gsl", host="pgserver.mah.se")
cursor = conn.cursor()

def get_places():
    places = []
    cursor.execute("with get_cat as (select places.id, places.name, latitude, longitude, description, categories.name, row_number() over (partition by place_id order by place_id desc) as row_number from (places join place_has_cat on places.id=place_has_cat.place_id) join categories on place_has_cat.cat_id=categories.id order by places.name) select * from get_cat where row_number = 1")
    
    for place in cursor:
        places.append(place)

    features = []
    for place in places:
        point = Point((place[3], place[2]))
        features.append(Feature(geometry=point, properties={"description": "{}".format(place[4]), "name": "{}".format(place[1]), "id":"{}".format(place[0]), "category":"{}".format(place[5])}))
    feature_collection = FeatureCollection(features)
    with open('places.geojson', 'w') as f:
        dump(feature_collection, f)

get_places()
