import sys
sys.path.append('/Users/hwheelen/Documents/GitHub/gerrymander-geoprocessing/areal_interpolation')
import areal_interpolation as ai
import geopandas as gpd
import matplotlib

small = gpd.read_file('/Volumes/GoogleDrive/Shared drives/princeton_gerrymandering_project/States and local partners/New York/Nassau County/demographics/Nassau_blocks_pop10.shp')
large = gpd.read_file('/Volumes/GoogleDrive/Shared drives/princeton_gerrymandering_project/States and local partners/New York/Nassau County/Matching Shapes and Elecs/second try/Nassau18Gen.shp')

large = large.to_crs(small.crs)

cols = ['tot', 'NHwhite', 'NHblack', 'hispanic', 'totVAP','WVAP', 'BVAP', 'HVAP']

small[cols] = small[cols].astype(float)

#nm = gpd.read_file('/Users/hwheelen/Desktop/VA/VA_Leg_Enacted_BH.shp’)

aggregated = ai.aggregate(small,large, source_columns=cols)[1] 

#check that totals match
small_total = small['tot'].sum()
print('old tot',small_total)
agg_total = aggregated['tot'].sum()
print('new tot',agg_total)

aggregated.to_file('/Volumes/GoogleDrive/Shared drives/princeton_gerrymandering_project/States and local partners/New York/Nassau County/Precincts Elecs and Demographics/Nassau18GenDem.shp')
