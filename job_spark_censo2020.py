from pyspark.sql import SparkSession

spark = (
    SparkSession.builder.appName("ExerciseSparkCenso")
    .getOrCreate()
)

censo = (
    spark
    .read
    .format("csv")
    .option("header", True)
    .option("inferSchema", True)
    .option("delimiter", "|")
    .load("s3://datalake-brx-edc/raw-data/censo2020/")
)

(
    censo
    .write
    .mode("overwrite")
    .format("parquet")
    .partitionBy("CO_UF")
    .save("s3://datalake-brx-edc/staging/censo2020")
)
