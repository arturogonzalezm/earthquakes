import requests


def main():
    """
    :return: List of places and magnitudes.
    """
    url = 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_month.geojson'
    response = requests.get(url)
    data = response.json()  # Check the JSON Response Content documentation below

    for dictionary in data['features']:
        place = dictionary['properties']['place']
        magnitude = dictionary['properties']['mag']
        print(place, '|', magnitude)


if __name__ == "__main__":
    main()
