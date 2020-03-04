from neo4j import GraphDatabase
import pandas as pd
from pandas.io.json import json_normalize
import redis
import numpy as np

redisClient = redis.StrictRedis(host='localhost', port=6379, db=0, charset="utf-8", decode_responses=True)
driver  = GraphDatabase.driver(uri ="bolt://localhost:7687", auth =('neo4j','family'))

session = driver.session()
q =""MATCH (n:Family{Name:'Sharma'})-[r:Travels]-(m:Destination) 
WITH point({longitude:toFloat(n.Longitude),latitude:toFloat(n.Latitude)}) AS p1, 
point({longitude:toFloat(m.Longitude),latitude:toFloat(m.Latitude)}) AS p2, r,n,m 
WITH toFloat(round(distance(p1,p2)))  AS TrDist, r, n,m 
Return n.Name AS Source, m.Place As Destination, (TrDist*0.001) AS Distance, r.Car As Car, r.date As Date  order by Date""

query = session.run(q)

x=[]
for i in query:
	x.append(i)
df = pd.DataFrame(x)

cm = []
cb = []
for i in df[3]:
	#print(i)
 	car_model = str(i.replace(" ","_"))
 	cm.append(car_model)
 	car_brand = redisClient.get(car_model)
 	cb.append(car_brand)

b=[]
j=0
for co in cb[1]:
	co=float(co)
	emission=df.iloc[j,2]*co
	b.append(em)
df["Emission"]=b

print(df)

grouped=df.groupby(4)
print(grouped['Emission'].agg(np.sum))