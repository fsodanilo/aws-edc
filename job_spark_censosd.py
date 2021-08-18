from pyspark.sql.functions import mean, max, min, col, count
from pyspark.sql import SparkSession

spark = (
    SparkSession.builder.appName("ExerciseSparkCenso")
    .getOrCreate()
)

enem = (
    spark
    .read
    .format("csv")
    .option("header", True)
    .option("delimiter", "|")
    .load("s3://datalake-brx-edc/raw-data/censono/year-2020/matricula_norte.CSV")
)

(
    enem
    .write
    .mode("overwrite")
    .format("parquet")
    .save("s3://datalake-brx-edc/staging/censono")
)
#teste