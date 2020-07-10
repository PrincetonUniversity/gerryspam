import pandas as pd 
import geopandas as gpd
import maup 

# 2018 from https://censusreporter.org/data/table/?table=B03002&geo_ids=620|04000US34&primary_geo_id=04000US34#valueType|estimate
# 2010 from decennial census aggregated to districts
dat = gpd.read_file("/Users/hopecj/projects/gerryspam/NJ/dat/NJDist1018Demographics.geojson")
dat['white10'] = dat['white10'].astype('float64')
dat['black10'] = dat['black10'].astype('float64')
dat['asian10'] = dat['asian10'].astype('float64')
dat['hisp10'] = dat['hisp10'].astype('float64')
dat["Hisp"][32] = 43.0

dat["white_change"] = dat["NHWhite"] - dat["white10"]
dat["hisp_change"] = dat["Hisp"] - dat["hisp10"]
dat["black_change"] = dat["NHBlack"] - dat["black10"]
dat["asian_change"] = dat["NHAsian"] - dat["asian10"]


dat["NEW_DIST"] = dat["DISTRICT"].str[1:]


for_table = dat[["DIST_NAME", "DISTRICT", 
                'white_change', 'hisp_change', 'black_change', 'asian_change']]

for_table.to_csv("/Users/hopecj/projects/gerryspam/NJ/dat/district-demo_changes.csv")

dat.to_file("/Users/hopecj/projects/gerryspam/NJ/dat/district_demo_changes.shp")