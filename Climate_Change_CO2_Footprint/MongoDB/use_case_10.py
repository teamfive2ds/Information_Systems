from pymongo import MongoClient
import pandas as pd

client = MongoClient('mongodb://localhost:27017')
db = client.cities
cities_co2 = db.cities_co2

City_emission_flag = [ 
{ '$sort' : {'C02_average': -1}},
{ '$limit' : 20 },
{'$project':{
'_id':0,
'City':1,
'Country':1,
'Country_code':1,
'C02_average':1,
'2018_C02(ppm)':1,
'2017_C02(ppm)':1,
'2016_C02(ppm)':1,
'Emission_quality_flag':1,
'Increased or decreased':1,
'Reason for increase/decrease in emissions':1
}
},
]
City_emission_flag_df = pd.DataFrame(list(cities_co2.aggregate(City_emission_flag)))
reorder_columns = City_emission_flag_df[['City','Country','Country_code','2018_C02(ppm)','2017_C02(ppm)','2016_C02(ppm)','C02_average','Emission_quality_flag','Increased or decreased','Reason for increase/decrease in emissions']]
print(reorder_columns)

