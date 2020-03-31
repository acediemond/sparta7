import pymongo

from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
#import pymongo.mongoclient 도 가능

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta                      # 'dbsparta'라는 이름의 db를 만듭니다.

# MongoDB에 insert 하기

# 'users'라는 collection에 {'name':'bobby','age':21}를 넣습니다.
# db.users.insert_one({'name':'bobby','age':21})
#all_users = list(db.users.find({'name':'bobby'}))
#print(all_users)

db.users.update_one({'name': 'bobby'}, {'$set':{'age':23}})

all_users = db.users.find()
for user in all_users:
    print(user)
