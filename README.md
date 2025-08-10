# Flight-CICD-Airflow

End-to-end **Data Engineering** demo showcasing:
- **Apache Airflow** for orchestration
- **Apache Spark** for data processing
- **GitHub Actions** for CI/CD
- **Docker + GHCR** for packaging & deployment

---

## Features
- **Airflow DAG** (`flight_pipeline`) that:
  - Runs a Spark job (`flight_process.py`) to process flight booking data
  - Generates aggregated insights
- **Spark transformations**:
  - Adds calculated fields (weekend flag, lead time category, booking success rate)
  - Aggregates by `route` and `booking_origin`
  - Writes results to CSV
- **CI/CD Pipeline**:
  - Lint & format checks (`flake8`, `black`)
  - DAG import validation
  - Spark smoke test
  - Automatic Docker image build & push to [GHCR](https://ghcr.io)

---

## Architecture
```text
Airflow DAG → PythonOperator → SparkSubmit → Data Transformations → Output CSVs
