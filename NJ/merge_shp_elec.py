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
results_exact.head(5)

out = results_exact[['year', 'STATEFP', 'COUNTYFP', 'NAMELSAD', 
            'G16DPRS', 'G16RPRS', 'G16DHOR', 'G16RHOR', 
            'precinct', 'precinct', 'shp_loc_prec_code', 'elec_loc_prec_code',
            'shp_loc_prec', 'elec_loc_prec', 'countynam']]

out.to_csv("/Users/hopecj/projects/gerryspam/NJ/dat/NJ16_merging.csv")