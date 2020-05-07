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
county-specific edit functions
"""
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

# edit precincts with matching issues
countyToCountyCleaner = {
    "033": edit_033,
}

clean_shp = partnership.sort_values(by=['COUNTYFP'])

counties = pd.Series(clean_shp['COUNTYFP']).unique()
clean_shp["prec_matching"] = clean_shp["precinct"].copy()
clean_shp.set_index(['COUNTYFP', 'precinct'], inplace=True)
print("duplicated indices", clean_shp[clean_shp.index.duplicated()])

for county in counties:
    county_dat = clean_shp.loc[county]
    changed = countyToCountyCleaner.get(county, lambda x: x)(county_dat)
    clean_shp.update(county_dat)

# continue with the general clean 
partnership_prec_split = clean_shp['prec_matching'].str.split(expand=True)
clean_shp['prec_word1'] = clean_shp_prec_split[0]

# make column of first word from precinct name and numbers 
shp_nums = ignore_alpha(clean_shp['shp_loc_prec'])
clean_shp["shp_loc_prec_nums"] = shp_nums
clean_shp["shp_loc_prec_code"] = clean_shp['shp_loc_prec_nums'].astype(str) + '_' + clean_shp['prec_word1']
