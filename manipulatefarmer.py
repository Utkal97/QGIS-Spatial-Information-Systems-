import pandas as pd

inpfile = 'Farmer.csv'

strlatlon = {}

dataframe= pd.read_csv(inpfile)
for i in range(0,len(dataframe['Sno'])):
    farmerid=dataframe['farmer_id'][i]
    strlatlon[farmerid]=dataframe['farmergps'][i]

#splitting into Latitutdes and Longitudes
lat = []
lon =[]
   
for i in strlatlon:
    lat.append(float(strlatlon[i][0:14]))
    if(strlatlon[i][19]=='-'):
        lon.append(float(strlatlon[i][20:34]))
    elif(strlatlon[i][18]=='-'):
        lon.append(float(strlatlon[i][19:33]))
    elif(strlatlon[i][17]=='-'):
        lon.append(float(strlatlon[i][18:32]))
    elif(strlatlon[i][16]=='-'):
        lon.append(float(strlatlon[i][17:31]))

#Changing photostrings ---

for i in range(0,len(dataframe['Sno'])):
    farmerid=dataframe['farmer_id'][i]
    dataframe['FarmerImage'][i]='photos/farmer_' + str(farmerid) + '.jpg'
    print(dataframe['FarmerImage'][i])

#ADDING LIVESTOCK TO FARMER SECTION---
livestockfile= 'Livestock.csv'

lsdataframe = pd.read_csv(livestockfile)

Cow = {}
Buffalo = {}
Hen = {}
Goat = {}
Sheep = {}
DesiCow= {}

for i in range(0, len(lsdataframe)):
    farmerid=lsdataframe['farmer_id'][i]

    if(int(lsdataframe['livestock_id'][i]) == 1):
        Hen[farmerid]=int(lsdataframe['no_of_livestock'][i])
    elif(int(lsdataframe['livestock_id'][i]) == 2):
        Cow[farmerid]=int(lsdataframe['no_of_livestock'][i])
    elif(int(lsdataframe['livestock_id'][i])== 3):
        Goat[farmerid]=int(lsdataframe['no_of_livestock'][i])
    elif(int(lsdataframe['livestock_id'][i])==4):
        Buffalo[farmerid]=int(lsdataframe['no_of_livestock'][i])
    elif(int(lsdataframe['livestock_id'][i])==6):
        Sheep[farmerid]=int(lsdataframe['no_of_livestock'][i])
    elif(int(lsdataframe['livestock_id'][i])==7):
        DesiCow[farmerid]=int(lsdataframe['no_of_livestock'][i])

#Putting them into lists ----
Cowlist = []
Buffalolist = []
Henlist = []
Goatlist = []
Sheeplist = []
DesiCowlist = []

for i in range(len(dataframe)):
    farmerid=dataframe['farmer_id'][i]
    if(farmerid in Hen):
        Henlist.append(Hen[farmerid])
    else:
        Henlist.append(0)

    if(farmerid in Cow):
        Cowlist.append(Cow[farmerid])
    else:
        Cowlist.append(0)

    if(farmerid in Buffalo):
        Buffalolist.append(Buffalo[farmerid])
    else:
        Buffalolist.append(0)
    
    if(farmerid in Sheep):
        Sheeplist.append(Sheep[farmerid])
    else:
        Sheeplist.append(0)
    
    if(farmerid in DesiCow):
        DesiCowlist.append(DesiCow[farmerid])
    else:
        DesiCowlist.append(0)

    if(farmerid in Goat):
        Goatlist.append(Goat[farmerid])
    else:
        Goatlist.append(0)

#FINAL SAVING of dataframe to csv ---
dataframe=dataframe.assign(Longitudes=lon,Latitudes=lat,Buffalo=Buffalolist,Cow=Cowlist,DesiCow=DesiCowlist,Goat=Goatlist,Hen=Henlist,Sheep=Sheeplist)
dataframe.to_csv('Farmer.csv')      #MAKE SURE THAT ALL PRIVILEGES ARE GIVEN TO USERS in the Operating systems
# AND FARMER.CSV FILE IS NOT OPENED CURRENTLY