'''@Author: Hari om Singh
   Organization: BT 
   Team : CCP  '''
from pykafka import KafkaClient
import time
import uuid

kafka_client = KafkaClient(hosts='localhost:9092')  

topic = kafka_client.topics['data1']
consumer=topic.get_balanced_consumer(consumer_group="test_group",auto_commit_enable=True,zookeeper_connect='localhost:2181')
while(1):
     message=consumer.consume()
     identifier = message.value
     print(identifier)
