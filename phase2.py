#phase 2

from bsddb3 import db

ad_database = db.DB() #handle for Berkeley DB database
DB_File = "ads_s.db" #our file name
#ad_database.open(DB_File ,None, db.DB_HASH, db.DB_CREATE) #specifying how to use this DB
ad_database.open(DB_File ,None, db.DB_HASH, db.DB_CREATE)
cursor = ad_database.cursor()

filename = "ads_s.txt" #open sorted txt file
file = open(filename, "r")

'''
berkeley_list_1 = []
for row in file:
	#print(row)
	row1 = row.split(":")
	#print(row)
	berkeley_list_1.append(row1)
	
for row in berkeley_list_1:
	item1 = int(row[0])
	item2 = row[1]
	#print(item1 + ", " + item2)
	ad_database.put(item1, item2)
'''
	
#ad_database.put(b"sample", "text")
#ad_database.put(b"free", "shevacadpoo")


#The arguments corresponds to (key, value, flag to insert key-value pair 
iter = cursor.first()
while iter:
	print(iter)
	iter = cursor.next()