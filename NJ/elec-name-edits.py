import pandas as pd
import fuzzy_pandas as fpd
import geopandas as gpd 
import re
from rich import print

"""
helper functions
"""
# strip letters from column 
def ignore_alpha(row):
    regex = re.compile('[\D_]+')
    return [regex.sub('', value) for value in row]

# ignore special election rows (mail-in, provisional, emergency, and overseas)
def ignore_special(df):
    patternDel = "mai|provision|emergency|overseas"
    filter = df[~df["precinct"].str.contains(patternDel, na=False)]
    return filter

# concat precinct words for sneaky precincts
# (e.g.: "salem north", "salem east" within the same county)
def edit_033(row):
    regex = re.compile('salem ')
    return [regex.sub('salem', value) for value in row]

"""
direct data cleaning
"""
# OpenElections
elec_16 = pd.read_csv('/Users/hopecj/projects/gerryspam/NJ/dat/NJ_G16_OpenElex.csv')

# if using open elections data
elec_16 = pd.concat([elec_16, elec_16['loc_prec'].str.split(',', expand=True)], axis=1)
elec_16 = elec_16.rename(columns={0: "countynam", 1: "precinct"})
elec_16['precinct'] = elec_16['precinct'].str.lower()
crosswalk = pd.read_csv('/Users/hopecj/projects/gerryspam/NJ/dat/nj-county-crosswalk.csv')
elec_16 = elec_16.merge(crosswalk, left_on='countynam', right_on='county_nam')
elec_16['county_fips_st'] = elec_16['statefips_countyfips'].apply(str)
elec_16['county_fips'] = elec_16['county_fips_st'].str.slice(start=2)

# remove special election precinct rows 
print(elec_16.shape)
elec_16 = ignore_special(elec_16)
print(elec_16.shape) # got rid of 1238 rows

# concat precinct words for sneaky precincts
# (e.g.: "salem north", "salem east" within the same county)




elec_16['elec_loc_prec'] = elec_16['county_fips'].astype(str) + "," + elec_16['precinct'].astype(str)
prec_split = elec_16['precinct'].str.split(expand=True)
elec_16['prec_word1'] = prec_split[0]
elec_16 = elec_16.drop([2, 3, 'Unnamed: 6'], axis=1)
# make column of first word from precinct name and numbers 
elec_nums = ignore_alpha(elec_16['elec_loc_prec'])
elec_16["elec_loc_prec_nums"] = elec_nums
elec_16["elec_loc_prec_code"] = elec_16['elec_loc_prec_nums'].astype(str) + '_' + elec_16['prec_word1']
