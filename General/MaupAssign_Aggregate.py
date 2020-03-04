import pandas as pd
import geopandas as gpd
import maup

#load in precinct and district shapefiles
census_blocks = gpd.read_file('/Users/hopecj/projects/AR/Shapefiles/oachita/GeoStor/Society.BLOCKS_TIGER_2010_polygon.shp')
precincts = gpd.read_file('/Users/hopecj/projects/AR/Shapefiles/oachita/ouachita_parnership 17/partnership_shapefiles_17v2_05103/PVS_17_v2_vtd_05103.shp')

#make sure they are in the same CRS
precincts = precincts.to_crs(census_blocks.crs)

#make district assignment for every precinct
assignment = maup.assign(census_blocks, precincts)
census_blocks['assignment'] = assignment

# save file
precincts.to_file('/Users/hopecj/projects/AR/Shapefiles/oachita/censusblocks_assigned.shp')

####
## # if you want to aggregate 
####

#list variables you want to aggreage into precincts
variables = ['tot','hispanic']

#sum votes by district
precincts[variables] = census_blocks[variables].groupby(assignment).sum()

#check that totals match
prec_total = census_blocks['tot'].sum()
print('old tot',prec_total)
agg_total = precincts['tot'].sum()
print('new tot',agg_total)

#save file
precincts.to_file('filename.shp')

csv = precincts.drop(['geometry'],axis = 1)
csv.to_csv('filename.csv')
