import requests

r = requests.get('http://openapi.seoul.go.kr:8088/6d4d776b466c656533356a4b4b5872/json/RealtimeCityAir/1/99')
rjson = r.json()


def name(a):
    print(a)
def mise():
    print('start')
    for row in rjson['RealtimeCityAir']['row']:
        if row['NO2'] >= 0.02:
            print(row['MSRSTE_NM'] + ':' + str(row['NO2']))
    print('end')



r = requests.get('http://openapi.seoul.go.kr:8088/6d4d776b466c656533356a4b4b5872/json/bikeList/1/99')

rjson = r.json()

bike = rjson['rentBikeStatus']
rows = bike['row']

for row in rows :

    stn = row["stationName"].split('. ')[1]
    prk = row['parkingBikeTotCnt']
    tot = row["rackTotCnt"]
    print('{} ({}/{})' .format(stn, prk, tot))
