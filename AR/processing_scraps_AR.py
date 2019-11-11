import geopandas as gpd
import pandas as pd
import numpy as np
import re

shp_path = '/Users/hopecj/projects/AR/Shapefiles/AR Precincts 10_11_2019/ELECTION_PRECINCTS.shp'
elec_path = '/Users/hopecj/projects/AR/elections/AR_G18.csv'

elec_df = pd.read_csv(elec_path)

shp_df = gpd.read_file(shp_path)
shp_df = shp_df[['county_nam', 'precinct','geometry']]

shp_df.groupby(['county_nam']).ngroups #sigh.....75 counties

# arkansas cnty
c1 = shp_df.loc[shp_df['county_nam'] == 'Arkansas']
c1['precinct'] = c1['prec_new'].str.upper()
c1['prec_new'] = c1['prec_new'].str.slice(start = 5)
c1.replace({
       'DEWITT 1': 'DEWITT WARD 1',
       'DEWITT 2': 'DEWITT WARD 2',
       'DEWITT 3': 'DEWITT WARD 3',
       'STUTTGART 1': 'STUTTGART WARD 1',
       'STUTTGART 2': 'STUTTGART WARD 2', 
       'STUTTGART 3': 'STUTTGART WARD 3'
})

# ashley cnty
c2 = shp_df.loc[shp_df['county_nam'] == 'Ashley']
c2['prec_new'] = c2['precinct'].str.upper()
c2['prec_new'] = c2['prec_new'].str.slice(start = 5)
c2.replace({
       'CROSSETT WARD 1': 'CW 1',
       'CROSSETT WARD 2': 'CW 2',
       'CROSSETT WARD 3': 'CW 3',
       'FOUNTAIN HILL CITY': 'FH CITY',
       'FOUNTAIN HILL CITY': 'FH RURAL',
       'HAMBURG WARD 1': 'HW1',
       'HAMBURG WARD 2': 'HW2',
       'HAMBURG WARD 3': 'HW3',
       'MT. ZION': 'MT ZION',
       'NORTH CROSSETT EAST': 'NCE',
       'NORTH CROSSETT WEST': 'NCW',
       'SNYDER / TRAFALGAR': 'SNY/TRA',
       'VO - TECH': 'VOTECH',
       'WEST CROSSETT RURAL': 'WCR'
})

# baxter cnty
c3_elec = elec_df.loc[elec_df['county'] == 'Baxter']

c3 = shp_df.loc[shp_df['county_nam'] == 'Baxter']
c3['prec_new'] = c3['precinct'].str.upper()
c3.sort_values(by=['prec_new'])



















geo_precincts = shp_df['precinct']
geo_precincts = geo_precincts.str.lower()
split_geo_precincts = geo_precincts.str.split(r'(.*?-)')

restrung_geo_prec = []

for prec in split_geo_precincts: 
       if len(prec) > 1:
              if len(prec[1]) == 4: # this should really be: list item = number, number, dash 
                     del prec[1]
                     #print (prec)
                   #  ''.join(prec)
                  #   print(prec)
                     restrung_geo_prec.append(prec)

       

np.where(geo_precincts.str.contains('-'), re.search(regex, geo_precincts),  geo_precincts)

cleaned_geo_precincts = re.search(regex, geo_precincts, re.VERBOSE)



shp_df['shp_loc_prec']=elec_df['county'].map(str) + ',' + elec_df['precinct']

### issues ###
# - mississippi county 
# -  


elec_df = pd.read_csv(elec_path)
elec_df['NAME'] = elec_df['NAME'].str.strip()
elec_df = elec_df[['NAME', 'precinct', 'G18DGOV', 'G18RGOV', 'G18LGOV',
       'G18DHOR', 'G18RHOR', 'G18DStSEN', 'G18RStSEN', 'G18DStHou',
       'G18RStHou', 'G18LStHou', 'G16DPRS', 'G16RPRS', 'G16LPRS', 'G16GPRS',
       'G16CPRS', 'G16NPPRS', 'G16NAPRS', 'G16DSEN', 'G16RSEN', 'G16LSEN',
       'G16NASEN', 'G16NPSEN', 'G16DHOR', 'G16RHOR', 'G16LHOR', 'G16NAHOR',
       'G16NPHOR', 'G16DStHou', 'G16RStHou', 'G16CStHou', 'G16IStHou',
       'G16NAStHou', 'G16NPStHou', 'G14RGOV', 'G14CGOV', 'G14LGOV', 'G14NAGOV',
       'G14NPGOV', 'G14DSEN', 'G14RSEN', 'G14LSEN', 'G14NASEN', 'G14NPSEN',
       'G14DHOR', 'G14RHOR', 'G14LHOR', 'G14NPHOR', 'G14DStSEN', 'G14RStSEN',
       'G14NAStSEN', 'G14NPStSEN', 'G14DStHou', 'G14RStHou', 'G14CStHou',
       'G14LStHou', 'G14NAStHou', 'G14NPStHou']]


#elec_df['precinct']=elec_df['precinct'].str.title().str.strip()
#csv_df['com_col']=csv_df['shp'].astype(int)

merged = pd.merge(shp_df, elec_df, on='NAME', how = 'outer')


merged.to_file('/Volumes/GoogleDrive/Shared drives/princeton_gerrymandering_project/OpenPrecincts/States for site/Alaska/Final/AK_Prec_G14_16_18.shp')
#merged.to_csv('/Volumes/GoogleDrive/Shared drives/princeton_gerrymandering_project/OpenPrecincts/States for site/Alaska/Final/AK_Prec_G14_16_18_test.csv')

for i in shp_df:
   geom = shp_df['geometry']
   if geom.geom_type=='MultiPolygon':
      print(geom)
