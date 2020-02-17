import geopandas as gpd 
import pandas as pd 
import pdb

shp_path = "/Users/hopecj/projects/AR/Shapefiles/AR Precincts 10_11_2019/ELECTION_PRECINCTS.shp"
elec_path = "/Users/hopecj/projects/gerryspam/AR/AR_G18.csv"

elec_df = pd.read_csv(elec_path)
shp_df = gpd.read_file(shp_path)
shp_df = shp_df[["county_nam", "precinct", "geometry"]]

"""
general helper functions for all counties 
"""

"""
county-specific cleaning counties
"""
def jefferson(dat):
    dat["prec"] = dat["prec"].str.lstrip("0")
    dat["prec"] = dat["prec"].str.rstrip("X")
    
def marion(dat):
    dat["prec"] = "P00" + dat["prec"].str.slice(start=9)
    print(dat['prec'])
    
def pulaski(dat):
    dat["prec"] = dat["prec"].str.slice(start=9)
    dat["prec"] = dat["prec"].str.lstrip("0")
    print(dat['prec'])

"""
overall call function
"""
countyToCountyCleaner = {
#    "Hempstead": hempstead,
    "Jefferson": jefferson,
    "Marion": marion,
    "Pulaski": pulaski,
#    "Craighead": craighead
}

test_df = shp_df.loc[
  # (shp_df['county_nam'] == "Jefferson") | 
    (shp_df['county_nam'] == "Marion") | 
   (shp_df['county_nam'] == "Pulaski")]
            
counties = pd.Series(test_df['county_nam']).unique()
test_df["prec"] = test_df["precinct"].copy()
test_df.set_index(['county_nam', 'precinct'], inplace=True)

for county in counties: 
    county_dat = test_df.loc[county]
    changed = countyToCountyCleaner.get(county, lambda x: x)(county_dat) # why lambda x?
#    pdb.set_trace()
    test_df.update(changed, errors='raise')
    
test_df.to_file("/Users/hopecj/projects/AR/Shapefiles/test.shp")