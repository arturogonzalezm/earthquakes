import time

import requests
import pandas as pd
import json

from pandas.io.json import json_normalize


def main():
    """
    :return: List of places and magnitudes, where magnitude is greater than 1.0.
    """
    start = time.time()

    url = 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_month.geojson'
    response = requests.get(url).json()
    features = pd.read_json(json.dumps(response['features'], indent=2), orient='columns')
    df = pd.DataFrame(features)
    properties = json_normalize(df['properties'])
    print(properties[['place', 'mag']])

    end = time.time()
    print('Time spent', end - start, 'seconds')


if __name__ == "__main__":
    main()
