import pandas as pd
import geopandas as gpd

#load in file
fp = '/Volumes/GoogleDrive/Shared drives/princeton_gerrymandering_project/OpenPrecincts/States for site/Georgia/2016/VEST/ga_2016/ga_2016.shp'

df = gpd.read_file(fp)

#get statewide totals
pres_tot = (df.G16PREDCli.sum(),df.G16PRERTru.sum())
sen_tot = (df.G16USSDBar.sum(),df.G16USSRIsa.sum())

#get county totals
counties = df.COUNTY.unique()

for county in counties:
    county_df = df.loc[df.COUNTY == county]
    county_tot = (county_df.G16PREDCli.sum(),county_df.G16PRERTru.sum())
    print(county,county_tot)
    
#when there are congressional results    
# =============================================================================
# districts = df.DISTRICT.unique()
# 
# for district in districts:
#     dist_df = df.loc[df.DISTRICT == district]
#     dist_tot = (dist_df.G16PREDCli.sum(),dist_df.G16PRERTru.sum())
#     print(dist,dist_tot)
# =============================================================================
