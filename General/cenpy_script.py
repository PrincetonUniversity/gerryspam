import cenpy as c
import pandas as pd

#set file type, SF1 or ACS
conn = c.base.Connection('DECENNIALSF12010')

#set empty dataframe to fill
data = pd.DataFrame(columns=['P005001','P005003','P005004','P005010','P011001','P011005','P011006','P011002', 'state', 'county', 'tract', 'block'])

#specifiy which state and counties you want to pull information from
# =============================================================================
# state = '37'
# counties = ['001', '003', '005', '007', '009', '011', '013', '015', '017', '019', '021', '023','025', '027', '029', '031', 
#             '033','035','037','039','041','043','045','047','049','051','053','055','057','059','061','063','065','067','069',
#             '071','073','075','077','079','081','083','085','087','089','091','093','095','097','099','101','103','105','107',
#             '109','111','113','115','117','119','121','123','125','127','129','131','133','135','137','139','141','143','145',
#             '147','149','151','153','155','157','159','161','163','165','167','169','171','173','175','177','179','181',
#             '183','185','187','189','191','193','195','197','199']
# 
# =============================================================================
state = '36'
counties = ['059']
#make census requests and store information in dataframe
for county in counties:
    print(county)
    count_data = conn.query(cols=['P005001','P005003','P005004','P005010','P011001','P011005','P011006','P011002'], geo_unit='block', geo_filter={'state':state, 'county':county})
    data = data.append(count_data)
 
#rename columns
data = data.rename(columns = {'P005001':'tot','P005003':'NHwhite','P005004':'NHblack','P005010':'hispanic',
                              'P011001':'totVAP','P011005':'WVAP','P011006':'BVAP','P011002':'HVAP'})   
#add geoid column  
data['GEOID10'] = data['state']+data['county']+data['tract']+data['block']  

#save file  
data.to_csv('/Volumes/GoogleDrive/Shared drives/princeton_gerrymandering_project/States and local partners/New York/Nassau County/demographics/Nassau_2010_pop.csv')
