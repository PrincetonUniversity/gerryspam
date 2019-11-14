import geopandas as gpd
import pandas as pd
import pathlib

#
# 2016 - verify VEST results 
#
merged_2016_path = pathlib.Path.home() / "projects" / "AZ" / "az_2016" / "az_2016.shp"
merged_2016 = gpd.read_file(merged_2016_path)
merged_2016.head()

merged_2016.groupby(['CDE_COUNTY']).sum()
# matches up with wikipedia results, yay!

# 2018 matching 
# 
# election results from open elections
url = 'https://raw.githubusercontent.com/openelections/openelections-data-az/master/2018/20181106__az__general__precinct.csv'
elec = pd.read_csv(url)
apache = elec.loc[elec['county'] == 'Apache']
len(apache.precinct.unique())

merged_2018_path = pathlib.Path.home() / "projects" / "AZ" / "az_2018" / "az_2018.shp"
merged_2018 = gpd.read_file(merged_2018_path)
merged_2018.head()
merged_2018.groupby(['CDE_COUNTY']).sum()
