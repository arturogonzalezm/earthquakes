import requests
import pandas as pd
import json


def main():
    """
    :return: List of places and magnitudes.
    """
    url = 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_month.geojson'
    response = requests.get(url)
    data = response.json()  # Check the JSON Response Content documentation below
    features = pd.read_json(json.dumps(data['features']), orient='columns')
    for f in features['properties']:
        magnitude = f['mag']
        place = f['place']
        print(place, '|', magnitude)


if __name__ == "__main__":
    main()
