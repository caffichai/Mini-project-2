# Project 2: oanderso, caboteja
import re


def digest(xmlfile):
    filename = xmlfile
    file = open(filename, "r")
    ad_table = []

    for row in file:  # creates a 2D list (or table) that contains the rows of the xml file. Each row is an ad.
        ad_table.append(row)
        print(row)

    # gets rid of the xml info, leaving only the data rows in the table.
    del ad_table[0]
    # del ad_table[1]
    # print (ad_table[-1])
    # gets rid of the last item in array
    del ad_table[-1]

    # -----------------------------------------------------------------------------------------
    aid_list = []  # AID lIST
    i = 1
    opentag = "<aid>";
    closetag = "</aid>";
    while (i < len(ad_table)):  # creates a list of the AIDs

        frag = re.search(opentag + "(.+?)" + closetag, ad_table[i]);

        aid = frag.group(1)
        aid_list.append(aid)

        i += 1

    # print(aid_list) #debug line

    # -----------------------------------------------------------------------------------------
    title_list = []  # TITLE LIST
    i = 1
    opentag = "<ti>";
    closetag = "</ti>";
    while (i < len(ad_table)):  # creates a list of the titles

        frag = re.search(opentag + "(.+?)" + closetag, ad_table[i]);  # magical regex thing

        # print(frag.group(1))
        title = frag.group(1)

        title_list.append(title)

        i += 1
    # for line in title_list:
    #     #     print(line) #debug line

    # -----------------------------------------------------------------------------------------
    date_list = []  # DATE LIST
    i = 1
    opentag = "<date>";
    closetag = "</date>";
    while (i < len(ad_table)):  # creates a list of the titles

        frag = re.search(opentag + "(.+?)" + closetag, ad_table[i]);  # magical regex thing

        date = frag.group(1)
        date_list.append(date)

        i += 1

    # print(date_list) #debug line

    # -----------------------------------------------------------------------------------------

    loc_list = []  # LOCATION LIST
    i = 1
    opentag = "<loc>";
    closetag = "</loc>";
    while (i < len(ad_table)):  # creates a list of the titles

        frag = re.search(opentag + "(.+?)" + closetag, ad_table[i]);  # magical regex thing

        loc = frag.group(1)
        loc_list.append(loc)

        i += 1

    # print(loc_list) #debug line

    # -----------------------------------------------------------------------------------------

    cat_list = []  # CATEGORY LIST
    i = 1
    opentag = "<cat>";
    closetag = "</cat>";
    while (i < len(ad_table)):  # creates a list of the titles

        frag = re.search(opentag + "(.+?)" + closetag, ad_table[i]);  # magical regex thing

        cat = frag.group(1)
        cat_list.append(cat)

        i += 1

    # print(cat_list) #debug line

    # -----------------------------------------------------------------------------------------

    desc_list = []  # DESCRIPTION LIST
    i = 1
    opentag = "<desc>";
    closetag = "</desc>";
    while (i < len(ad_table)):  # creates a list of the titles

        frag = re.search(opentag + "(.+?)" + closetag, ad_table[i]);  # magical regex thing

        desc = frag.group(1)
        desc_list.append(desc)

        i += 1

    # for line in desc_list:
    #     print(line)
    # print(desc_list) #debug line

    # -----------------------------------------------------------------------------------------

    price_list = []  # PRICE LIST
    i = 1
    opentag = "<price>";
    closetag = "</price>";
    while (i < len(ad_table)):  # creates a list of the titles

        frag = re.search(opentag + "(.+?)" + closetag, ad_table[i]);  # magical regex thing

        price = frag.group(1)
        price_list.append(price)

        i += 1

    # print(price_list) #debug line

    # -----------------------------------------------------------------------------------------

    no_of_ads = len(aid_list)

    # return information:
    return aid_list, title_list, date_list, loc_list, cat_list, desc_list, price_list, no_of_ads, ad_table


# ---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#
def terms_txt(aid_list, title_list, desc_list):
    # WHY IS IT SKIPPING OVER THE TERM F4??? ***** CHECK THIS OUT?
    # removes unaccepted terms from title_list.
    # This loops twice because for some reason only doing it once doesn't remove all the terms < 2 chars long...

    split_title_list = []
    for item in title_list:
        frag = item.split()
        split_title_list.append(frag)
        print(frag)

    print(split_title_list)

    n = 0
    while n < 2:
        for subset in split_title_list:
            i = 0
            # takes out terms that have a length of less than or equal to 2
            while i < len(subset):
                # print(subset[i]) #debug line
                if len(subset[i]) <= 2:
                    print("DELETED: " + subset[i])  # debug line
                    del subset[i]
                i += 1

            # keep this just in case
            # tries to take out these
            while i < len(subset):
                if (subset[i] == "&apos;") or (subset[i] == "&quot;") or (subset[i] == "&amp;"):
                    print("DELETED: " + subset[i])  # debug line
                    del subset[i]
                i += 1

            while i < len(subset):
                # if (subset[i][0] == "&") and (subset[i][1] == "#") and (type(subset[i][2]) == int): #THIS DOESN'T WORK YET debug line
                #     del subset[i]
                # if (subset[i][0] == "-") and (subset[i][1] == "&") and (subset[i][3] == "#") and (type(subset[i][3]) == int): #THIS DOESN'T WORK YET debug line
                #     del subset[i]

                # if (re.search('^&#+[0-9]', subset[i])) or (re.search('^-&#+[0-9]', subset[i])) or (re.search('^[0-9]+&#+[0-9]', subset[i])):
                #     del subset[i]

                if re.search('^&+#', subset[i]):
                    print("DELETED: " + subset[i])  # debug line
                    del subset[i]

                i += 1

            # Not working either!!!!! Check whole method
            while i < len(subset):
                subset[i].lower()
                i += 1
        n += 1

    # current list is holding list of lists
    #
    # can't do this way because won't hold a bunch of empty arrays
    # len_of_split_title_list = len(split_title_list)
    # print(len_of_split_title_list)
    # special_string_removal_list = []
    # i = 1
    # if i <= len_of_split_title_list:
    #     special_string_removal_list.append([''])
    #     i += 1
    # print(special_string_removal_list)

    # temp list to hold temporary strings
    temp = []
    # special_string_removal_list
    special_string_removal_title_list = []
    # input function to check if have &#number --> becomes empty strings ,
    for each in split_title_list:
        sub_list_len = len(each)
        i = 0
        # debugging lines
        # print(each)
        # print(i)
        # make sure to check each list in current list
        while i < sub_list_len:
            # now looking at list of strings
            # find each &#number
            result = re.findall('&#[0-9]+;', each[i])
            # print(result)  # debugging line
            # ensures that we don't index and try and split on something that isn't there
            if len(result) == 0:
                temp.append(each[i])
            if len(result) > 0:
                already_done = ''
                for y in result:
                    temp2 = each[i].split(y)
                    temp2 = ''.join(temp2)
                    # ensures that won't split and rejoin same strings and add a duplicate to list
                    if already_done != temp2:
                        temp.append(temp2)
                        already_done = temp2
                    # for x in temp2:
                    #     temp.append(x)
            i += 1
        special_string_removal_title_list.append(temp)
        temp = []

    # temp list to hold temporary strings
    temp = []
    # special_string_removal_list
    apos_special_string_removal_title_list = []
    # input function to check if have &#number --> becomes empty strings ,
    for each in special_string_removal_title_list:
        sub_list_len = len(each)
        i = 0
        print(each)
        print(i)
        # make sure to check each list in current list
        while i < sub_list_len:
            # now looking at list of strings
            # find each &#number
            result = re.findall('&apos;', each[i])
            # print(result)  # debugging line
            # ensures that we don't index and try and split on something that isn't there
            if len(result) == 0:
                temp.append(each[i])
            if len(result) != 0:
                temp2 = re.split('[^0-9A-Za-z-_]+', each[i])
                print(temp2)
                temp3 = []
                for w in temp2:
                    # check if empty string and if over length of 2 and doesn't allow them to be appended
                    # lower cases all strings with length > 2
                    if len(w) > 2:
                        temp3.append(w)
                for x in temp3:
                    print(x)
                    temp.append(x)
                    # temp2 = each[i].split(y)
                    # #temp2 = ''.join(temp2) #don't need for &apos, &quot, and & &amp
                    # #since treated as seperator
                    # # ensures won't add duplicate strings to list
                    # # if already_done != temp2:
                    # #     temp.append(temp2)
                    # #     already_done = temp2
                    # for x in temp2:
                    #     temp.append(x)
            i += 1
        apos_special_string_removal_title_list.append(temp)
        temp = []

    # temp list to hold temporary strings
    temp = []
    # special_string_removal_list
    amp_special_string_removal_title_list = []
    # input function to check if have &#number --> becomes empty strings ,
    for each in apos_special_string_removal_title_list:
        sub_list_len = len(each)
        i = 0
        print(each)
        print(i)
        # make sure to check each list in current list
        while i < sub_list_len:
            # now looking at list of strings
            # find each &#number
            result = re.findall('&amp;', each[i])
            print(result)  # debugging line
            # ensures that we don't index and try and split on something that isn't there
            if len(result) == 0:
                temp.append(each[i])
            if len(result) != 0:
                temp2 = re.split('[^0-9A-Za-z-_]+', each[i])
                print(temp2)
                temp3 = []
                for w in temp2:
                    # check if empty string and if over length of 2 and doesn't allow them to be appended
                    # lower cases all strings with length > 2
                    if len(w) > 2:
                        temp3.append(w)
                for x in temp3:
                    print(x)
                    temp.append(x)
            i += 1
        amp_special_string_removal_title_list.append(temp)
        temp = []

    # temp list to hold temporary strings
    temp = []
    # special_string_removal_list
    quot_special_string_removal_title_list = []
    # input function to check if have &#number --> becomes empty strings ,
    for each in amp_special_string_removal_title_list:
        sub_list_len = len(each)
        i = 0
        print(each)
        print(i)
        # make sure to check each list in current list
        while i < sub_list_len:
            # now looking at list of strings
            # find each &#number
            result = re.findall('&quot;', each[i])
            print(result)  # debugging line
            # ensures that we don't index and try and split on something that isn't there
            if len(result) == 0:
                temp.append(each[i])
            if len(result) != 0:
                temp2 = re.split('[^0-9A-Za-z-_]+', each[i])
                print(temp2)
                temp3 = []
                for w in temp2:
                    # check if empty string and if over length of 2 and doesn't allow them to be appended
                    # lower cases all strings with length > 2
                    if len(w) > 2:
                        temp3.append(w)
                for x in temp3:
                    print(x)
                    temp.append(x)
            i += 1
        quot_special_string_removal_title_list.append(temp)
        temp = []

    # temp list to hold temporary strings
    temp = []
    # special_string_removal_list
    other_special_removal_title_list = []
    # input function to check if have &#number --> becomes empty strings ,
    # for each in amp_special_removal_desc_list:
    for each in quot_special_string_removal_title_list:
        sub_list_len = len(each)
        i = 0
        # make sure to check each list in current list
        while i < sub_list_len:
            # now looking at list of strings
            # find each &#number
            result = re.findall('[^0-9A-Za-z-_]+', each[i])
            # print(result)  # debugging line
            # ensures that we don't index and try and split on something that isn't there
            print(each)
            print(result)
            if len(result) == 0:
                low_string = each[i].lower()
                print(low_string)
                temp.append(low_string)
            if len(result) != 0:
                temp2 = re.split('[^0-9A-Za-z-_]+', each[i])
                print(temp2)
                temp3 = []
                for w in temp2:
                    # check if empty string and if over length of 2 and doesn't allow them to be appended
                    # lower cases all strings with length > 2
                    if len(w) > 2:
                        low_string = w.lower()
                        print(low_string)
                        temp3.append(low_string)
                for x in temp3:
                    print(x)
                    temp.append(x)
            i += 1
        other_special_removal_title_list.append(temp)
        temp = []

    # print(split_title_list) #debug line

    # removes unaccepted terms from desc_list.

    split_desc_list = []
    for item in desc_list:
        frag = item.split()
        split_desc_list.append(frag)

    # print(split_desc_list)
    n = 0
    while n < 2:
        for subset in split_desc_list:
            i = 0
            while i < len(subset):
                # print(subset[i]) #debug line
                if len(subset[i]) <= 2:
                    # print("DELETED: " + subset[i]) #debug line
                    del subset[i]
                i += 1
            while i < len(subset):
                if (subset[i] == "&apos;") or (subset[i] == "&quot;") or (subset[i] == "&amp;"):
                    del subset[i]
                i += 1

            while i < len(subset):
                if (subset[i][0] == "-") and (subset[i][1] == "&") and (
                        subset[i][2] == "#"):  # THIS DOESN'T WORK YET debug line
                    del subset[i]
                i += 1
            while i < len(subset):
                subset[i].lower()
                i += 1

        n += 1

    # temp list to hold temporary strings
    temp = []
    # special_string_removal_list
    special_string_removal_desc_list = []
    # input function to check if have &#number --> becomes empty strings ,
    for each in split_desc_list:
        sub_list_len = len(each)
        i = 0
        # debugging lines
        # print(each)
        # print(i)
        # make sure to check each list in current list
        while i < sub_list_len:
            # now looking at list of strings
            # find each &#number
            result = re.findall('&#[0-9]+;', each[i])
            # print(result)  # debugging line
            # ensures that we don't index and try and split on something that isn't there

            if len(result) == 0:
                temp.append(each[i])
            if len(result) > 0:
                already_done = []
                for y in result:
                    temp2 = each[i].split(y)
                    temp2 = ''.join(temp2)

                    # ensures that won't split and rejoin same strings and add a duplicate to list
                    if len(already_done) != 0:
                        for x in already_done:
                            if x != temp2:
                                temp.append(temp2)
                                already_done.append(temp2)
                    else:
                        temp.append(temp2)
                        already_done.append(temp2)
                    # for x in temp2:
                    #     temp.append(x)
            i += 1
        special_string_removal_desc_list.append(temp)
        temp = []

    # temp list to hold temporary strings
    temp = []
    # special_string_removal_list
    apos_special_string_removal_desc_list = []
    # input function to check if have &#number --> becomes empty strings ,
    for each in special_string_removal_desc_list:
        sub_list_len = len(each)
        i = 0
        print(each)
        print(i)
        # make sure to check each list in current list
        while i < sub_list_len:
            # now looking at list of strings
            # find each &#number
            result = re.findall('&apos;', each[i])
            # print(result)  # debugging line
            # ensures that we don't index and try and split on something that isn't there
            if len(result) == 0:
                temp.append(each[i])
            if len(result) != 0:
                temp2 = re.split('[^0-9A-Za-z-_]+', each[i])
                print(temp2)
                temp3 = []
                for w in temp2:
                    # check if empty string and if over length of 2 and doesn't allow them to be appended
                    # lower cases all strings with length > 2
                    if len(w) > 2:
                        temp3.append(w)
                for x in temp3:
                    print(x)
                    temp.append(x)
                    # temp2 = each[i].split(y)
                    # #temp2 = ''.join(temp2) #don't need for &apos, &quot, and & &amp
                    # #since treated as seperator
                    # # ensures won't add duplicate strings to list
                    # # if already_done != temp2:
                    # #     temp.append(temp2)
                    # #     already_done = temp2
                    # for x in temp2:
                    #     temp.append(x)
            i += 1
        apos_special_string_removal_desc_list.append(temp)
        temp = []

    # temp list to hold temporary strings
    temp = []
    # special_string_removal_list
    amp_special_string_removal_desc_list = []
    # input function to check if have &#number --> becomes empty strings ,
    for each in apos_special_string_removal_desc_list:
        sub_list_len = len(each)
        i = 0
        print(each)
        print(i)
        # make sure to check each list in current list
        while i < sub_list_len:
            # now looking at list of strings
            # find each &#number
            result = re.findall('&amp;', each[i])
            print(result)  # debugging line
            # ensures that we don't index and try and split on something that isn't there
            if len(result) == 0:
                temp.append(each[i])
            if len(result) != 0:
                temp2 = re.split('[^0-9A-Za-z-_]+', each[i])
                print(temp2)
                temp3 = []
                for w in temp2:
                    # check if empty string and if over length of 2 and doesn't allow them to be appended
                    # lower cases all strings with length > 2
                    if len(w) > 2:
                        temp3.append(w)
                for x in temp3:
                    print(x)
                    temp.append(x)
            i += 1
        amp_special_string_removal_desc_list.append(temp)
        temp = []

    # temp list to hold temporary strings
    temp = []
    # special_string_removal_list
    quot_special_string_removal_desc_list = []
    # input function to check if have &#number --> becomes empty strings ,
    for each in amp_special_string_removal_desc_list:
        sub_list_len = len(each)
        i = 0
        print(each)
        print(i)
        # make sure to check each list in current list
        while i < sub_list_len:
            # now looking at list of strings
            # find each &#number
            result = re.findall('&quot;', each[i])
            print(result)  # debugging line
            # ensures that we don't index and try and split on something that isn't there
            if len(result) == 0:
                temp.append(each[i])
            if len(result) != 0:
                temp2 = re.split('[^0-9A-Za-z-_]+', each[i])
                print(temp2)
                temp3 = []
                for w in temp2:
                    # check if empty string and if over length of 2 and doesn't allow them to be appended
                    # lower cases all strings with length > 2
                    if len(w) > 2:
                        temp3.append(w)
                for x in temp3:
                    print(x)
                    temp.append(x)
            i += 1
        quot_special_string_removal_desc_list.append(temp)
        temp = []

    # temp list to hold temporary strings
    temp = []
    # special_string_removal_list
    other_special_removal_desc_list = []
    # input function to check if have &#number --> becomes empty strings ,
    # for each in amp_special_removal_desc_list:
    for each in quot_special_string_removal_desc_list:
        sub_list_len = len(each)
        i = 0
        # make sure to check each list in current list
        while i < sub_list_len:
            # now looking at list of strings
            # find each &#number
            result = re.findall('[^0-9A-Za-z-_]+', each[i])
            # print(result)  # debugging line
            # ensures that we don't index and try and split on something that isn't there
            print(each)
            print(result)
            if len(result) == 0:
                if len(each[i]) > 2:
                    low_string = each[i].lower()
                    # print(low_string)
                    temp.append(low_string)
            if len(result) != 0:
                temp2 = re.split('[^0-9A-Za-z-_]+', each[i])
                print(temp2)
                temp3 = []
                for w in temp2:
                    # check if empty string and if over length of 2 and doesn't allow them to be appended
                    # lower cases all strings with length > 2
                    if len(w) > 2:
                        low_string = w.lower()
                        print(low_string)
                        temp3.append(low_string)
                for x in temp3:
                    print(x)
                    temp.append(x)
            i += 1
        other_special_removal_desc_list.append(temp)
        temp = []

    print(other_special_removal_desc_list)

    stl_len = (len(split_title_list))  # same for both lists (10 elements in this case)

    # creates the list to be printed
    export_file = open("terms.txt", "w+")
    i = 0
    while i < stl_len:
        for term in other_special_removal_title_list[i]:
            # print(term + " : " + aid_list[i])
            export_file.write(term + ":" + aid_list[i] + "\n")
        for term2 in other_special_removal_desc_list[i]:
            # print(term2 + " : " + aid_list[i])
            export_file.write(term2 + ":" + aid_list[i] + "\n")
        # print("-----") #debug line
        i += 1


# ---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#

def pdates_txt(aid_list, date_list, cat_list, loc_list, no_of_ads):
    export_file = open("pdates.txt", "w+")
    i = 0
    while i < no_of_ads:
        # print(date_list[i] + ":" + aid_list[i] + ":" + cat_list[i] + ":" + loc_list[i]) debug line
        export_file.write(date_list[i] + ":" + aid_list[i] + ":" + cat_list[i] + ":" + loc_list[i] + "\n")

        i += 1

    # ---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#


def prices_txt(price_list, aid_list, cat_list, loc_list, no_of_ads):
    export_file = open("prices.txt", "w+")
    i = 0
    while i < no_of_ads:
        # print(price_list[i] + ":" + aid_list[i] + "," + cat_list[i] + "," + loc_list[i]) debug line
        export_file.write(price_list[i] + ":" + aid_list[i] + "," + cat_list[i] + "," + loc_list[i] + "\n")

        i += 1
    # ---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#


def ads_txt(aid_list, ad_table, no_of_ads):
    export_file = open("ads.txt", "w+")
    i = 0

    del ad_table[0]

    while i < no_of_ads:
        # print(aid_list[i] + ":" + ad_table[i])
        export_file.write(aid_list[i] + ":" + ad_table[i] + "\n")

        i += 1

    # ---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#


def main():
    # gets data from xml file
    # filename = input("Enter file name: ")
    aid_list, title_list, date_list, loc_list, cat_list, desc_list, price_list, no_of_ads, ad_table = digest(
        "10.xml")  # all of these variables are assigned accordingly.

    # create terms.txt file
    terms_txt(aid_list, title_list, desc_list)

    # creates pdates.txt file
    pdates_txt(aid_list, date_list, cat_list, loc_list, no_of_ads)

    # creates prices.txt file
    prices_txt(price_list, aid_list, cat_list, loc_list, no_of_ads)

    # creates ads.txt file
    ads_txt(aid_list, ad_table, no_of_ads)


main()