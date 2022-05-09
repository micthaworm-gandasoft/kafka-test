from ensurepip import bootstrap
from kafka import KafkaAdminClient, KafkaConsumer
from kafka.errors import KafkaError
import json
import time
import os
import logging
# To consume latest messages and auto-commit offsets
if __name__=='__main__':
    consumer =KafkaConsumer(
        os.environ['TOPIC'],
        bootstrap_servers=os.environ['BROKER_SERVER'],
        auto_offset_reset="earliest",
        group_id='test-group'
    )
    for messages in consumer:
        time.sleep(10)
        logging.info(messages.value)
        print(json.loads(messages.value))