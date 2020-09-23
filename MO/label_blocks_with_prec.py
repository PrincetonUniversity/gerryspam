import sys
sys.path.append('~/gerryspam/General') # will probably need to change the relative path; set it to gerryspam/General
import areal_interpolation as ai
import geopandas as gpd
import maup
import matplotlib

small = gpd.read_file('/Users/hopecj/projects/gerryspam/MO/dat/blocks_with_racepop/blocks_with_racepop.shp')
large = gpd.read_file('/Users/hopecj/projects/gerryspam/MO/dat/mo_prec_labeled/mo_prec_labeled_nopop.shp')

small = small.to_crs(large.crs)

agg = ai.aggregate(small, large, target_columns=['loc_prec'])[0] # this takes a while

agg.to_file('/Users/hopecj/projects/gerryspam/MO/dat/blocks_with_prec/blocks_with_prec.shp')
