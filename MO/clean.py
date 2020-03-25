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

#prec.to_file("/Users/hopecj/projects/gerryspam/MO/dat/mo_prec_labeled/mo_prec_labeled_nopop.shp")

# population 
block_path = "/Users/hopecj/projects/gerryspam/MO/dat/blocks with precincts/MOBlocksPrecLabels.shp"
block = gpd.read_file(block_path)
agg_prec = block.dissolve(by='loc_prec', aggfunc='sum')

# merge labelled precinct file and prec (from blocks) file
prec_merging = prec[['loc_prec', 'COUNTYFP', 'NAME', 'CD115FP', 'SLDUST', 'G16PREDCLI', 'G16PRERTRU', 
                     'G16PRELJOH', 'G16PREGSTE', 'G16PRECCAS', 'G16USSDKAN', 'G16USSRBLU', 'G16USSLDIN', 
                     'G16USSGMCF', 'G16USSCRYM', 'G16GOVDKOS', 'G16GOVRGRE', 'G16GOVLSPR', 'G16GOVGFIT', 
                     'G16GOVITUR', 'G16LTGDCAR', 'G16LTGRPAR', 'G16LTGLHED', 'G16LTGGLEA', 'G16ATGDHEN', 
                     'G16ATGRHAW', 'G16TREDBAK', 'G16TRERSCH', 'G16TRELOTO', 'G16TREGHEX', 'G16SOSDSMI', 
                     'G16SOSRASH', 'G16SOSLMOR']]
out_file = agg_prec.merge(prec_merging, on='loc_prec')

# write it out to a file
out_file.to_file("/Users/hopecj/projects/gerryspam/MO/dat/final_prec/prec_labeled.shp")


