import requests
import time


def main():
    """
    :return: List of places and magnitudes, where magnitude is greater than 1.0.
    """
    start = time.time()

    url = 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_month.geojson'
    response = requests.get(url)
    data = response.json()  # Check the JSON Response Content documentation below

    for dictionary in data['features']:
        place = dictionary['properties']['place']
        magnitude = dictionary['properties']['mag']
        if magnitude > 1.0:
            print(place, '|', magnitude)

    end = time.time()
    print('Time spent', end - start, 'seconds')


if __name__ == "__main__":
    main()

# Python3.6: 4.863826036453247
# PyPy3: 4.521245002746582
