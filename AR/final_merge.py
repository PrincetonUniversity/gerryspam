import geopandas as gpd
import pandas as pd
import numpy as np
import re

shp_path = "/Users/hopecj/projects/AR/Shapefiles/4_merged/ar18.shp"
elec_path = "/Users/hopecj/projects/gerryspam/AR/AR_G18.csv"


elec_df = pd.read_csv(elec_path)
shp_df = gpd.read_file(shp_path)

elec_df["elec_loc_prec"] = elec_df["county"] + "," + elec_df["precinct"].str.lower()

shp_df["shp_loc_prec"] = shp_df["county_nam"] + "," + shp_df["PREC"].str.lower()

out = shp_df.merge(elec_df, left_on='shp_loc_prec', right_on='elec_loc_prec', how='outer')

out = out.drop(["geometry"], axis=1)
out.to_csv("/Users/hopecj/projects/gerryspam/AR/testing_merged.csv")