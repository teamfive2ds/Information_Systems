from pymongo import MongoClient
import pandas as pd
from matplotlib import pyplot as plt

client = MongoClient('mongodb://localhost:27017')
db = client.cities
cities_co2 = db.cities_co2

city_wise_dense = [ 
{ '$sort' : {'C02_average': -1, 'Population': -1}},
{ '$limit' : 20 },
{'$project':{
'_id':0,
'City':1,
'Country':1,
'Country_code':1,
'Population':1,
'C02_average':1,
'Protocol':1,
}
},
]

city_wise_dense_df = pd.DataFrame(list(cities_co2.aggregate(city_wise_dense)))
reorder_columns = city_wise_dense_df[["City","Country","Country_code","C02_average","Population","Protocol"]]
print(reorder_columns)
