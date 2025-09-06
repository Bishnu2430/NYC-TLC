import findspark
findspark.init('/opt/spark')

import pyspark
from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("NYC TLC Analysis") \
    .config("spark.sql.adaptive.enabled", "true") \
    .getOrCreate()

print("Spark session initialized!")
print(f"Spark version: {spark.version}")
