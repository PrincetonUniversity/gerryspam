import geopandas as gpd
import pandas as pd
import maup
import os

# precinct data 
prec_path = "/Users/hopecj/projects/gerryspam/MO/dat/mo_2016/mo_2016.shp"
prec = gpd.read_file(prec_path)
prec.crs
list(prec.columns) # president, u.s. senate, governor, lt. gov, atg, sect. of state, treasurer
prec.head()

# create unique precinct identifier 
prec["loc_prec"] = prec['COUNTYFP'] + ',' + prec['NAME']
prec['loc_prec'].nunique()
prec.shape
prec[prec.duplicated(['loc_prec'])]
prec = prec.dissolve(by='loc_prec', as_index=False) #dissolve precincts with the same name

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
# ...none for now

# Assigning precincts to U.S. congressional districts
assignment = maup.assign(prec, mscong_merging)
assignment.isna().sum()
prec["CD115FP"] = assignment
# prec.to_file("precincts_testing.shp")

# Assigning precincts to state senate districts
assignment = maup.assign(prec, state)
assignment.isna().sum()
prec["SLDUST"] = assignment

prec.to_file("/Users/hopecj/projects/gerryspam/MO/dat/mo_prec_labeled/mo_prec_labeled_nopop.shp")

# population 
# aggregating block-level census data to precincts
# block_path = "/Users/hopecj/projects/gerryspam/MO/dat/tabblock2010_29_pophu/tabblock2010_29_pophu.shp"
# block = gpd.read_file(block_path)
# block.rename(columns={"BLOCKID10": "id"}, inplace=True)
# assignment = maup.assign(block, prec)
# assignment.isna().sum()
# assignment[assignment.isna()] # fix the NAs manually
# assignment[246433] = ""
# assignment[308849] = ""
# variables = ["POP10"]
# prec[variables] = block[variables].groupby(assignment).sum()

# write it out to a file
#os.mkdir("mo_prec_labeled")
prec.to_file("/Users/hopecj/projects/gerryspam/MO/dat/mo_prec_labeled/mo_prec_labeled.shp")