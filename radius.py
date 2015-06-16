#Pellegrino Conte, 5/28/15
#code for opining csv files into probably arrays but we'll see what ends up happinign
#Runs on python 3.4
#Last updated on 6/4/15 by Pellegirno Conte
#radius.py .2.5
#For use with CMDS.py
#imports
import math


#############################################
#############################################
#Start Code


#Radius , desigend for a already opened csv file to be used as input,

def radius(datalist, yso, combos = [[1, 1, 3], [2, 2, 3], [4, 2, 4], [2, 2, 5], [4, 4, 5] ], printbool = True ):
    #                                               **IMPORTANT**
    # -radius2() takes in two 2D arrays.
    #-The arrays first value, (array[0]) should contain an arrat with the names of each row, not that it matters. However data in that first slot is ignored
    #-I also assume that if you read a csv file or any file for that mater you also changes the numberical values to type int.
    # - combos is the differenc CMD graph combinations [1, 2, 3] --> 1 is the y axis, 2-3 is the x axis, 1 = 3.6, 2= 4.5, 3 = 5.8, 4 = 8.0, 5 = 24 micrometers
    #- Set printbool to false to stop printing progress during run.
    #-The format for datalist and yso should be [ ID or starnae,  3.6, 4.5,  5.8,  8.0,  24 ], if it is not in that order this will not give you correct results.
    #- the returned value R will give back the a 7x len(yso) 2d array composed of
    #    ['ID', '3.6x(3.6-5.8)', '4.5x(4.5-8.0)', '8.0x(4.5-8.0)','4.5x(4.5-24)', '8.0x(8.0-24)', 'average', 'scaled average']   (this is the first entity, R[0])
    # -if a star has no data for a certian wavelength that value should be 99.999.
    #                                               **WHAT IT DOES**
    # -   Using CMD plots it 'plots out'(doesnt plot anything) 5 different wavelength combos of ...
    #   the datalist elements and one YSO element and finds the smallest radius from the yso element...
    #   in color-space that creates a cirlcle emclosing 5% of the number of elements in the datalist whether ...
    #   it's massive stars, galaxys, RGB ect.
    #                                                        **WHY**
    # -Farther away a YSO(young steller object) is from other opbjects in color-space, the more lilkly it is a YSO
    
    
    #temp vars
    radius = 0
    dist = 0
    stars = len(yso)-1
    p = int(stars*.05)
    R = [None]*stars
    
    

    #main loop
    
    for combo in combos:
        D = [0]
        #counter for printing progress
        counter  = 0

        #loop through YSO
        for i in yso[1:]:
            counter +=1
            if printbool:
                print("%d  %d|%d" % (combos.index(combo), counter , len(yso)) )
            index = yso.index(i)
            D = [0]
            #loop through astronomical objects 
            for j in (datalist[1:]):

                #checks to see if we even have the data
                if (j[combo[1] ] <100 and j[ combo[1] ]>99.9) or (j[ combo[2] ] <100 and j[ combo[2] ] >99.9) or (i[ combo[1] ] <100 and i[ combo[1] ]   >99.9) or (i[ combo[2] ] <100 and i[ combo[2]]   >99.9):
                    dist = 99.999
                else:
                    #calc distance from YSO  i to object j in color-space
                    dist = (  (j[ combo[0] ]-i[ combo[0] ])**2+((j[ combo[1]  ]-j[ combo[2] ])-(i[ combo[1] ]-i[ combo[2] ]))**2  )**.5
                D.append(dist)
                
            
            
            #takes the distance that would contin 5%( =(p+1) ) of non-YSOs
            D.sort()

            if combos.index(combo) == 0:
                R[index-1] = [i[0], D[p+1]]
            else:               
                R[index-1].append( D[p+1] )

    #done with main loop
        
  

    print('cacluating Averages...')

    #Side loop
    for index, elem in enumerate(R):
        #calc avrg radius
        summ = 0
        total=0
        if elem[1] != 99.999:
            summ+= elem[1]
            total+=1
        if elem[2] != 99.999:
            summ+= elem[2]
            total+=1
        if elem[3] != 99.999:
            summ+= elem[3]
            total+=1
        if elem[4] != 99.999:
            summ+= elem[4]
            total+=1
        if elem[5] != 99.999:
            summ+= elem[5]
            total+=1
        
        
        if total == 0:
            R[index].append(99.999)
            R[index].append(0)
        
        else:
            #average radius
            R[index].append( summ/total  )
            # -scaled radius --> this is used to scale back distances with less data than we would like, ie smaller radius less chance,
            #  so less data less shoure we are so we also lessen the radius
            R[index].append( summ/5 )
    #inserts title row
    insert = ['ID', '3.6x(3.6-5.8)', '4.5x(4.5-8.0)', '8.0x(4.5-8.0)','4.5x(4.5-24)', '8.0x(8.0-24)', 'average', 'scaled average']
    R.insert(0, insert )
    print('done!')


    return R

#End Code
#############################################
#############################################



