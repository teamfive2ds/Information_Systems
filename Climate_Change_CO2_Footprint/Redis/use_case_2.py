import datetime
import redis
import json
import pandas as pd

redisClient = redis.StrictRedis(host='localhost', port=6379, db=0, charset="utf-8", decode_responses=True)

print("Enter the date to show the top 50 CO2 emitted CAR: ")
print("Date format should be DD-MM-YYYY")
inp = input()

RedisKey = redisClient.zrevrange("TOP_CARS_CO2_"+inp, 0, 50, "withscores")

dataf = pd.DataFrame(RedisKey, columns = ["Cars", "Total CO2 Emitted for the day"])
dataf.index = dataf.index + 1
print(dataf)

