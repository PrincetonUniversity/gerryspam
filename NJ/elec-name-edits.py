import pandas as pd
import fuzzy_pandas as fpd
import geopandas as gpd 
import re
from rich import print
# import helper_functions

"""
helper functions
"""
# strip letters from column 
def ignore_alpha(row):
    regex = re.compile('[\D_]+')
    return [regex.sub('', value) for value in row]

# ignore special election rows 
# mail-in, provisional, emergency, hand(?), overseas, removed resident, congressional district tallies
def ignore_special(df):
    patternDel = "mail|vbm|prov|emergency|oversea|hand|total|not defined|removed|congressional"
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
def rm_space_multiples(row, prec_to_replace, replace_with=None):
    if replace_with is None:
        to_replace = {(prec + ' '):prec for prec in prec_to_replace}
        out = row.replace(to_replace, regex=True)
    else:
        out = row.replace(prec_to_replace, replace_with, regex=True)
    out_list = out.tolist()
    return out_list

"""
county-specific edit functions
"""
# edit precincts with matching issues
def edit_033(row):
    return rm_space(row, 'salem')

def edit_027(row):
    precs = ['chatham ', 'chester ', 'mendham ', 'morris ', 'parsippany - troy', 'mt. ']
    replace_with = ['chatham', 'chester', 'mendham', 'morris', 'parsippany-troy', 'mt.']
    return rm_space_multiples(row, precs, replace_with)

def edit_019(row):
    precs = ['clinton', 'lebanon']
    return rm_space_multiples(row, precs)

def edit_025(row):
    precs = ['freehold ', 'neptune ', 'sea ', 'spring lake ', 'shrewsbury ']
    replace_with = ['freehold', 'neptune', 'sea', 'springlake', 'shrewsbury']
    return rm_space_multiples(row, precs, replace_with)

def edit_009(row):
    precs = ['wildwood crest', 'wildwood', 'west ', 'cape may point', 'cape may']
    replace_with = ['wildwoodcrest', 'wildwoodcity', 'west', 'capemaypoint', 'capemay']
    return rm_space_multiples(row, precs, replace_with)
    
def edit_021(row):
    precs = ['trenton', 'hopewell']
    return rm_space_multiples(row, precs)

def edit_037(row):
    return rm_space(row, 'andover')

def edit_041(row):
    return rm_space(row, 'washington')

def edit_007(row):
    precs = ['audubon', 'berlin', 'gloucester', 'haddon', 'pine']
    return rm_space_multiples(row, precs)
    
def edit_013(row):
    precs = ['irvington n-', 'irvington e-', 'irvington s-', 'irvington w-',
             'newark n-', 'newark e-', 'newark s-', 'newark w-', 'newark c-']
    replace_with = ['irvingtonnorth ', 'irvingtoneast ', 'irvingtonsouth ', 'irvingtonwest ',
                    'newarknorth ', 'newarkeast ', 'newarksouth ', 'newarkwest ', 'newarkcentral ']
    return rm_space_multiples(row, precs, replace_with)

def edit_039(row):
    precs = ['roselle park', 'roselle ward', ]
    replace_with=['rosellepark', 'roselleward',]
    return rm_space_multiples(row, precs, replace_with)

def edit_001(row):
    precs = ['buena ', 'egg harbor ', 'west ']
    replace_with = ['buena', 'eggharbor', 'west']
    return rm_space_multiples(row, precs, replace_with)

def edit_003(row):
    precs = ['ridgefield park ', 'river vale', 'river edge', 'saddle brook', 'saddle river',
             'wood ridge']
    replace_with = ['ridgefieldpark ', 'rivervale', 'riveredge', 'saddlebrook', 'saddleriver',
                    'wood-ridge']
    return rm_space_multiples(row, precs, replace_with)

def edit_023(row):
    precs = [',', 'south ']
    replace_with = ['', 'south']
    return rm_space_multiples(row, precs, replace_with)

def edit_035(row):
    precs = ['peapack-gladstone', 'greenbrook']
    replace_with=['peapack and gladstone', 'green brook']
    return rm_space_multiples(row, precs, replace_with)

def edit_029(row):
    precs = ['ocean gate', 'ocean district']
    replace_with=['oceangate', 'oceantwp']
    return rm_space_multiples(row, precs, replace_with)

countyToCountyCleaner = {
    "033": edit_033,
    "027": edit_027,
    "019": edit_019,
    "025": edit_025,
    "009": edit_009,
    "021": edit_021,
    "037": edit_037,
    "041": edit_041,
    "007": edit_007,
    "013": edit_013,
    "039": edit_039,
    "001": edit_001,
    "003": edit_003,
    "023": edit_023,
    "035": edit_035,
    "029": edit_029
}
    
"""
direct data cleaning
"""
# OpenElections
elec_16 = pd.read_csv('/Users/hopecj/projects/gerryspam/NJ/dat/NJ_G16_OpenElex.csv')

# if using open elections data
# split apart county and precinct (only 1 comma split)
elec_16 = pd.concat([elec_16, elec_16['loc_prec'].str.split(',', 1, expand=True)], axis=1)
elec_16 = elec_16.rename(columns={0: "countynam", 1: "precinct"})
elec_16['precinct'] = elec_16['precinct'].str.lower()
crosswalk = pd.read_csv('/Users/hopecj/projects/gerryspam/NJ/dat/nj-county-crosswalk.csv')
elec_16 = elec_16.merge(crosswalk, left_on='countynam', right_on='county_nam')
elec_16['county_fips_st'] = elec_16['statefips_countyfips'].apply(str)
elec_16['county_fips'] = elec_16['county_fips_st'].str.slice(start=2)

# remove special election precinct rows 
print(elec_16.shape)
elec_16 = ignore_special(elec_16)
print(elec_16.shape) # got rid of 1363 rows

clean_elec = elec_16.sort_values(by=['county_fips'])
counties = pd.Series(clean_elec['county_fips']).unique()
clean_elec["prec_matching"] = clean_elec["precinct"].copy()
clean_elec.set_index(['county_fips', 'precinct'], inplace=True)
# print("duplicated indices", clean_elec[clean_elec.index.duplicated()])

# CHECK: are all of the counties in election results?
print(counties)
print("# counties in elections:", len(counties))
print("# counties in NJ:", len(crosswalk.statefips_countyfips.unique()))

# # FOR TESTING
# county_dat = clean_elec.loc['033']
# changed = countyToCountyCleaner.get(county, lambda x: x)(county_dat['prec_matching'])
# print("changed", changed)
# county_dat['prec_matching'] = changed
# print(county_dat['prec_matching'])

for county in counties:
    county_dat = clean_elec.loc[county]
    changed = countyToCountyCleaner.get(county, lambda x: x)(county_dat['prec_matching'])
    county_dat['prec_matching'] = changed
    clean_elec.update(county_dat)

# continue with the general clean
clean_elec.reset_index(inplace=True)
clean_elec['elec_loc_prec'] = clean_elec['county_fips'].astype(str) + "," + clean_elec['prec_matching'].astype(str)
prec_split = clean_elec['prec_matching'].str.split(expand=True)
clean_elec['prec_word1'] = prec_split[0]
# clean_elec = clean_elec.drop([2, 3, 'Unnamed: 6'], axis=1)

# clean_elec.to_csv("/Users/hopecj/projects/gerryspam/NJ/dat/cleanprec_elec_intermediate.csv")
# clean_elec = pd.read_csv("/Users/hopecj/projects/gerryspam/NJ/dat/cleanprec_elec_intermediate.csv")

# # make column of first word from precinct name and numbers 
# # strip the leading zero off the precinct number, if there is one
elec_nums = ignore_alpha(clean_elec['elec_loc_prec'])
fips_nums = [number[:3] for number in elec_nums]
prec_nums = [number[3:] for number in elec_nums] 
prec_nums_noleadingzero = [number.lstrip('0') for number in prec_nums] 
clean_elec['clean_fips'] = fips_nums
clean_elec['clean_prec_code'] = prec_nums_noleadingzero
clean_elec["elec_loc_prec_nums"] = clean_elec['clean_fips'].astype(str) + clean_elec['clean_prec_code'].astype(str)
clean_elec["elec_loc_prec_code"] = clean_elec['elec_loc_prec_nums'].astype(str) + '_' + clean_elec['prec_word1']

clean_elec.to_csv("/Users/hopecj/projects/gerryspam/NJ/dat/cleanprec_elec.csv")