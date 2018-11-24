#phase 3
from bsddb3 import db


def digest(): #opens the database

	print("Opening idx files...\n")

	database1 = db.DB() #handle for Berkeley DB database
	database2 = db.DB()
	database3 = db.DB()
	database4 = db.DB()
	
	DB_File = "ad.idx" #our file name
	database1.open("ad.idx")
	
	DB_File = "te.idx" #our file name
	database2.open("te.idx")
	'''
	DB_File = "da.idx" #our file name
	database3.open("pr.idx")
	
	DB_File = "pr.idx" #our file name
	database4.open("pr.idx")
	'''
	#database.open(DB_File ,None, db.DB_HASH, db.DB_CREATE) #another way to do it
	cursor = database2.cursor()

	#check idx database
	iter = cursor.first()
	while iter:
		print(iter)
		iter = cursor.next()
		
	return cursor
	

	
def search(cursor):

	search_term = input("search the term you want: ")  
	
	ping = cursor.set(search_term.encode("utf-8"))  #search for the search_term
	#print("Query: " + str(ping[0].decode("utf-8")) + "  AID: " + str(ping[1].decode("utf-8")))
	
	if ping != None:
		print("Query: " + str(ping[0].decode("utf-8")) + "  AID: " + str(ping[1].decode("utf-8"))) #puts cursor on first hit and prints it
		
		dup = cursor.next_dup() #prints any other hit terms
		while(dup != None):
			print("Name: " + str(ping[0].decode("utf-8")) + "  AID: " + str(ping[1].decode("utf-8")))
			dup = cursor.next_dup()
			
	else:
		print("No results!")

def main():
	
	#open the 4 idx files
	cursor = digest() 
	search(cursor)
	
	print("\nComplete.\n")
	
	#give opened database to 
	
main()


















