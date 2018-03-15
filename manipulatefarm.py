import pandas as pd
import string

inpfile = 'Farm - Copy.csv'

gispts = {}

dataframe= pd.read_csv(inpfile)
for i in range(0,len(dataframe)):
    farmid=dataframe['Sno'][i]
    gispts[farmid]=dataframe['GIS'][i]


#REMOVING #.... CONTENT
nohashes = {}
for i in gispts:
    k=[]
    nomins=[]
    k = gispts[i].split(',')
    for j in range(len(k)):
        if('#' in k[j]):
            nomins.append(k[j].split('#')[0])
        else:
            nomins.append(k[j])
    nohashes[i]=nomins

#INFLATION OF SINGLE POINT LANDS
inflated = {}
for i in nohashes:
    if(len(nohashes[i])!=1):
        inflated[i]=nohashes[i]

    elif(len(nohashes[i])==1):
        infpts=[]
        for j in nohashes[i]:
            k=j.split('-')
            x1=str(float(k[0])+0.00004)
            y1=str(float(k[1])-0.00004)
            x2=str(float(k[0])+0.00004)
            y2=str(float(k[1])+0.00004)
            x3=str(float(k[0])-0.00004)
            y3=str(float(k[1])+0.00004)
            x4=str(float(k[0])-0.00004)
            y4=str(float(k[1])-0.00004)
            infpts.append(x1 + ' '+ y1 + ',' + x2 + ' '+ y2 + ',' + x3 + ' '+ y3 + ',' + x4 + ' '+ y4 + ',' + x1 + ' '+ y1 )
        inflated[i]=infpts

#REPLACING '-' and '^' with ' '
formattedpts={}

for i in inflated:
    lit=[]
    for j in inflated[i]:
        if('^' in j):
            j=j.replace('^',' ')
        elif('-' in j):
            j=j.replace('-',' ')
        lit.append(j)
    if( i < 47):
        lit.append(lit[0])
    formattedpts[i]=lit            

strpts = []
for i in formattedpts:
    strpts.append('POLYGON((' +','.join(formattedpts[i]) + '))')

#Changing photostrings ---

for i in range(0,len(dataframe)):
    farmid=dataframe['Sno'][i]
    dataframe['Image'][i]='photos/farm_' + str(farmid) + '.jpg'

#FINAL SAVING of dataframe to csv ---
dataframe=dataframe.assign(Geometry=strpts)
dataframe.to_csv('Farm.csv')      #MAKE SURE THAT ALL PRIVILEGES ARE GIVEN TO USERS in the Operating systems
# AND FARMER.CSV FILE IS NOT OPENED CURRENTLY