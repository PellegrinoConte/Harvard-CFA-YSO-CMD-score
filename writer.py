#Pellegrino Conte, 5/28/15
#code for opining csv files into probably arrays but we'll see what ends up happinign
#python 3.4
#Last updated on 6/4/15 by Pellegirno Conte
#writer.py .1.1
#For use with CMDS.py
#imports
import csv
import math


#############################################
#############################################
#Start Code

#Use to get the usefull stuff
def writer(filename, R):
    #                                           **IMPORTANT**
    #- this code writes the array R to the filename parameter, make filename a csv file or this might not work
    #-the file filename shold aready be made and empty and in the same file as this document
    report = open(filename, 'w')
    fieldnames = ['ID', 'avg', 'savg' ]
    w = csv.DictWriter(report, fieldnames=fieldnames)
    for row in R:
        w.writerow({'ID':row[0], 'avg' :row[1], 'savg':row[2]})





#use if you want to print out all data 
def writer2(filename, R):
    report = open(filename, 'w')
    fieldnames = ['ID', '3_6', '4_5', '8_0','4_52' ,'24', 'avg', 'savg' ]
    w = csv.DictWriter(report, fieldnames=fieldnames)
    for row in R:
        w.writerow({'ID':row[0], '3_6':row[1], '4_5':row[2], '8_0':row[3],'4_52':row[4],  '24':row[5], 'avg' :row[6], 'savg':row[7]})

     
#end code
#############################################
#############################################

