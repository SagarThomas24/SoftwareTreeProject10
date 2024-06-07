## SoftwareTreeProject10
# Project Overview
This project consists of a Kafka consumer script, data files, and a Docker Compose configuration. The purpose is to consume messages from Kafka topics, process them, and store the data in JSON format.

# Files Included
consumer.py: A Python script to consume messages from Kafka topics and save them into JSON files.
data.json: A combined data file containing user and transaction data.
data_T1.json: A JSON file containing user data.
data_T2.json: A JSON file containing transaction data.
docker-compose.yml: A Docker Compose configuration file to set up the required services.


# File Descriptions
consumer.py
The consumer.py script connects to a Kafka server, subscribes to topics T1 and T2, and saves the consumed messages into respective JSON files.

# Usage
Ensure Kafka is running and accessible.
Install the required Python packages using pip install confluent_kafka.


# Run the script: 
python consumer.py.


# Details
Kafka Configuration:
bootstrap.servers: localhost:9092
group.id: myg
auto.offset.reset: earliest
Topics: T1 and T2
Output files: data_T1.json, data_T2.json
