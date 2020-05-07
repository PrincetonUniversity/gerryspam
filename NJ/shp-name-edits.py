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

# concat precinct words for sneaky precincts
# (e.g.: "salem north", "salem east" within the same county)
def edit_033(row):
    regex = re.compile('salem ')
    return [regex.sub('salem', value) for value in row]

"""
direct data cleaning
"""
partnership = gpd.read_file('/Users/hopecj/projects/gerryspam/NJ/dat/partnership-2016/unzipped/extracted/precincts/compiled.shp')

# clean up shapefile precinct column
list(partnership.columns)
partnership['precinct'] = partnership.NAMELSAD.str.lower()
partnership['shp_loc_prec'] = partnership['COUNTYFP'].astype(str) + "," + partnership['precinct']
partnership_prec_split = partnership['precinct'].str.split(expand=True)
partnership['prec_word1'] = partnership_prec_split[0]

# make column of first word from precinct name and numbers 
shp_nums = ignore_alpha(partnership['shp_loc_prec'])
partnership["shp_loc_prec_nums"] = shp_nums
partnership["shp_loc_prec_code"] = partnership['shp_loc_prec_nums'].astype(str) + '_' + partnership['prec_word1']
