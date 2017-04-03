'''@Author: Hari om Singh
   Organization:
   Team :   '''
from pykafka import KafkaClient
import requests
from bs4 import BeautifulSoup
import ConfigParser as configparser
import time

while(1):
    time.sleep(5)
    r=requests.get('http://www.hl.co.uk/shares/shares-search-results/b/bt-group-plc-ordinary-5p')
    soup=BeautifulSoup(r.content)
    #print(soup)
    for i in soup.find_all("span",{"class":"bid price-divide"}):
        sell_price=i.text
    for i in soup.find_all("span",{"class":"ask price-divide"}):
        buy_price=i.text
    localtime = time.asctime( time.localtime(time.time()) )
    message=localtime+' '+ 'Sell-Price :'+ sell_price + ' Buy-Price :'+buy_price
    Prices=str(message)
    print(message)
    kafka_client = KafkaClient(hosts='localhost:9092')
    topic = kafka_client.topics['data1']
    producer=topic.get_producer()
    producer.produce(Prices)
