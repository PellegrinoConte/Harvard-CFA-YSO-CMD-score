read me for use with CMDS1.py, radius.py, opencsv.py, and writer.py.

Pellegrino Conte
Harvard Smithsonian CFA
Working under Lynn Carlson
6/16/15

INTRO
				CMD Score Calculation For YSO’s 

A CMD(color magnitude diagram) score is evaluated based on the distance in color- magnitude space between a source and other plotted objects. For each young stellar object(YSO), a CMD plot is formed and it is plotted along with a separate group of stellar objects such as galaxies. A circle is then created, centered at the YSO source and having a radius such that the perimeter of the circle encapsulates 5% of the other plotted objects. The radius of this circle is considered the CMD score for this particular YSO, Object list, and CMD plot group. Each YSO was compared to four different object lists(RGB, AGB, Massive stars and galaxies) and plotted on 5 different CMDs(3.6x(3.6-5.8), 4.5x(4.5-5.8), 8.0x(4.5-8.0), 4.5x(4.5-24)). CMD scores for each YSO and object list group are obtained by obtaining the mean of the 5 scores when they are analyzed on the different CMDs. This score given to the YSO and Object group is then scaled based on how much information was provided the YSO. If all 5 CMDs could be created then it would be scaled by 5/5. If only four were produced it would be scaled by 4/5 and so on. The CMD score for each YSO is obtained by selecting the smallest score from each YSO object score. The algorithm to process this score is designed to provide the same score as the proses used in the paper "Surveying The Agents Of Galaxy Evolution In The Tidally Stripped, Low Metallicity Small Magellanic Cloud (Sage-Smc). Iii. Young Stellar Objects." ApJ The Astrophysical Journal 778.1 (2013) as to allow for comparison between the two sources. 

The idea behind the code is that the closer a potential YSO is in color magnitude space to known objects such as massive stars the less likely it is that it is in fact a YSO. If a YSO has a particularly high score it would be farther away from these determined objects and thus increasing the chance that is is not these pre-determined objects. The scale is incorporated to account for potential YSOs with less data as we are incapable of providing the same certainty given to other potential YSO. 


Bibliography
Sewiło, M., L. R. Carlson, J. P. Seale, R. Indebetouw, M. Meixner, B. A. Whitney, T. P. Robitaille, J. M. Oliveira, K. Gordon, M. R. Meade, B. L. Babler, J. L. Hora, M. Block, K. Misselt, J. Th. Van Loon, C.-H. R. Chen, E. Churchwell, and B. Shiao. "Surveying The Agents Of Galaxy Evolution In The Tidally Stripped, Low Metallicity Small Magellanic Cloud (Sage-Smc). Iii. Young Stellar Objects." ApJ The Astrophysical Journal 778.1 (2013): 15. Web.




1. What you should have
a.
hopefully this document is in a file that also has these other python files
	-CMDS1.py (script that brings together the other functions listed)
	-radius.py
	-opencsv.py
	-writer.py
and it might have some other csv files that will allow this to run as is to show you what it can do
b. This program is designed to have all its files in one folder, data py files, everything
c. if it doesn’t have the files listed above then you should find them


2. basic overview
a.
this program is designed to work by taking a csv file of Yso names, and the following magnitudes in this order —> 3.6, 4.5, 5.8, 8.0, 24 ,  and compare it to several csv files of galaxies and stars and what not in the same format.
b.
if you don’t have data for a magnitude the null value is 99.999, if you have something else set, go into radius.py and replace every instance of 99.999 to your null value
c. 
####read this######
The program takes the yso file that it opened and sorts it into a 2d array( a python list) and does the same for the object file. it takes the two and creates a plot for each potential yso  with all of the objects and the yso plotted in color space it finds the smallest radius that will produce a circle with the center point being the potential yso and whose area encapsulates 5% of the objects. it does this for each yso for every yso lit object list pair and then finds the smallest radius for each yso out of the yso-object pairs, it then scales the values based on how much data we have for each yso. this is then printed out to a csv file that contains the yso name score and scaled score. 
d.
It might be in your best interest to go through each file and look over it so you understand whats going on, the code is very simple and even if you don’t know python it is helpful to just read the comments. 

3. What you need to do, pre-run
-READ THE COMMENTS IN ALL THE PY FILES
a.
if your lucky there should be example files in this folder, run the CMDS1.py file, it might take a while to run based on you computers processing power. open the Report.csv file and there should be values in there. this will help you understand how everything works. 
b. 
you can use csv files or 2d arrays with the format listed in 2.a, if you use 2d arrays you will need to change CMDS1.py a little and won’t need opencsv.py
c.
this code does most of the math in radius.py, it has a optimal parameter combos which is set so that with the format listed in 2.a it will create several plots and average them, the plots it will create are:3.6x(3.6-5.8), 4.5x(4.5-5.8), 8.0x(4.5-8.0), 4.5x(4.5-24), 8.0x(8.0-24), for this the combos parameter for the radius function is combos = [[1, 1, 3], [2, 2, 3], [4, 2, 4], [2, 2, 5], [4, 4, 5] ], where each index in combos holds a list of the indexes in the datalist and yso 2d list of the desired wavelength, ex. yso[1] has the mag3.6 values. if you want different combos change combos.
d.
CMDS1.py pulls all the functions together and does some basic math, you’ll need to change that if your filenames are different or if you don’t have four objects lists you are comparing it to . 
e.
You’ll have to put your csv files and all data in the same file as the rest of these python documents. 

4. What you will need to do to run
a. 
you should have all your files in the same folder and ready to go. 
b.
you can open a IDE and run CMDS1.py from there and it should run and put the value in whatever you set as the print csv file.
c.
if you have a mac, open terminal and you’ll need to change your working directory to the file that contains all the files. in terminal type ‘pwd’ to see your current directory, type ‘cd FILEPATH’ where FILEPATH is something like /Users/username/Documents/program/file , to change the working directory,once your wiring directory is set type the following 
	>>> python
	>>> import CMDS1
d.
if you are using windows or linux, google how to run a python file. 

5. In Conclusion
a.
please give me credit if this is used
b. 
feel free to improve/modify it
c.
questions, concerns, email me at pellecnt@gmail.com
d.
thank you 

—Pellegirno Conte
 Studying Optics at University of Rochester
 6/15/15






