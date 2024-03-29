import time

import requests
import pandas as pd
import json


def main():
    """
    :return: List of places and magnitudes, where magnitude is greater than 1.0.
    """
    start = time.time()

    url = 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_month.geojson'
    response = requests.get(url)
    data = response.json()  # Check the JSON Response Content documentation below
    features = pd.read_json(json.dumps(data['features']), orient='columns')
    for f in features['properties']:
        magnitude = f['mag']
        place = f['place']
        if magnitude > 1.0:
            print(place, '|', magnitude)

    end = time.time()
    print('Time spent', end - start, 'seconds')


if __name__ == "__main__":
    main()
