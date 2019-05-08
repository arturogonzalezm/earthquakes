import requests
import time

url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_month.geojson"


def load_json_data(json_url):
    """
    :param json_url: "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_month.geojson"
    :return: Earthquakes json data
    """
    data = requests.get(json_url).json()
    return data


def get_place_and_magnitude(data):
    """
    :param data: Earthquakes json data
    :return: List of places and magnitudes, where magnitude is greater than 1.0.
    """
    start = time.time()

    data = load_json_data(url)
    for dictionary in data['features']:
        place = dictionary['properties']['place']
        magnitude = dictionary['properties']['mag']
        if magnitude > 1.0:
            print(place, '|', magnitude)

    end = time.time()
    print('Time spent', end - start, 'seconds')


if __name__ == "__main__":
    get_place_and_magnitude(url)

# Python3.6: 4.863826036453247
# PyPy3: 4.521245002746582
