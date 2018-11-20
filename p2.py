#Project 2: oanderso, caboteja
import re


def digest(xmlfile):
   
    filename = xmlfile
    file = open(filename, "r")
    ad_table = []
    
    for row in file: #creates a 2D list (or table) that contains the rows of the xml file. Each row is an ad.
        ad_table.append(row)
    
    #gets rid of the xml info, leaving only the data rows in the table.
    del ad_table[0]
    #del ad_table[1]
    del ad_table[-1]
    
    
    #-----------------------------------------------------------------------------------------
    aid_list = [] #AID lIST
    i = 1
    opentag = "<aid>";
    closetag = "</aid>";
    while (i < len(ad_table)): #creates a list of the AIDs 
    
        frag = re.search(opentag + "(.+?)" + closetag, ad_table[i]);
            
        aid = frag.group(1)
        aid_list.append(aid)
        
        i+=1
       
    #print(aid_list) #debug line
        
    #-----------------------------------------------------------------------------------------    
    title_list = [] #TITLE LIST
    i = 1
    opentag = "<ti>";
    closetag = "</ti>";
    while (i < len(ad_table)): #creates a list of the titles 
    
        frag = re.search(opentag + "(.+?)" + closetag, ad_table[i]); #magical regex thing
            
        title = frag.group(1)
        title_list.append(title)
        
        i+=1
       
    #print(title_list) #debug line
    #-----------------------------------------------------------------------------------------
    date_list = [] #DATE LIST
    i = 1
    opentag = "<date>";
    closetag = "</date>";
    while (i < len(ad_table)): #creates a list of the titles 
    
        frag = re.search(opentag + "(.+?)" + closetag, ad_table[i]); #magical regex thing
            
        date = frag.group(1)
        date_list.append(date)
        
        i+=1
       
    #print(date_list) #debug line
    
    #-----------------------------------------------------------------------------------------
    
    loc_list = [] #LOCATION LIST
    i = 1
    opentag = "<loc>";
    closetag = "</loc>";
    while (i < len(ad_table)): #creates a list of the titles 
    
        frag = re.search(opentag + "(.+?)" + closetag, ad_table[i]); #magical regex thing
            
        loc = frag.group(1)
        loc_list.append(loc)
        
        i+=1
       
    #print(loc_list) #debug line
    
    #-----------------------------------------------------------------------------------------
    
    cat_list = [] #CATEGORY LIST
    i = 1
    opentag = "<cat>";
    closetag = "</cat>";
    while (i < len(ad_table)): #creates a list of the titles 
    
        frag = re.search(opentag + "(.+?)" + closetag, ad_table[i]); #magical regex thing
            
        cat = frag.group(1)
        cat_list.append(cat)
        
        i+=1
       
    #print(cat_list) #debug line
    
    #-----------------------------------------------------------------------------------------
    
    desc_list = [] #DESCRIPTION LIST
    i = 1
    opentag = "<desc>";
    closetag = "</desc>";
    while (i < len(ad_table)): #creates a list of the titles 
    
        frag = re.search(opentag + "(.+?)" + closetag, ad_table[i]); #magical regex thing
            
        desc = frag.group(1)
        desc_list.append(desc)
        
        i+=1
       
    #print(desc_list) #debug line
    
    #-----------------------------------------------------------------------------------------
    
    price_list = [] #PRICE LIST
    i = 1
    opentag = "<price>";
    closetag = "</price>";
    while (i < len(ad_table)): #creates a list of the titles 
    
        frag = re.search(opentag + "(.+?)" + closetag, ad_table[i]); #magical regex thing
            
        price = frag.group(1)
        price_list.append(price)
        
        i+=1
       
    #print(price_list) #debug line
    
    #return information:
    return aid_list, title_list, date_list, loc_list, cat_list, desc_list, price_list
    

def terms_txt (aid_list, title_list, desc_list):
    
    #WHY IS IT SKIPPING OVER THE TERM F4??? ***** CHECK THIS OUT?
    #removes unaccepted terms from title_list. 
    #This loops twice because for some reason only doing it once doesn't remove all the terms < 2 chars long...    
    
    split_title_list = []
    for item in title_list:
        frag = item.split()
        split_title_list.append(frag)
        
    n = 0
    while n < 2: 
        for subset in split_title_list: 
            i = 0
            while i < len(subset):
                #print(subset[i]) #debug line
                if len(subset[i]) <= 2:
                    #print("DELETED: " + subset[i]) #debug line
                    del subset[i]
                i+=1 
            while i < len(subset):        
                if (subset[i] == "&apos;") or (subset[i] == "&quot;") or (subset[i] == "&amp;"):
                    del subset[i]
                i+=1
            
            while i < len(subset):
                if (subset[i][0] == "&") and (subset[i][1] == "#") and (type(subset[i][2])  == int): #THIS DOESN'T WORK YET debug line
                    del subset[i]
                i+=1
            while i < len(subset):
                subset[i].lower()
                i+=1             
        n+=1
             
    #print(split_title_list) #debug line
     
     
     
    #removes unaccepted terms from desc_list.
    
    split_desc_list = []
    for item in desc_list:
        frag = item.split()
        split_desc_list.append(frag)
    
    #print(split_desc_list)    
    n = 0    
    while n < 2: 
        for subset in split_desc_list: 
            i = 0
            while i < len(subset):
                #print(subset[i]) #debug line
                if len(subset[i]) <= 2:
                    #print("DELETED: " + subset[i]) #debug line
                    del subset[i]
                i+=1 
            while i < len(subset):        
                if (subset[i] == "&apos;") or (subset[i] == "&quot;") or (subset[i] == "&amp;"):
                    del subset[i]
                i+=1
            
            while i < len(subset):                
                if (subset[i][0] == "-") and (subset[i][1] == "&") and (subset[i][2] == "#"):  #THIS DOESN'T WORK YET debug line
                    del subset[i]
                i+=1
            while i < len(subset):
                subset[i].lower()
                i+=1 
        n+=1
                 
    
    stl_len = (len(split_title_list)) #same for both lists (10 elements in this case)
    
    #creates the list to be printed
    
    export_file = open("terms.txt", "w+")

    i=0
    while i < stl_len:
        for term in split_title_list[i]:
            #print(term + " : " + aid_list[i])
            export_file.write(term + ":" + aid_list[i] + "\n")
        for term2 in split_desc_list[i]:
            #print(term2 + " : " + aid_list[i])
            export_file.write(term2 + ":" + aid_list[i] + "\n")
        #print("-----") #debug line
        i+=1
        







#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#
def main():
    
    #filename = input("Enter file name: ")
    aid_list, title_list, date_list, loc_list, cat_list, desc_list, price_list = digest("10.xml") #all of these variables are assigned accordingly.
    
    #create terms.txt file
    terms_txt (aid_list, title_list, desc_list)




main()