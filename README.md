# MAL Data Warehouse
- A repository for automatic data warehouse codes for me using Apache Airflow and Github Action 

- So, the purposes of this project is mostly to train my Data Engineer skills


## How to Run (For Ubuntu)

1. Initialize Airflow from Docker

```
docker-compose up airflow-init
```

2. Build everything from Apache Airflow
```
docker build -t apache/airflow:2.1.4 .
```

3. Run Airflow
```
docker-compose up
```

Note (Not Recommended): if you can't run as regular user, try using "sudo" to run as a root user.

## User Interface 

While running, Airflow UI will be in localhost port 8080 (http://localhost:8080/)
