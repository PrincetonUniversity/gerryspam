import areal_interpolation as ai
import geopandas as gpd
import maup
import matplotlib

small = gpd.read_file('/Users/hopecj/projects/gerryspam/MO/dat/tabblock2010_29_pophu/tabblock2010_29_pophu.shp')
large = gpd.read_file('/Users/hopecj/projects/gerryspam/MO/dat/tl_2013_29_bg/tl_2013_29_bg.shp')
# large = gpd.read_file('/Users/hopecj/projects/gerryspam/MO/dat/mo_prec_labeled/mo_prec_labeled_nopop.shp')

small = small.to_crs(large.crs)

# target_columns should be name of disaggregation column from `large`
# start time: 12:31 pm
# end time: 1:30 pm
agg = ai.aggregate(small, large, target_columns=['GEOID'])[0] # this takes a while!

agg = agg[['STATEFP10', 'COUNTYFP10', 'TRACTCE10', 'BLOCKCE',
       'BLOCKID10', 'PARTFLG', 'HOUSING10',
       'POP10', 'GEOID', 'geometry']]

agg.to_file('/Users/hopecj/projects/gerryspam/MO/dat/blocks_with_bg/blocks_with_bg.shp')