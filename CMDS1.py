#Pellegrino Conte, 5/28/15
#code for opining csv files into probably arrays but we'll see what ends up happinign
#python 3.4
#Last updated on 6/15/15 by Pellegirno Conte
#CMDScore.py  .2.5

#imports
import csv
import math
from opencsv import *
from radius import *
from writer import *

'''
##################################
#                   READ THIS                       #
1) There should be a readme.txt file with this code, you might want to read it.
2) There are certian things you will need to change torun this program
    a) they will be indicated by '--->'
3) this script needs other functions which are mentioned in the readme.txt
4) reading the comments will be benifical
5) this code takes into consideration 4 different types of stellar objects, if you need less or more follow the pattern established
6) if what is being printed is bothering you, delete it, it is not nessisary.
'''

#######StartCode##########
print('Started')
#---> change the name of the text file to the name of your file that contains your yso's and mag data
# --> the list must be in the format Sourcename, magnitudes...,
#--> the python list holds the indexs of collums I did not want to include from the opriginal document
#--> if you wish to include the entire csv file ommit this paramiter, ie opencsv('filename.csv')

#ysoData is a 2d array of sourcename, mag3.6, mag4.5, mag5.8, mag8.0, mag24
ysoData = opencsv('YSOfull.csv', [2, 4, 6, 8, 10]) #[2, 4, 6, 8, 10 ] are dMags
#--> if you have the ysodata already in a 2d array you may comment the line above out and just set ysodata to that


#r Massive Stars
#--> change paramiters to fit your needs
ms = opencsv('bonanosfull.csv')
R1 =  radius( ms , ysoData)


#r galaxys
#--> change paramiters to fit your needs
galaxyData = opencsv('galaxyfull.csv', [1, 2])
R2=  radius(galaxyData, ysoData)


#r type  RGB
#--> change paramiters to fit your needs
RGBData = opencsv('RGBfull.csv', [0, 2, 3, 4])
R3 = radius( RGBData, ysoData)


#r type AGB
#--> change paramiters to fit your needs
AGBData = opencsv('AGBfull.csv', [0, 2, 3, 4])
R4 = radius( AGBData, ysoData)


Rf = []

#takes the 4 returned arays from the radius calls and finds the smallest returned value for each yso
#--> youll need to change the following while loop if you don't use 4 different list against the yso list.
i = 1
print('SortingData...')
while i < len(R1):
    if i%2==1: 
        print('.')
    elif i%2 == 0:
        print('-')
    row = [R1[i][0]]
    if R1[i][6]<=R2[i][6] and R1[i][6]<=R3[i][6] and R1[i][6]<=R3[i][6]and R1[i][6]<=R4[i][6]:
        row.append(R1[i][6])
        row.append(R1[i][7])
    elif R2[i][6]<=R1[i][6] and R2[i][6]<=R3[i][6] and R2[i][6]<=R3[i][6] and R2[i][6]<=R4[i][6]:
        row.append(R2[i][6])
        row.append( R3[i][7])
    elif R3[i][6]<=R2[i][6] and R3[i][6]<=R1[i][6] and R3[i][6]<=R3[i][6] and R3[i][6]<=R4[i][6]:
        row.append(R3[i][6])
        row.append(R3[i][7])
    elif R4[i][6]<=R2[i][6] and R4[i][6]<=R3[i][6] and R4[i][6]<=R3[i][6] and R4[i][6]<=R1[i][6]:
        row.append(R4[i][6])
        row.append(R4[i][7])
    else:
        row.append(99.999)
        row.append(99.999)
    Rf.append(row)
    i+=1
print('Writing Data')

#writes out the code to report.csv
#--> have an empty csv file in the same file as this script
#--> if you only use one source change rf to whatever you named the retun value from the radius() functionyou called on your source
writer('Report.csv', Rf)
print('Done!!')






    
