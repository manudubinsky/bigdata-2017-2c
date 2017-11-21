from pymongo import MongoClient

client = MongoClient()
db = client.test

cursor = db.tweets.find ({"place":{"$ne":None}})


var = 1

for document in cursor:
  print (document["user"]["name"])
  print (document["place"])
  var +=1

print (var-1)
