import geopandas as gpd
import pandas as pd
import maup
import os
from rich import print

# precinct data 
prec_path = "/Users/hopecj/projects/gerryspam/MO/dat/mo_2016/mo_2016.shp"
prec = gpd.read_file(prec_path)
prec.crs
list(prec.columns) # president, u.s. senate, governor, lt. gov, atg, sect. of state, treasurer
prec.head()

# create unique precinct identifier 
prec["loc_prec"] = prec['COUNTYFP'] + ',' + prec['NAME']
prec['loc_prec'].nunique()
prec[prec.duplicated(['loc_prec'])]
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

# state HOR data 
st_house_path = "/Users/hopecj/projects/gerryspam/MO/dat/tl_2016_29_sldl/tl_2016_29_sldl.shp"
st_house = gpd.read_file(st_house_path)
st_house.crs
list(st_house.columns) # SLDUST is st_house senate district
st_house.rename(columns={"SLDLST": "id"}, inplace=True)
st_house = st_house[["id", "geometry"]]

# Assigning precincts to U.S. congressional districts
assignment = maup.assign(prec, mscong_merging)
assignment.isna().sum()
prec["CD115FP"] = assignment

# Assigning precincts to state senate districts
assignment = maup.assign(prec, state)
assignment.isna().sum()
prec["SLDUST"] = assignment

# Assigning precincts to state house districts
assignment = maup.assign(prec, st_house)
assignment.isna().sum()
prec["SLDLST"] = assignment

# census block-group shapefile
block_group = gpd.read_file("/Users/hopecj/projects/gerryspam/MO/dat/tl_2013_29_bg/tl_2013_29_bg.shp")

# CVAP (block-group level)
# converted original file to utf-8 using
# iconv -c -f ascii -t utf-8 BlockGr.csv > BlockGr_8.csv
cvap = pd.read_csv("/Users/hopecj/projects/gerryspam/MO/dat/CVAP_2013-2017_ACS_csv_files/BlockGr_8.csv", encoding='utf-8')
cvap['GEOID'] = cvap["geoid"].str.slice(start=7)
cvap.set_index(['lntitle'], inplace=True) # only keep "total" CVAP, not ones broken down by race
cvap_small = cvap.loc['Total']

blockgr = block_group.merge(cvap_small, on="GEOID")
blockgr.to_file("/Users/hopecj/projects/gerryspam/MO/dat/blockgr_cvap/blockgr_cvap.shp")


#prec.to_file("/Users/hopecj/projects/gerryspam/MO/dat/mo_prec_labeled/mo_prec_labeled_nopop.shp")

## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## 
## once areal_interpolation script is run to give census blocks with precinct labels
## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## 


# population 
block_path = "/Users/hopecj/projects/gerryspam/MO/dat/blocks_with_prec/mo_blocks_with_prec.shp"
block = gpd.read_file(block_path)
agg_prec = block.dissolve(by='loc_prec', aggfunc='sum')



# merge labelled precinct file and prec (from blocks) file
prec = gpd.read_file("/Users/hopecj/projects/gerryspam/MO/dat/mo_prec_labeled/mo_prec_labeled_nopop.shp")
prec_merging = prec[['loc_prec', 'COUNTYFP', 'NAME', 'CD115FP', 'SLDUST', 'SLDLST',
                    'G16PREDCLI', 'G16PRERTRU', 
                     'G16PRELJOH', 'G16PREGSTE', 'G16PRECCAS', 'G16USSDKAN', 'G16USSRBLU', 'G16USSLDIN', 
                     'G16USSGMCF', 'G16USSCRYM', 'G16GOVDKOS', 'G16GOVRGRE', 'G16GOVLSPR', 'G16GOVGFIT', 
                     'G16GOVITUR', 'G16LTGDCAR', 'G16LTGRPAR', 'G16LTGLHED', 'G16LTGGLEA', 'G16ATGDHEN', 
                     'G16ATGRHAW', 'G16TREDBAK', 'G16TRERSCH', 'G16TRELOTO', 'G16TREGHEX', 'G16SOSDSMI', 
                     'G16SOSRASH', 'G16SOSLMOR']]
out_file = agg_prec.merge(prec_merging, on='loc_prec')

# write it out to a file
out_file.to_file("/Users/hopecj/projects/gerryspam/MO/dat/final_prec/prec_labeled.shp")

file = gpd.read_file("/Users/hopecj/projects/gerryspam/MO/dat/final_prec/prec_labeled.shp")

################## post sampling !!!!!!!!!!!!!!!!!!!
dat_chain1 = pd.read_csv("/Users/hopecj/projects/gerryspam/MO/dat/pop-constrained_small.csv")
dat_chain2 = pd.read_csv("/Users/hopecj/projects/gerryspam/MO/dat/single-flip-contiguous_small.csv")

out = pd.concat([dat_chain1, dat_chain2])
out.to_csv("/Users/hopecj/projects/gerryspam/MO/dat/sampled-plans.csv")