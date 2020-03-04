import datetime
import redis
import json
import pandas as pd

redisClient = redis.StrictRedis(host='localhost', port=6379, db=0, charset="utf-8", decode_responses=True)

print("Please enter Mode_Of_Generation\nExample: RunOfRiver Nuclear Waste Lignite Oil HardCoal Gas\n")
inp = input().split()

#lists=["RunOfRiver", "Nuclear"]
Elist=[]
for i in inp:
	RedisKey = redisClient.smembers(i)
	for brown in RedisKey:
		json_string = brown.replace("'", "\"")
		coal = json.loads(json_string)
		Elist.append(coal)
	dataf = pd.DataFrame(Elist)
	#print(df)
elecco2 = dataf.groupby(['Date', 'Mode_Of_Generation','Place', 'State']).sum()
print(elecco2)

