FROM apache/airflow:2.9.0-python3.9

# Install Java (needed for Spark) + curl
USER root
RUN apt-get update && \
    apt-get install -y openjdk-17-jre-headless curl && \
    rm -rf /var/lib/apt/lists/*

# Install Spark (3.5.0 archived URL)
RUN curl -L https://archive.apache.org/dist/spark/spark-3.5.0/spark-3.5.0-bin-hadoop3.tgz \
    -o spark-3.5.0-bin-hadoop3.tgz && \
    tar xvf spark-3.5.0-bin-hadoop3.tgz -C /opt/ && \
    ln -s /opt/spark-3.5.0-bin-hadoop3 /opt/spark && \
    rm spark-3.5.0-bin-hadoop3.tgz


# Environment variables
ENV SPARK_HOME=/opt/spark
ENV PATH=$SPARK_HOME/bin:$PATH

USER airflow
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
