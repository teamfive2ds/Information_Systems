import pandas as pd
from pymongo import MongoClient
from pandas.io.json import json_normalize

client = MongoClient('mongodb://localhost:27017')

db = client.cities
cities_co2 = db.cities_co2

city_morning_evening_peak = [
{ '$sort' : {'Morning_Peak:': -1,'Evening_Peak:':-1}},
{'$project':{
'_id':0,
'City':1,
'Country':1,
'Country_code':1,
'C02_average':1,
'Morning_Peak':1,
'Evening_Peak':1,
}
},
]
city_morning_evening_peak_df = pd.DataFrame(list(cities_co2.aggregate(city_morning_evening_peak)))
print(city_morning_evening_peak_df)


