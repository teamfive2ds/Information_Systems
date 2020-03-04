from pymongo import MongoClient
import datetime
import redis
import json
import pandas as pd

redisClient = redis.StrictRedis(host='localhost', port=6379, db=0, charset="utf-8", decode_responses=True)

print("Please enter the CAR Number:")
car_number = input().split()

Elist=[]
for i in car_number:
	RedisKey = redisClient.smembers(i)
	for brown in RedisKey:
		json_string = brown.replace("'", "\"")
		coal = json.loads(json_string)
		Elist.append(coal)
	dataframe1 = pd.DataFrame(Elist)
CARS_CO2 = dataframe1.groupby(['Date', 'CAR_Number','Start_Location', 'End_Location', 'Average_Speed']).sum()
print(CARS_CO2)

