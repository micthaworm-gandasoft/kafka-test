
from kafka import KafkaProducer
import requests
import json
import time
import random
import os
import logging

def jsonserializer(message):
    return json.dumps(message).encode('utf-8')

  
producer = KafkaProducer(bootstrap_servers=os.environ['KAFKA_SERVER'],value_serializer=jsonserializer)


if __name__=='__main__':
    payload_size=os.environ['PAYLOAD_SIZE']
    for message in range(0,int(payload_size)):
        data =requests.get('https://reqres.in/api/users?page=2')
        producer.send(os.environ['TOPIC'],data.text)
        logging.info(data.status_code)