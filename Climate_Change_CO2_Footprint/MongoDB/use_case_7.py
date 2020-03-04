from pymongo import MongoClient
import pandas as pd
from pandas.io.json import json_normalize

client = MongoClient('mongodb://localhost:27017')

db = client.cars
volkswagen = db.volkswagen
skoda = db.skoda
mercedes = db.mercedes
bmw = db.bmw
audi = db.audi


lists=[]

car_brand = (input ("Enter Brand of Car:")).upper()
car_model = (input ("Enter Model of Car:")).upper()

def car_brands(a):
 cars = [
  { '$match' : { 'Mk': car_brand, 'Cn' : car_model }},
  {
     '$group': { '_id': {'Manufacturer_Name': "$Mh",'Variant_No':"$Va",'Fuel_type':"$Ft", 'Commercial_name':"$Cn",'CO2(g/km)':"$Ewltp (g/km)"}
  }
  },
  { '$sort': {'_id.CO2(g/km)': 1}
  },
 ]
 agg = list(a.aggregate(cars))
 #print(agg)
 Brand_model = json_normalize(agg)
 #print(Brand_model)
 lists.append(Brand_model)

if car_brand == "AUDI":
    car_brands(audi)
elif car_brand == "VOLKSWAGEN":
    car_brands(volkswagen)
elif car_brand == "MERCEDES":
    car_brands(mercedes)
elif car_brand == "BMW":
    car_brands(bmw)
elif car_brand == "SKODA":
    car_brands(skoda)

print(lists)




