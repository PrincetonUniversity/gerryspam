'''
Expected input: Shapefile of Missori census blocks with total population in each block
Expected output: Shapefile of Missouri census blocks with black population in each
'''

from census_area import Census
import secrets

# API_KEY = 

c = Census(API_KEY)

infile = '/Users/hopecj/projects/gerryspam/MO/dat/tabblock2010_29_pophu/tabblock2010_29_pophu.shp'
block_shape = gpd.read_file(infile)
features = []

# Variables here
# https://api.census.gov/data/2010/dec/sf1/variables.html 
black_pop = c.sf1.geo_block(('NAME', 'P003003'), block_shape['geometry'], 2010)

for block_geojson, block_data in black_pop:
     block_geojson['properties'].update(block_data)
     features.append(block)
     
my_shape_with_new_data_geojson = {'type': "FeatureCollection", 'features': features}
print(my_shape_with_new_data_geojson)