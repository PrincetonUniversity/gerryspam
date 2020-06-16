import pandas as pd
import geopandas as gpd
import maup

# give partnership unique precinct identifier
# dissolve repeated precincts
partnership = gpd.read_file('/Users/hopecj/projects/gerryspam/NJ/dat/partnership-2016/unzipped/extracted/precincts/compiled.shp')
partnership["loc_prec"] = partnership['COUNTYFP'] + ',' + partnership['NAMELSAD']
partnership['loc_prec'].nunique()
partnership[partnership.duplicated(['loc_prec'])]
partnership.shape
partnership = partnership.dissolve(by='loc_prec', as_index=False) #dissolve precincts with the same name

# voter roll
vr = gpd.read_file('/Users/hopecj/projects/gerryspam/NJ/dat/Geocoded VR/NJ_CivisVRblocks.shp')

# give voter roll precinct labels 
vr.crs
partnership.crs
#partnership.to_crs(vr.crs, inplace=True)
