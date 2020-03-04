import time
import pandas as pd
import geopandas as gpd
import math
import shapely as shp
import warnings
import numpy as np
warnings.filterwarnings("ignore")
import helper_tools as ht
import sys
sys.path.append('/Users/hwheelen/Documents/GitHub/gerrymander-geoprocessing/areal_interpolation')
import areal_interpolation as ai
from collections import Counter



df_tot = pd.DataFrame()
# loop through geocoded voter rolls and combine into one dataframe

geo_path = "/Volumes/GoogleDrive/Shared drives/princeton_gerrymandering_project/geocoding/Geocoded States from Civis Voterroll/geocoded_NJ.csv"
df_geo = pd.read_csv(geo_path)
# Only keep rows that matches were found
df_geo = df_geo[df_geo['is_match'] == 'Match']

# create cenus block geoid
df_geo['GEOID10'] = df_geo['state_fips'].astype(int).map(str).str.zfill(2) + \
                    df_geo['county_fips'].astype(int).map(str).str.zfill(3) + \
                    df_geo['tract'].astype(int).map(str).str.zfill(6) + \
                    df_geo['block'].astype(int).map(str).str.zfill(4)
# create dataframe by dropping unnecessary columns in df_geo dataframe
df = df_geo[['GEOID10','state_fips','county_fips','vb_vf_precinct_id', 'vb_vf_precinct_name','vb_vf_national_precinct_code', 
             'voter_status', 'vf_reg_cd','vf_reg_hd', 'vf_reg_sd']]
df['precinct'] = df['vb_vf_precinct_name']
df = df[['GEOID10','precinct']]

df = df.groupby('GEOID10')['precinct'].apply(list).apply(Counter)
df = pd.DataFrame(df)
df.to_csv('/Volumes/GoogleDrive/Shared drives/princeton_gerrymandering_project/OpenPrecincts/States for site/New Jersey/Geocoded VR/NJ_CivisVR.csv')
