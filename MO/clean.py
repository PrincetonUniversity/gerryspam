import geopandas as gpd
import pandas as pd
import maup

# precinct data 
prec_path = "/Users/hopecj/projects/gerryspam/MO/dat/mo_2016/mo_2016.shp"
prec = gpd.read_file(prec_path)
prec.crs
list(prec.columns) # president, u.s. senate, governor, lt. gov, atg, sect. of state, treasurer
prec.head()

# u.s. congressional data
uscong_path = "/Users/hopecj/projects/gerryspam/MO/dat/cb_2016_us_cd115_5m/cb_2016_us_cd115_5m.shp"
uscong = gpd.read_file(uscong_path)
uscong.crs
uscong.set_index('STATEFP', inplace=True)
mscong = uscong.loc["29"] # filter down to missouri
mscong.rename(columns={"CD115FP": "id"}, inplace=True)
mscong = mscong.reset_index(drop=True)
mscong_merging = mscong[["id", "geometry"]]

# state senate data
state_path = "/Users/hopecj/projects/gerryspam/MO/dat/tl_2016_29_sldu/tl_2016_29_sldu.shp"
state = gpd.read_file(state_path)
state.crs
list(state.columns) # SLDUST is state senate district
state.rename(columns={"SLDUST": "id"}, inplace=True)
state = state[["id", "geometry"]]

# state HOR data? 


# Assigning precincts to U.S. congressional districts
assignment = maup.assign(prec, mscong_merging)
prec["CD115FP"] = assignment
prec.to_file("precincts_testing.shp")

# Assigning precincts to state senate districts
assignment = maup.assign(prec, state)
prec["SLDUST"] = assignment
prec.to_file("precincts_testing.shp")

# population 


