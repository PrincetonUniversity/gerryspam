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

# concat first two words for sneaky precincts
# (e.g.: "salem north", "salem east" within the same county)
def rm_space(row, prec_in, prec_out=None):
    with_space_in = prec_in + ' '
    regex = re.compile(with_space_in)
    if prec_out is None:
        replace = prec_in 
    else:
        replace = prec_out
    return [regex.sub(replace, value) for value in row]

# same as the above but deals with multiple precincts within one county
def rm_space_multiples(row, *mult_precincts):
    to_replace = {(prec + ' '):prec for prec in mult_precincts}
    out = row.replace(to_replace, regex=True)
    out_list = out.tolist()
    return out_list

"""
county-specific edit functions
"""
# edit precincts with matching issues
countyToCountyCleaner = {
    "033": edit_033,
    "027": edit_027,
    "019": edit_019,
}

def edit_033(row):
    return rm_space(row, 'salem city', 'salem')

def edit_027(row):
    precs = ['salem', 'chester', 'mendham', 'morris']
    return rm_space_multiples(row, precs)

# need to come back and change this one
# so that it's possible to put "in" and "out" options on the multiple 
def edit_019(row):
    to_replace = ['clinton ', 'lebanon borough']
    replace_with=['clinton', 'lebanonboro']
    out = df['prec'].replace(to_replace, replace_with, regex=True)
    return out 

d = {'prec': ["clinton hill", "p", "lebanon borough west", 'lebanon boro south', 'salem hill east', 'chester thing 2', 'chester'], 'col2': ["dog", 4, "cat", "rabbit", 3, 5, 2]}
df = pd.DataFrame(data=d)

print(df['prec'])
u_out = edit_019(df['prec'])

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
