import random
import datetime
import time
import redis
import geopy.geocoders
from geopy.geocoders import Nominatim
from geopy import distance

geolocator = Nominatim(user_agent="CARAPP")

redisClient = redis.StrictRedis(host='localhost', port=6379, db=0, charset="utf-8", decode_responses=True)

def test():
    lat = str(round(random.uniform(start_location.latitude, End_location.latitude),7))
    lon = str(round(random.uniform(start_location.longitude, End_location.longitude),7))
#    geol = str("\""+lat+", "+lon+"\"")
#    location = geolocator.geocode(geol)
    dic = dict()
    dic['DateAndTime'] = (datetime.datetime.now() - datetime.timedelta(days = 0)).strftime('%d-%m-%Y %H:%M:%S')
    dic['CAR_Number'] = car_number
    dic['Brand'] = Brand
    dic['Variant'] = Variant
    dic['Start_Location'] = start_point
    dic['End_Location'] = End_point
    dic['Current_Location'] = "NA"
    dic['Latitude'] = lat
    dic['Longitude'] = lon
    dic['Speed'] = random.randint(60,120)
    dic['Distance'] = int(counter)
    dic['CO2'] = random.randint(90,120)
    time.sleep(1)
    return dic

    
print("Please enter the CAR Number:")
car_number = input()

vart = car_number+"_VAR"

RedisKey = redisClient.lrange(vart, 0, -1)

Brand = str(RedisKey[1])
Variant = str(RedisKey[0])

print("\nYour car details are:\nBrand: {}\nVariant: {}\n".format(Brand, Variant))

print("Enter the Start Point:")
start_point = input()
start_location = geolocator.geocode(start_point)
geo_start = start_location.latitude, start_location.longitude
print(geo_start)

print("Enter the Destination Point:")
End_point = input()
End_location = geolocator.geocode(End_point)
geo_end = End_location.latitude, End_location.longitude
print(geo_end)

distance_id = int(distance.distance(geo_start, geo_end).km)
print("Distance between {} and {} is: {}\n".format(End_point, start_point, distance_id))

Today_date = str((datetime.datetime.now() - datetime.timedelta(days = 0)).strftime('%d-%m-%Y-%H-%M-%S'))
Today_car_date = str((datetime.datetime.now() - datetime.timedelta(days = 0)).strftime('%d-%m-%Y'))

CAR_REDIS_KEYS = "CAR_REDIS_KEYS_"+ Today_car_date

counter = 2
while counter <= distance_id:
    n = random.randint(1, 7)
    redins = test()
    counter = counter + n
    print(redins)
    redisClient.sadd(car_number + '_' + Today_date, str(redins))
redisClient.sadd(CAR_REDIS_KEYS, car_number + '_' + Today_date)

