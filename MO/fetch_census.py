'''
Expected input: Shapefile of Missouri census blocks with total population in each block, CSV of Missouri census blocks with population by race
Expected output: Shapefile of Missouri census blocks with black population in each
'''

import pandas as pd
import geopandas as gpd

# read in shapefile of Missouri census blocks with total population in each block
infile = '/Users/hopecj/projects/gerryspam/MO/dat/tabblock2010_29_pophu/tabblock2010_29_pophu.shp'
block_shape = gpd.read_file(infile)

# read in CSV of Missouri census blocks with population by race
infile_two = '/Users/hopecj/projects/gerryspam/MO/dat/DECENNIALPL2010.P3_2020-06-29T123442/DECENNIALPL2010.P3_data_with_overlays_2020-06-29T123319.csv'
race_pop = pd.read_csv(infile_two, header=1)
race_pop['BLOCKID10'] = race_pop['id'].str[9:]
race_pop = race_pop[['BLOCKID10', 'Total', 'Total!!Population of one race',
       'Total!!Population of one race!!White alone',
       'Total!!Population of one race!!Black or African American alone']]
race_pop.rename(columns={'Total': "total", 
                       'Total!!Population of one race': "total_pop_1_race",
                       'Total!!Population of one race!!White alone': "total_pop_white", 
                       'Total!!Population of one race!!Black or African American alone': "total_pop_black"},
                inplace=True)

# merge the files
outfile = block_shape.merge(race_pop, on='BLOCKID10')
 # add stuff here to compare differences between pop in both data sts
 # add percentage here
 