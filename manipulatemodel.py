import pandas as pd
import chardet
#THIS IS NOT IN utf8 ENCODING , SO WE NEED TO FIND WHICH ENCODING HAS BEEN USED AND DECODE ACCORDINGLY
with open('Model.csv', 'rb') as f:
    result = chardet.detect(f.read())

inpfile = 'Model.csv'

strlatlon = {}
dataframe= pd.read_csv(inpfile, encoding=result['encoding'])
for i in range(0,len(dataframe)):
    modelid=dataframe['model_tr_id'][i]
    strlatlon[modelid]=dataframe['GPS'][i]

#SPLITTING LATs AND LONs
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


#CHANGING PHOTO STRINGS ---

for i in range(0,len(dataframe)):
    modelid=dataframe['model_tr_id'][i]
    dataframe['Image'][i]='photos/model_' + str(modelid) + '.jpg'

#FINAL SAVING of dataframe to csv ---
dataframe=dataframe.assign(Longitudes=lon,Latitudes=lat)
dataframe.to_csv('Model.csv')      #MAKE SURE THAT ALL PRIVILEGES ARE GIVEN TO USERS in the Operating systems
# AND FARMER.CSV FILE IS NOT OPENED CURRENTLY