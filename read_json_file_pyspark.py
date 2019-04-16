import os

from pyspark.shell import sqlContext

root = os.path.dirname(__file__)
path = 'data/all_month.geojson'


def main():
    """
    :return: Place and magnitude, where magnitude is greater than 1.0.
    """
    data = os.path.join(root, path)
    df = sqlContext.read.json(data)
    df.createOrReplaceTempView('earthquakes')
    earthquakes_df = sqlContext.sql("SELECT properties.mag, properties.place "
                                    "FROM earthquakes "
                                    "WHERE properties.mag > 1.0")
    earthquakes_df.show()


if __name__ == '__main__':
    main()
