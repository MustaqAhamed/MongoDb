import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["tariff"]
mycol = mydb["HS(5)"]

myquery = { "HS(5)": "Cattle"}

mycol.delete_one(myquery)


#print the tariff collection after the deletion:
for x in mycol.find():
  print(x)
