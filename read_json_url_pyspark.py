import json

from urllib.request import urlopen
from pyspark.shell import spark, sqlContext

url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_month.geojson"


def load_json_data(json_url):
    response = urlopen(json_url)
    source = response.read().decode("utf-8")
    data = json.dumps(source)
    return json.loads(data)


def main():
    df = sqlContext.read.json(load_json_data(url))
    df.createOrReplaceTempView('earthquakes')
    earthquakes_df = spark.sql("SELECT properties.mag, properties.place "
                               "FROM earthquakes "
                               "WHERE properties.mag > 1.0")
    earthquakes_df.show()


if __name__ == '__main__':
    main()
