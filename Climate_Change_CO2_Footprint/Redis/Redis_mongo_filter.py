from pymongo import MongoClient
import datetime
import redis
import json
import numpy as np


redisClient = redis.StrictRedis(host='localhost', port=6379, db=0, charset="utf-8", decode_responses=True)
client = MongoClient('mongodb://localhost:27017')

Today_date = str((datetime.datetime.now() - datetime.timedelta(days = 0)).strftime('%d-%m-%Y'))
TOP = "TOP_CARS_CO2_"+ Today_date
CAR_REDIS_KEYS = "CAR_REDIS_KEYS_"+ Today_date

RedisKey = redisClient.smembers(CAR_REDIS_KEYS)

db = client.Live_Redis

def test1():
	dic = dict()
	dic['TripTime'] = coal['DateAndTime']
	dic['Current_Location'] = coal['Current_Location']
	dic['Latitude'] = coal['Latitude']
	dic['Longitude'] = coal['Longitude']
	dic['Distance'] = coal['Distance']
	dic['Speed'] = coal['Speed']
	dic['CO2'] = coal['CO2']
	return dic

#for rawkeys in RedisKey:
for rawkeys in RedisKey:
	BaseKey = redisClient.smembers(rawkeys)
	totalco2=0
	avg = []
	Value_lists=[]
	for brown in BaseKey:
		json_string = brown.replace("'", "\"")
		coal = json.loads(json_string)
		totalco2 += coal['CO2']
		avg.append(coal['Speed'])
		mean = int(np.average(avg))
		Value_lists.append(test1())
	mong = dict()
	mong['_id'] = rawkeys
	mong['Date'] = Today_date
	mong['CAR_Number'] = coal['CAR_Number']
	mong['Start_Location'] = coal['Start_Location']
	mong['End_Location'] = coal['End_Location']
	mong['Average_Speed'] = mean
	mong['CO2_Generated'] = totalco2
	redisClient.sadd(coal['CAR_Number'], str(mong))
	mong['Brand'] = coal['Brand']
	mong['Variant'] = coal['Variant']
	mong['Value'] = Value_lists
	mongo_coll = db.Live_Trips.insert(mong)
	redisClient.zincrby(TOP, totalco2, coal['CAR_Number'])
#	print(rawkeys)
	redisClient.delete(rawkeys)
	redisClient.srem(CAR_REDIS_KEYS, rawkeys)
