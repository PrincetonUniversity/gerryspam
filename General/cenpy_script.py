import cenpy as c
import pandas as pd

#set file type, SF1 or ACS
conn = c.base.Connection('DECENNIALSF12010')

#set empty dataframe to fill
data = pd.DataFrame(columns=['P005001','P005003','P005004','P005010','P011001','P011005','P011006','P011007','P011008','P011002', 'state', 'county', 'tract', 'block'])

#specifiy which state and counties you want to pull information from and what counties
state = '34' # 34 is NJ's state FIPS code
counties = []

for i in range(1,43,2): # NJ's counties range from 001 to 041 skipping even numbers
    x = str(i).zfill(3)
    counties.append(x)

#make census requests and store information in dataframe
for county in counties:
    print(county)
    count_data = conn.query(cols=['P005001','P005003','P005004','P005005','P005006','P005010','P011001','P011005','P011006','P011007','P011008','P011002'], geo_unit='block', geo_filter={'state':state, 'county':county})
    data = data.append(count_data)
 
#rename columns
data = data.rename(columns = {'P005001':'tot','P005003':'NHwhite','P005004':'NHblack','P005005':'NHnat','P005006':'NHasi','P005010':'hispanic',
                              'P011001':'totVAP','P011005':'WVAP','P011006':'BVAP','P011007':'NatVAP','P011008':'AVAP','P011002':'HVAP'})   
#add geoid column  
data['GEOID10'] = data['state']+data['county']+data['tract']+data['block']  

#save file  
data.to_csv('/Volumes/GoogleDrive/Shared drives/princeton_gerrymandering_project/States and local partners/New Jersey/Shapefiles/Census Data/NJ2010pop_breakdown.csv')






