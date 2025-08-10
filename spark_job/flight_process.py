from pyspark.sql import SparkSession
from pyspark.sql.functions import col, when, lit, count, avg


def run_spark_job(input_path, output_dir):
    spark = SparkSession.builder.appName("FlightProcess").getOrCreate()

    df = spark.read.csv(input_path, header=True, inferSchema=True)

    # Add new calculated fields
    df_transformed = df.withColumn(
        "is_weekend", when(col("flight_day").isin("Sat", "Sun"), lit(1)).otherwise(lit(0))
    ).withColumn(
        "lead_time_category",
        when(col("purchase_lead") < 7, lit("Last-minute"))
        .when((col("purchase_lead") >= 7) & (col("purchase_lead") < 30), lit("Short-Term"))
        .otherwise(lit("Long-term"))
    ).withColumn(
        "booking_success_rate",
        (col("booking_complete").cast("double") / col("num_passengers").cast("double"))
    )

    # Aggregations
    route_data = df_transformed.groupBy("route").agg(
        count("*").alias("total_bookings"),
        avg(col("flight_duration").cast("double")).alias("Avg_Flight_Duration"),
        avg(col("length_of_stay").cast("double")).alias("Avg_Stay_Length"),
    )

    origin_insights = df_transformed.groupBy("booking_origin").agg(
        count("*").alias("total_bookings"),
        avg(col("booking_success_rate").cast("double")).alias("success_rate"),
        avg(col("purchase_lead").cast("double")).alias("Avg_purchase_lead"),
    )

    # Write results (Spark will create folders with CSV part files)
    df_transformed.coalesce(1).write.mode("overwrite").csv(f"{output_dir}/transformed.csv", header=True)
    route_data.coalesce(1).write.mode("overwrite").csv(f"{output_dir}/route_insights.csv", header=True)
    origin_insights.coalesce(1).write.mode("overwrite").csv(f"{output_dir}/origin_insights.csv", header=True)

    spark.stop()


if __name__ == "__main__":
    run_spark_job("/opt/airflow/flight_booking.csv", "/opt/airflow/output")
