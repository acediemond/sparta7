import requests
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsparta.bicycle

def Bicycle_scrape_insert():

    r = requests.get('http://openapi.seoul.go.kr:8088/6d4d776b466c656533356a4b4b5872/json/bikeList/1/99')

    rjson = r.json()

    bike = rjson['rentBikeStatus']
    rows = bike['row']

    for row in rows :

        stn = row["stationName"].split('. ')[1]
        prk = row['parkingBikeTotCnt']
        tot = row["rackTotCnt"]
        print('{} ({}/{})' .format(stn, prk, tot))
        db.insert_one({'Station': stn, 'ParkingBikeTotalCount': prk, 'RackTotalCount': tot})

def Bicycle_find_print():
    all_bicycle = list(db.find())
    for bicycle in all_bicycle:
        print(bicycle['Station'], bicycle['ParkingBikeTotalCount'])

Bicycle_find_print()