
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
    i=0
    while i<=100:
        data =requests.get('https://reqres.in/api/users?page=2')
        logging.info(json.dumps(data.text))
        producer.send(os.environ['TOPIC'],data.text)
        i+=1
    logging.info("###FINISHED TRANSMITTING###")