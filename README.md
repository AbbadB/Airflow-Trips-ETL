# Trips ETL Pipeline
An ETL process using the framework [Airflow](https://airflow.apache.org/) to orchestrate the flux.

The process is divided from extracting the data from a PostgreSQL server, transforming it with SQL functions and loading into new tables to store the metrics.


## Installation

First the docker-compose must be installed, that can be found [here](https://docs.docker.com/compose/install/).



## Usage

The next step is to run the docker-compose command in the terminal, inside the project folder to build the environment.

```bash
docker-compose up -d
```

After it builds, you must wait until the container mobi7postgres_1 be ready to connection. You can see that inside the container if you are using the docker hub interface.

![My Remote Image](https://i.imgur.com/sRrWhN1.png)

Than you can access the Airflow interface by entering in localhost:8080 and log into with the access:
- username: airflow 
- password: airflow

![Login Airflow](https://i.imgur.com/289yeVf.png)

Since the DAG is triggered monthly, you must trigger it manually in the actions column.

![Action Button](https://i.imgur.com/p7TwOih.png)

After triggering the DAG it will create tables and generate a .csv report inside the folder files, you can verify the tables accessing the adminer on you localhost:8585 and logging with the access:
- Sistema: PostgreSQL
- Servidor: mobi7postgres
- Usuário: postgres
- Senha: postgres
- Base de dados: mobi7_code_interview

![Login adminer](https://i.imgur.com/he67dna.png)
