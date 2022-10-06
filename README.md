# Kafka-Producer-twitter

This is repository for streaming API twitter data using Apache Kafka. In this case I'll be using twitter data with search topic as Covid19.

Pre-requisite:

Python 3.7 or later.
Kafka confluent. Install with command pip install confluent_kafka.
Tweepy. Install with command pip install tweepy.
How to run:

Open docker and start running docker-compose.yml file with command docker-compose up.
Fill in your twitter API credentials in auth_tokens.py file with your own.
Run file kafkaProducer.py. Note: Edit the file for V1 login if you want to use V1 Auth in twitter.
Open another terminal and run file kafkaConsumer.py to see the streamed data from kafka.
