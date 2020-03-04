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


AUDI_diesel_petrol = [
  {
     '$group': { '_id': {'Mh': "$Mh",'Ft':"$Ft"},
     'C02_Consumed':{ '$sum': "$Ewltp (g/km)"},
     'Number_of_cars':{ '$sum': 1},
     }
  },
  { '$sort' : {'C02_Consumed': -1}},

]
BMW_diesel_petrol = [
  {
     '$group': { '_id': {'Mh': "$Mh",'Ft':"$Ft"},
     'C02_Consumed':{ '$sum': "$Ewltp (g/km)"},
     'Number_of_cars':{ '$sum': 1},
     }
  },
  { '$sort' : {'C02_Consumed': -1}},

]
Mercedes_diesel_petrol = [
  {
     '$group': { '_id': {'Mh': "$Mh",'Ft':"$Ft"},
     'C02_Consumed':{ '$sum': "$Ewltp (g/km)"},
     'Number_of_cars':{ '$sum': 1},
     }
  },
  { '$sort' : {'C02_Consumed': -1}},

]
Skoda_diesel_petrol = [
  {
     '$group': { '_id': {'Mh': "$Mh",'Ft':"$Ft"},
     'C02_Consumed':{ '$sum': "$Ewltp (g/km)"},
     'Number_of_cars':{ '$sum': 1},
     }
  },
  { '$sort' : {'C02_Consumed': -1}},

]
VW_diesel_petrol = [
  {
     '$group': { '_id': {'Mh': "$Mh",'Ft':"$Ft"},
     'C02_Consumed':{ '$sum': "$Ewltp (g/km)"},
     'Number_of_cars':{ '$sum': 1},
     }
  },
  { '$sort' : {'C02_Consumed': -1}},

]

Audi_diesel = list(audi.aggregate(AUDI_diesel_petrol))
Audi_diesel_petrol = json_normalize(Audi_diesel)
Audi = Audi_diesel_petrol[['_id.Mh','_id.Ft','Number_of_cars','C02_Consumed']]
BMW_diesel = list(bmw.aggregate(BMW_diesel_petrol))
BMW_diesel_petrol = json_normalize(BMW_diesel)
BMW = BMW_diesel_petrol[['_id.Mh','_id.Ft','Number_of_cars','C02_Consumed']]
Mercedes_diesel = list(mercedes.aggregate(Mercedes_diesel_petrol))
Mercedes_diesel_petrol = json_normalize(Mercedes_diesel)
Mercedes = Mercedes_diesel_petrol[['_id.Mh','_id.Ft','Number_of_cars','C02_Consumed']]
Skoda_diesel = list(skoda.aggregate(Skoda_diesel_petrol))
Skoda_diesel_petrol = json_normalize(Skoda_diesel)
Skoda = Skoda_diesel_petrol[['_id.Mh','_id.Ft','Number_of_cars','C02_Consumed']]
VW_diesel = list(volkswagen.aggregate(VW_diesel_petrol))
VW_diesel_petrol = json_normalize(VW_diesel)
VW = VW_diesel_petrol[['_id.Mh','_id.Ft','Number_of_cars','C02_Consumed']]

AUDI_BMW_MERCEDES_SKODA_VW = Audi.append([BMW, Mercedes, Skoda, VW], ignore_index=True)
print(AUDI_BMW_MERCEDES_SKODA_VW)

