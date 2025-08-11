# Flight-CICD-Airflow ✈️

End-to-end **Data Engineering** demo showcasing:
- **Apache Airflow** for orchestration
- **Apache Spark** for data processing
- **GitHub Actions** for CI/CD
- **Docker + GHCR** for packaging & deployment

---

## 🚀 Features
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

## 🏗️ Architecture
```text
Airflow DAG → PythonOperator → SparkSubmit → Data Transformations → Output CSVs
````

---

## 📦 Docker Image

This repo publishes a ready-to-use image to **GitHub Container Registry (GHCR)**.

**Latest build**:
`ghcr.io/harishg4/flight-cicd-airflow:latest`

### Pull image:

```bash
docker pull ghcr.io/harishg4/flight-cicd-airflow:latest
```

---

## 🛠️ Run Locally

### 1️⃣ Clone repo

```bash
git clone https://github.com/harishg4/Flight-CICD-Airflow.git
cd Flight-CICD-Airflow
```

### 2️⃣ Build locally (optional)

```bash
docker build -t flight-cicd-airflow .
```

### 3️⃣ Run Airflow + Spark with Docker Compose

```bash
docker compose up -d
```

Then open **Airflow UI**: [http://localhost:8080](http://localhost:8080)
Default creds: `airflow / airflow`

---

## 📂 Project Structure

```
airflow_job/
  flight_dag.py         # Airflow DAG definition
spark_job/
  flight_process.py     # Spark transformation job
requirements.txt        # Python dependencies
.github/workflows/ci-cd.yaml  # GitHub Actions workflow
Dockerfile
docker-compose.yaml
```

---

## ✅ CI/CD Workflow

* Runs on **push** / **PR** to `main`
* Steps:

  1. Install dependencies (Airflow, Spark, Pandas, etc.)
  2. Lint with `flake8`
  3. Format check with `black`
  4. Import all Airflow DAGs (sanity check)
  5. Run Spark smoke test
  6. Build and push Docker image to GHCR (only on `main` or tags)

---

## 📊 Example Output

After running, the Spark job produces:

```
output/transformed.csv/
output/route_insights.csv/
output/origin_insights.csv/
```

Each contains aggregated booking metrics for analytics.

---

## 🧑‍💻 Author

**Harish Gaddam** — [GitHub](https://github.com/harishg4)

---

## 📜 License

MIT — feel free to fork & adapt!

```
