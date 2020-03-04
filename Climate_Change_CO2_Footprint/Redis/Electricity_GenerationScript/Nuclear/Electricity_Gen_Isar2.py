import random
import datetime
import time
import redis

def test():
    dic = dict()
    dic['DateAndTime'] = datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')
    dic['Date'] = datetime.datetime.now().strftime('%d-%m-%Y')
    dic['Mode_Of_Generation'] = "Nuclear"
    dic['Place'] = "Isar2"
    dic['State'] = "Bavaria"
    dic['KWHR'] = random.randint(70,90)
    dic['CO2'] = random.randint(90,130)
    time.sleep(5)
    return dic

Ele = "Nuclear"

redisClient = redis.StrictRedis(host='localhost', port=6379, db=0, charset="utf-8", decode_responses=True)

while True:
    redins = test()
#    print(redins)
    redisClient.sadd(Ele, str(redins))

