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
    patternDel = "mail|vbm|prov|emergency|overseas|hand|total|not defined"
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
    else:
        to_replace = replace_with
    out = row.replace(to_replace, regex=True)
    out_list = out.tolist()
    return out_list

"""
county-specific edit functions
"""
# edit precincts with matching issues
def edit_033(row):
    return rm_space(row, 'salem city', 'salem')

def edit_027(row):
    precs = ['salem ', 'chester ', 'mendham ', 'morris ', 'mount ', 'chatham ']
    replace_with = ['salem', 'chester', 'mendham', 'morris', 'mt.', 'chatham']
    return rm_space_multiples(row, precs, replace_with)

def edit_019(row):
    precs = ['clinton ', 'lebanon borough']
    replace_with=['clinton', 'lebanonboro']
    return rm_space_multiples(row, precs, replace_with)

def edit_025(row):
    # need to make sure that 'shrewsbury' is working, not sure why it isn't
    precs = ['freehold ', 'neptune ', 'sea ', 'spring lake ', 'shrewsbury ', 'avon-by-the-sea']
    replace_with = ['freehold', 'neptune', 'sea', 'springlake', 'shrewsbury', 'avon']
    return rm_space_multiples(row, precs, replace_with)

def edit_009(row):
    precs = ['wildwood ', 'west ', 'cape may city', 'cape may point']
    replace_with = ['wildwood', 'west', 'capemay', 'capemaypoint']
    return rm_space_multiples(row, precs, replace_with)

def edit_021(row):
    precs = ['trenton city ward n', 'trenton city ward e', 'trenton city ward s', 'trenton city ward w',
             'hopewell borough', 'hopewell township']
    replace_with = ['trentonnorth', 'trentoneast', 'trentonsouth', 'trentonwest',
                    'hopewellboro', 'hopewelltwp']
    return rm_space_multiples(row, precs, replace_with)

def edit_037(row):
    precs = ['andover township', 'andover borough']
    replace_with = ['andovertwp', 'andoverboro']
    return rm_space_multiples(row, precs, replace_with)

def edit_041(row):
    return rm_space(row, 'washington')

def edit_007(row):
    precs = ['audubon park', 'audubon borough', 
             'berlin borough', 'berlin township', 
             'gloucester township', 'gloucester city',
             'haddon heights', 'haddon township', 
             'pine ']
    replace_with = ['audubonpark', 'audubonboro', 
                    'berlinboro', 'berlintwp', 
                    'gloucestertwp', 'gloucestercity', 
                    'haddonheights', 'haddontwp',
                    'pine']
    return rm_space_multiples(row, precs, replace_with)

def edit_013(row):
    precs = ['irvington township ward north', 'irvington township ward east', 
             'irvington township ward south', 'irvington township ward west',
             'newark city ward north', 'newark city ward east', 
             'newark city ward south', 'newark city ward west', 'newark city ward central']
    replace_with = ['irvingtonnorth ', 'irvingtoneast ', 'irvingtonsouth ', 'irvingtonwest ',
                    'newarknorth ', 'newarkeast ', 'newarksouth ', 'newarkwest ', 'newarkcentral ']
    return rm_space_multiples(row, precs, replace_with)

def edit_039(row):
    precs = ['roselle borough ward', 'roselle park']
    replace_with=['roselleward', 'rosellepark']
    return rm_space_multiples(row, precs, replace_with)

def edit_001(row):
    precs = ['buena borough', 'buena vista',
             'egg harbor township', 'egg harbor city',
             'mullica township ward 1 voting district 1',
             'mullica township ward 2 voting district 1',
             'mullica township ward 3 voting district 1',
             'port republic city ward 2 voting district 1',
             'port republic city ward 1 voting district 1',
             'brigantine city ward 1 voting district 1',
             'brigantine city ward 2 voting district 1',
             'brigantine city ward 3 voting district 1',
             'brigantine city ward 4 voting district 1',
             ]
    replace_with = ['buenaboro', 'buenavista',
                    'eggharbortwp', 'eggharborcity',
                    'mullica township ward 1',
                    'mullica township ward 2',
                    'mullica township ward 3',
                    'port republic city ward 2',
                    'port republic city ward 1',
                     'brigantine city ward 1',
                     'brigantine city ward 2',
                     'brigantine city ward 3',
                     'brigantine city ward 4']
    return rm_space_multiples(row, precs, replace_with)

def edit_003(row):
    precs = ['ridgefield park ', 'ridgefield borough', 
             'river vale', 'river edge', 'saddle brook', 'saddle river']
    replace_with = ['ridgefieldpark ', 'ridgefield', 
                    'rivervale', 'riveredge', 'saddlebrook', 'saddleriver']
    return rm_space_multiples(row, precs, replace_with)

def edit_023(row):
    return rm_space(row, 'south')

def edit_029(row):
    precs = ['ocean gate', 'ocean township']
    replace_with=['oceangate', 'oceantwp']
    return rm_space_multiples(row, precs, replace_with)

# # test function
# d = {'prec': ["pine valley", "pine hill", "audubon borough west", 'haddon township south', 'salem hill east', 'chester thing 2', 'chester'], 'col2': ["dog", 4, "cat", "rabbit", 3, 5, 2]}
# df = pd.DataFrame(data=d)

# print(df['prec'])
# u_out = edit_007(df['prec'])

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
    "029": edit_029
}

"""
direct data cleaning
"""
partnership = gpd.read_file('/Users/hopecj/projects/gerryspam/NJ/dat/partnership-2016/unzipped/extracted/precincts/compiled.shp')

# clean up shapefile precinct column
partnership['precinct'] = partnership.NAMELSAD.str.lower()
partnership['shp_loc_prec'] = partnership['COUNTYFP'].astype(str) + "," + partnership['precinct']

# dissolve precincts with the same precinct name (3)
partnership = partnership.dissolve(by='shp_loc_prec', as_index=False)

clean_shp = partnership.sort_values(by=['COUNTYFP'])

counties = pd.Series(clean_shp['COUNTYFP']).unique()
clean_shp["prec_matching"] = clean_shp["precinct"].copy()
clean_shp.set_index(['COUNTYFP', 'precinct'], inplace=True)
print("duplicated indices", clean_shp[clean_shp.index.duplicated()])

#drop geometry for this step -- can merge geometry back in later
clean_shp = pd.DataFrame(clean_shp.drop(columns='geometry'))

for county in counties:
    print(county)
    county_dat = clean_shp.loc[county]
    changed = countyToCountyCleaner.get(county, lambda x: x)(county_dat['prec_matching'])
    county_dat['prec_matching'] = changed
    clean_shp.update(county_dat)

# continue with the general clean 
clean_shp.reset_index(inplace=True)
partnership_prec_split = clean_shp['prec_matching'].str.split(expand=True)
clean_shp['prec_word1'] = partnership_prec_split[0]

# make column of first word from precinct name and numbers 
shp_nums = ignore_alpha(clean_shp['shp_loc_prec'])
clean_shp["shp_loc_prec_nums"] = shp_nums
clean_shp["shp_loc_prec_code"] = clean_shp['shp_loc_prec_nums'].astype(str) + '_' + clean_shp['prec_word1']

clean_shp.to_csv("/Users/hopecj/projects/gerryspam/NJ/dat/cleanprec_shp.csv")