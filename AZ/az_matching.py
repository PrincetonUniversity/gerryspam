import geopandas as gpd
import pathlib

#
# 2016 - verify VEST results 
#
merged_2016_path = pathlib.Path.home() / "projects" / "AZ" / "az_2016" / "az_2016.shp"
merged_2016 = gpd.read_file(merged_2016_path)
merged_2016.head()

merged_2016.groupby(['CDE_COUNTY']).sum()
# matches up with wikipedia results, yay!

# 
# 2018 matching 
#
