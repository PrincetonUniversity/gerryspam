import geopandas as gpd
import pandas as pd

shp_path = "/Users/hopecj/projects/AR/Shapefiles/AR Precincts 10_11_2019/ELECTION_PRECINCTS.shp"
elec_path = "/Users/hopecj/projects/gerryspam/AR/AR_G18.csv"

elec_df = pd.read_csv(elec_path)
shp_df = gpd.read_file(shp_path)
shp_df = shp_df[["state_fips", "county_fip",
                 "county_nam", "precinct", "geometry"]]

"""
general helper functions for all counties
"""


def chop_five(dat):
    dat["prec"] = dat["prec"].str.slice(start=5)


"""
county-specific cleaning counties
"""


def arkansas(dat):
    chop_five(dat)
    dat["prec"] = dat["prec"].replace({
        "DeWitt 1": "Dewitt ward 1",
        "Dewitt 2": "Dewitt ward 2",
        "Dewitt 3": "Dewitt WARD 3",
        "Stuttgart 1": "Stuttgart ward 1",
        "Stuttgart 2": "Stuttgart ward 2",
        "Stuttgart 3": "Stuttgart ward 3",
    })


def baxter(dat):
    dat["prec"] = dat["prec"] + "b"

         })
    dat["prec"] = dat["prec"].str.replace(" - ", "/")

def garland(dat): 
    dat["prec"] = dat["prec"].str.lstrip("0")


def hempstead(dat):
    dat["prec"] = dat["prec"].str.slice(start=3)
    dat["prec"] = dat["prec"].replace(
        {"Cross Roads": "Crossroads",
         })


def marion(dat):
    dat["prec"] = "P00" + dat["prec"].str.slice(start=9)



def pope(dat):
    chop_five(dat)
    dat["prec"] = dat["prec"].str.replace("-", "")

def pulaski(dat):
    dat["prec"] = dat["prec"].str.slice(start=9)
    dat["prec"] = dat["prec"].str.lstrip("0")



"""
overall call function
"""
countyToCountyCleaner = {
    "Arkansas": arkansas,
    "Ashley": ashley,
    "Baxter": baxter,
    "Benton": benton,
    "Boone": boone,
    "Bradley": bradley,
    "Carroll": carroll,
    "Chicot": chicot,
    "Clark": clark,
    "Clay": clay,
    "Cleburne": chop_five,
    "Cleveland": cleveland,
    "Columbia": columbia,
    "Conway": conway,
    "Crawford": crawford,
    "Cross": cross,
    "Dallas": dallas,
    "Desha": desha,
    "Drew": drew,
    "Faulkner": faulkner,
    "Franklin": franklin,
    "Fulton": fulton,
    "Garland": garland,
    "Grant": chop_five,
    "Greene": greene,
    "Hempstead": hempstead,
    "Hot Spring": hotspring,
    "Howard": howard,
    "Independence": independence,
    "Izard": izard,
    "Jackson": jackson,
    "Lafayette": lafayette,
    "Lawrence": lawrence,
    "Lee": lee,
    "Lincoln": lincoln,
    "Little River": littleriver,
    "Logan": logan,
    "Lonoke": lonoke,
    "Marion": marion,
    "Miller": miller,
    "Monroe": monroe,
    "Montgomery": montgomery,
    "Newton": newton,
    "Perry": perry,
    "Phillips": phillips,
    "Pike": chop_five,
    "Polk": polk,
    "Pope": pope,
    "Prairie": prairie,
    "Pulaski": pulaski,
    "Randolph": randolph,
    "Saline": saline,
    "Sebastian": sebastian,
    "Sevier": sevier,
    "Scott": scott,
    "Stone": stone,
    "Union": union,
    "Washington": washington,
    "Woodruff": woodruff,
    "Yell": chop_five,
}

# to test for select counties
# raw_df = shp_df.loc[
#    (shp_df['county_nam'] == "Desha") |
#    (shp_df['county_nam'] == "Benton") |
#    (shp_df['county_nam'] == "Woodruff")]

# must sort alphabetically in order for second-order function to work
clean_df = shp_df.sort_values(by=['county_nam'])

counties = pd.Series(clean_df['county_nam']).unique()
clean_df["prec"] = clean_df["precinct"].copy()
clean_df.set_index(['county_nam', 'precinct'], inplace=True)
print("duplicated indices", clean_df[clean_df.index.duplicated()])


for county in counties:
    county_dat = clean_df.loc[county]
    changed = countyToCountyCleaner.get(county, lambda x: x)(county_dat)
    clean_df.update(county_dat)

clean_df['prec_edit'] = clean_df['prec'].str.lower()
clean_df.reset_index(inplace=True)

clean_df.to_file("/Users/hopecj/projects/AR/Shapefiles/1_edited_precnames/clean.shp")
