#import libraries
import auth_tokens as auth
import tweepy
import logging
import json
import time

from confluent_kafka import Producer

logging.basicConfig(format='%(asctime)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename='producer.log',
                    filemode='w')

logger = logging.getLogger()
logger.setLevel(logging.INFO)

search_term = 'covid19'

client = tweepy.Client(auth.bearer_token)

tweets = client.search_recent_tweets(query=search_term, max_results=10) #v2.0

p=Producer({'bootstrap.servers':'localhost:9092'})
print('Kafka Producer has been initiated...')

def receipt(err,msg):
    if err is not None:
        print('Error: {}'.format(err))
    else:
        message = 'Produced message on topic {} with value of {}\n'.format(msg.topic(), msg.value().decode('utf-8'))
        logger.info(message)
        print(message)

def main():
    for tweet in tweets.data:
        data={
            'id': tweet.id,
            'text': tweet.text
        }
    m=json.dumps(data)
    p.poll(1)
    p.produce('covid19_topic', m.encode('utf-8'),callback=receipt)
    p.flush()
    time.sleep(3)

if __name__ == '__main__':
    main()
