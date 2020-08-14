import pandas as pd
import fuzzy_pandas as fpd
import geopandas as gpd 
import re

clean_shp = pd.read_csv("/Users/hopecj/projects/gerryspam/NJ/dat/cleanprec_shp.csv")
clean_elec = pd.read_csv("/Users/hopecj/projects/gerryspam/NJ/dat/cleanprec_elec.csv")

# merge by digits and first precinct word
results_exact = fpd.fuzzy_merge(clean_shp, clean_elec, left_on='shp_loc_prec_code', right_on='elec_loc_prec_code', 
                          ignore_case=True, 
                          keep='all',
                          join='full-outer',
                          method='exact')

print("Found", results_exact.shape)
results_exact.head(5)

out = results_exact[['year', 'STATEFP', 'COUNTYFP', 'NAMELSAD', 
            'G16DPRS', 'G16RPRS', 'G16DHOR', 'G16RHOR', 
            'precinct', 'precinct', 'shp_loc_prec_code', 'elec_loc_prec_code',
            'shp_loc_prec', 'elec_loc_prec', 'countynam']]

out.to_csv("/Users/hopecj/projects/gerryspam/NJ/dat/NJ16_merging.csv")


#############
############# FILE-LOCATIONS
#############

## precinct-level shapefile
## 2019 partnership file
#partnership = gpd.read_file('/Users/hopecj/projects/NJ/2016/Shapefiles/Combined Partnership Files/NJ2019Precincts.shp')
# ## 2016 partnership file
# partnership = gpd.read_file('/Users/hopecj/projects/gerryspam/NJ/dat/partnership-2016/unzipped/extracted/precincts/compiled.shp')

# # precinct-level election results
# # MEDSL
# # elec_18 = pd.read_csv('/Users/hopecj/projects/gerryspam/NJ/dat/NJ_G18_MIT.csv')
elec_16 = pd.read_csv('/Users/hopecj/projects/gerryspam/NJ/dat/NJ_G16_MIT.csv')
# # OpenElections
# elec_16 = pd.read_csv('/Users/hopecj/projects/gerryspam/NJ/dat/NJ_G16_OpenElex.csv')

#############
############# CLEANING
#############

## if using MEDSL data
# elec_16 = pd.concat([elec_16, elec_16['precinct'].str.split(',', expand=True)], axis=1)
# elec_16 = elec_16.astype({"county_fips": int})
# elec_16 = elec_16.rename(columns={"precinct": "countynam_prec", 1: "precinct", "county_fips": "statefp_countyfp"})
# elec_16['county_fips'] = elec_16['statefp_countyfp'].astype(str).str[2:]
# elec_16['precinct'] = elec_16['precinct'].str.lower()
# elec_16['elec_loc_prec'] = elec_16['county_fips'].astype(str) + "," + elec_16['precinct'].astype(str)

#############
############# MERGING
#############

# # LEVENSHTEIN - STRING DISTANCE METRIC
# out = partnership.merge(elec_16, left_on='shp_loc_prec', right_on='elec_loc_prec', how='outer')

# results = fpd.fuzzy_merge(partnership, elec_16, left_on='shp_loc_prec', right_on='elec_loc_prec', 
#                           ignore_case=True, keep='match', method='levenshtein', threshold=0.85)

# print("Found", results.shape)
# results.head(5)
# len(results)
# len(elec_16)
# frac_mached = len(results)/len(elec_16)
# print("fraction matched =", frac_mached*100)

# # bilenko - prompts for matches 
# results_bilenko = fpd.fuzzy_merge(partnership, elec_16, left_on='shp_loc_prec', right_on='elec_loc_prec', 
#                           ignore_case=True, keep='match', method='bilenko')

# print("Found", results_bilenko.shape)
# results_bilenko.head(5)
# len(elec_16)
# frac_mached = len(results_bilenko)/len(elec_16)
# print("fraction matched =", frac_mached*100)

# results.to_csv('bilenko_res.csv')

# # metaphone - phoenetic matching algoritm  
# results_metaphone = fpd.fuzzy_merge(partnership, elec_16, left_on='shp_loc_prec', right_on='elec_loc_prec', 
#                           ignore_case=True, keep='match', method='metaphone')

# print("Found", results_metaphone.shape)
# results_metaphone.head(5)
# len(elec_16)
# frac_mached = len(results_metaphone)/len(elec_16)
# print("fraction matched =", frac_mached*100)

# results.to_csv('metaphone_res.csv')

# # STR distance - numbers only
# results_exact = fpd.fuzzy_merge(partnership, elec_16, left_on='shp_loc_prec_nums', right_on='elec_loc_prec_nums', 
#                           ignore_case=True, keep_left='shp_loc_prec', keep_right='elec_loc_prec',
#                           method='exact')

# print("Found", results_exact.shape)
# frac_mached = len(results_exact)/len(elec_16)
# print("fraction matched =", frac_mached*100)

