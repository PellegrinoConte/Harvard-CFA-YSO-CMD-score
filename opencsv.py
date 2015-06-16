
#Pellegrino Conte, 5/28/15
#code for opining csv files into probably arrays but we'll see what ends up happinign
#python 3.4
#Last updated on 6/4/15 by Pellegirno Conte
#opencsv.py .1.3
#For use with CMDS.py
#imports
import csv
import math


#############################################
#############################################
#Start Code


def opencsv(filename, elements = []):
#                                                   **IMPORTANT**
#-filename ex. 'data.csv', removing elements, ex elements = [1, 2] will remove 2 and 3rd collums
#- opens file placing each collumn into its own array
#-The first row of the csv file is assumed to contain the names of the collumns thus are kept as strings
#- returns a 2d array final[ csv file total column ][ csv total row num ]
    data = open(filename, 'r')
    csvData = csv.reader(data)
    final = []
    #set up final

    for row in csvData:
        final.append([])
        numn = 0;
        num = 0
        #throughs csv file into an array
        while num < len(row):
            if elements.count(num) == 0:
                final[len(final)-1].append(row[num])
            num+=1
    #cast values to float, exept first ro
    for index, num in enumerate(final[1:]):
        l = 1
        while l < len(num):
            final[index+1][l] = float(num[l])
            l+=1
    
    
    return(final)

#end code
#############################################
#############################################


