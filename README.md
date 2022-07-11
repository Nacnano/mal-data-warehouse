# MAL Data Warehouse
- A repository for automatic data warehouse codes for me using Apache Airflow and Github Action 

- So, the purposes of this project is mostly to train my Data Engineer skills

## Requirements 

1. Docker installed (the rest can be installed  using docker anyway)

2. 4 GB RAM avalible (more than 8 GB is highly recommended)

3. Enable your Docker RAM usage to >=4 GB 

### Warning : This may cause lag or crash your device when you start running Docker


## How to Run (For Ubuntu)

1. Setup Environments

```
echo -e "AIRFLOW_UID=$(id -u)" > .env
```

2. Initialize Airflow from Docker

```
docker-compose up airflow-init
```

3. Build everything from Apache Airflow

```
docker build -t apache/airflow:2.1.4 .
```

4. Run Airflow

```
docker-compose up
```

5. Execute Airflow using Bash in Docker

(Now you are in the Docker)

```
sudo docker exec -ti mal-data-warehouse-airflow-worker-1 bash
```

Note (Not Recommended): if you can't run as regular user, try using "sudo" to run as a root user.


Trigger Airflow

```
airflow dags trigger anime-data-warehouse
```

## User Interface 

While running, Airflow UI will be in localhost port 8080 (http://localhost:8080/)
