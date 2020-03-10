import geopandas as gpd
import pandas as pd
import numpy as np
import re
import shapely

shp_path = '/Users/hopecj/projects/AR/Shapefiles/1_edited_precnames/clean.shp'
shp = gpd.read_file(shp_path)

def carroll(dat):
    dat["PREC"] = dat["PREC"].replace({
        "bv ward 1": "bv wards 1 and 2",
        "bv ward 2": "bv wards 1 and 2",
        "es ward 1": "es wards 1, 2, 3",
        "es ward 2": "es wards 1, 2, 3",
        "es ward 3": "es wards 1, 2, 3",
        "gf ward 1": "gf wards 1 and 2",
        "gf ward 2": "gf wards 1 and 2",
        "ne hickory": "ne/nw hickory/coin/lng crk",
        "nw hickory": "ne/nw hickory/coin/lng crk",
        "coin": "ne/nw hickory/coin/lng crk",
        "lng crk": "ne/nw hickory/coin/lng crk",
        "cabanal": "prairies/cabanal",
        "ne prairie": "prairies/cabanal",
        "nw & sw prairie": "prairies/cabanal",
    })


def crittenden(dat):
    dat["PREC"] = dat["PREC"].replace({
        "11 - ward 1 precinct 1": "1ST BAPTIST CHURCH WMPH",
        "12 - ward 1 precinct 2": "1ST BAPTIST CHURCH WMPH",
        "41 - ward 4 precinct 1": "7TH STREET CHURCH WMPH",
        "42 - ward 4 precinct 2": "7TH STREET CHURCH WMPH",
        "79 - bob ward 2": "ANTHONYVILLE CITY HALL",
        "70 - lucas": "BONDS MARINE",
        "32 - ward 3 precinct 2": "CALVARY WMPH",
        "21 - ward 2 precinct 1": "CIVIC CENTER",
        "22 - ward 2 precinct 2": "CIVIC CENTER",
        "63 - jackson 1": "CRAWFORDSVILLE",
        "59 - earle ward 1": "EARLE CITY HALL",
        "60 - earle ward 2": "EARLE CITY HALL",
        "61 - earle ward 3": "EARLE CITY HALL",
        "73 - north tyronza": "EARLE CITY HALL",
        "56 - bob ward 1": "EDMONDSON",
        "57 - north fogleman": "GILMORE",
        "54 - east black oak": "HEAFER",
        "55 - west black oak": "HEAFER",
        "77- lucas estate (h'shoe lake)": "HORSESHOE FIRE STATION",
        "81 - south tyronza, jeanette": "JENNETTE CITY HALL",
        "82 - wappanocca, clarkdale": "JERICHO CITY HALL",
        "80 - wappanocca, jericho": "JERICHO CITY HALL",
        "76 - wappanocca": "JERICHO CITY HALL",
        "65 - jasper country box (court": "MARION CHURCH OF GOD",
        "67 - jasper 1": "MARION CHURCH OF GOD",
        "69 - jasper 3": "MARION COUNTY OFFICE",
        "66 - mound city": "MARION COUNTY OFFICE",
        "75 - jasper county box, sunset": "MARION COUNTY OFFICE",
        "68 - jasper 2": "MARION IMMANUEL HWY 77",
        "78 - jasper country box (lakes": "MARION IMMANUEL HWY 77",
        "23 - ward 2 precinct 3": "MT OLIVE WMPH",
        "64 - jackson 2": "MT PISGAH CHURCH",
        "51 - ward 5 precinct 1": "PILGRIMS REST CHURCH",
        "62 - earle ward 4": "ST LUKE CHURCH",
        "13 - ward 1 precicnt 3": "WM HIGH SCHOOL",
        "14 - ward 1 precicnt 4": "WM HIGH SCHOOL",
        "31 - ward 3 precinct 1": "WM HIGH SCHOOL",
        "33 - ward 3 precinct 3": "WM HIGH SCHOOL",
        "72 - proctor": "WM HIGH SCHOOL",
        "52 - ward 5 precinct 2": "WONDER BOYS CLUB",
        "58 - south fogleman": "WR GOLDEN",
    })


def faulkner(dat):
    dat["PREC"] = dat["PREC"].replace({
        "2d conway city 40": "07 2a"
    })


def independence(dat):
    dat["PREC"] = dat["PREC"].replace({
        "big bottom ward 1": "Big Bottom Wards 1,2,3",
        "big bottom ward 2": "Big Bottom Wards 1,2,3",
        "big bottom ward 3": "Big Bottom Wards 1,2,3",
    })


def monroe(dat):
    dat["PREC"] = dat["PREC"].replace({
        "brinkley township": "BRINKLEY/ DIXON",
        "dixon township": "BRINKLEY/ DIXON",
        "fargo": "RICHLAND/GREENFIELD/FARGO",
        "richland township": "RICHLAND/GREENFIELD/FARGO",
        "greenfield township": "RICHLAND/GREENFIELD/FARGO",
        "jackson township": "JACKSN/CLBRNE/MONT./SMALL",
        "cleburne": "JACKSN/CLBRNE/MONT./SMALL",
        "montgomery/smalley townsh": "JACKSN/CLBRNE/MONT./SMALL",
        "hindman township": "HINDMAN/ RAYMOND/PINE RID",
        "raymond township": "HINDMAN/ RAYMOND/PINE RID",
        "pine ridge township": "HINDMAN/ RAYMOND/PINE RID",
        "roc-roe township": "roc",
        "roc-roe township/city": "roc",
    })


def nevada(dat):
    dat["PREC"] = dat["PREC"].replace({
        "bluff city": "Bluff City City/Rural",
        "bluff city rural": "Bluff City City/Rural",
        "bodcaw city": "Bodcaw",
        "bodcaw rural": "Bodcaw",
        "ward 1": "Wards 1,2,3,4",
        "ward 2": "Wards 1,2,3,4",
        "ward 3": "Wards 1,2,3,4",
        "ward 4": "Wards 1,2,3,4",
        "willisville city": "Willisville City/Rural",
        "willisville rural": "Willisville City/Rural",
    })


def poinsett(dat):
    dat["PREC"] = dat["PREC"].replace({
        "bolivar north": "bolivar",
        "bolivar south": "bolivar",
        "bolivar ward 1": "bolivar",
        "bolivar ward 2": "bolivar",
        "bolivar ward 3": "bolivar",
        "bolivar ward 4": "bolivar",
        "dobson - cooper haynes": "dobson",
        "dobson - pitts": "dobson",
        "greenwood - rivervale": "Greenwood and Rivervale",
        "greenwood township": "Greenwood and Rivervale",
        "greenwood ward 1": "Greenwood and Rivervale",
        "greenwood ward 2": "Greenwood and Rivervale",
        "greenwood ward 3": "Greenwood and Rivervale",
        "greenwood ward 4": "Greenwood and Rivervale",
        "little river - payneway": "Little River and Payneway",
        "little river township": "Little River and Payneway",
        "little river ward 1": "Little River and Payneway",
        "little river ward 2": "Little River and Payneway",
        "little river ward 3": "Little River and Payneway",
        "little river ward 4": "Little River and Payneway",
        "lunsford - mccormick": "lunsford",
        "lunsford - tulot": "lunsford",
        "lunsford - weona": "lunsford",
        "owen - fisher city": "owen - fisher",
        "owen - fisher rural": "owen - fisher",
        "owen - waldenburg city": "owen - waldenburg",
        "owen - waldenburg rural": "owen - waldenburg",
        "scott - valley view": "scott vv and wh",
        "scott - whitehall": "scott vv and wh",
        "tyronza city": "tyronza",
        "tyronza rural": "tyronza",
        "west prairie city": "west prairie",
        "west prairie rural": "west prairie",
        "willis ward 1": "willis",
        "willis ward 2": "willis",
        "willis ward 3": "willis",
        "willis ward 4": "willis",
        "willis ward 5": "willis",
    })


def st_francis(dat):
    dat["PREC"] = dat["PREC"].replace({
        "24 - bonair": "bonair",
        "16 - tuni": "bonair",
        "17 - bonair": "bonair",
        "26 - bonair": "bonair",
        "23 - caldwell country": "caldwell",
        "22 - caldwell city": "caldwell",
        "20 - colt city": "colt",
        "27 - pine Tree": "colt",
        "21 - colt country": "colt",
        "57 - forrest city ward 1-6": "fc ward 1",
        "35 - forrest city ward 1-1": "fc ward 1",
        "38 - forrest city ward 1-4": "fc ward 1",
        "43 - forrest city ward 2-3": "fc ward 2",
        "45 - forrest city ward 2-4": "fc ward 2",
        "41 - forrest city ward 2-2": "fc ward 2",
        "55 - forrest city ward 2-6": "fc ward 2",
        "50 - forrest city ward 2-2": "fc ward 2",
        "40 - forrest city ward 2-1": "fc ward 2",
        "53 - forrest city ward 3-5": "fc ward 3",
        "52 - forrest city ward 3-4": "fc ward 3",
        "49 - forrest city ward 3-1": "fc ward 3",
        "65 - forrest city ward 4-5": "fc ward 4",
        "66 - forrest city ward 4-6": "fc ward 4",
        "56 - forrest city ward 4-2": "fc ward 4",
        "26 - forrest city country west": "forrest city country west",
        "06 - heth": "heth/blackfish",
        "13 - round pond mosley gw": "heth/blackfish",
        "11 - round pond mosley ge": "heth/blackfish",
        "07 - blackfish": "heth/blackfish",
        "02 - hughes ward 2": "hughes",
        "01 - hughes ward 1": "hughes",
        "03 - hughes ward 3": "hughes",
        "05 - rawlison": "hughes",
        "04 - hughes country": "hughes",
        "14 - madison city": "madison",
        "15 - madison country": "madison",
        "19 - newcastle": "newcastle/parrott",
        "18 - parrott": "newcastle/parrott",
        "25 - parrot/newcastle": "newcastle/parrott",
        "29 - palestine city 2": "palestine",
        "30 - palestine city 3": "palestine",
        "32 - goodwin": "palestine",
        "31 - palestine country": "palestine",
        "28 - palestine city 1": "palestine",
        "34 - wheatley country": "wheatley",
        "33 - wheatley city": "wheatley",
        "10 - widener city ge": "widener",
        "09 - widener county gw": "widener",
    })


def stone(dat):
    dat["PREC"] = dat["PREC"].replace({
        "fifty six": "northwest"
    })


def washington(dat):
    dat["PREC"] = dat["PREC"].replace({
        "fay 09a": "fay 9",
        "fay 09b": "fay 9",
        "farmington-3": "farmington 2",
        "prairie gr city-1": "prairie gr city",
        "prairie gr city-2": "prairie gr city",
    })


countyToDissolve = {
    "Carroll": carroll,
    "Crittenden": crittenden,
    "Faulkner": faulkner,
    "Independence": independence,
    "Monroe": monroe,
    "Nevada": nevada,
    "Poinsett": poinsett,
    "St. Francis": st_francis,
    "Stone": stone,
    "Washington": washington,
}

clean_df = shp.sort_values(by=['county_nam'])

counties = pd.Series(clean_df['county_nam']).unique()
clean_df["PREC"] = clean_df["prec_edit"].copy()
clean_df = clean_df[["state_fips", "county_fip",
                 "county_nam", 
                 "precinct", "PREC",
                 "geometry"]]

clean_df.set_index(['county_nam', 'precinct'], inplace=True)

for county in counties:
    county_dat = clean_df.loc[county]
    changed = countyToDissolve.get(county, lambda x: x)(county_dat)
    clean_df.update(county_dat)

clean_df.reset_index(inplace=True)
print("clean_df, reset index", clean_df)

clean_df["loc_prec"] = clean_df["county_nam"] + "," + clean_df["PREC"]
dissolved = clean_df.dissolve(by='loc_prec', as_index=False)
print(list(dissolved.columns))

#check for topology errors
# print("topology errors", dissolved.is_valid)

dissolved = dissolved[["state_fips", "county_fip", "county_nam", "precinct", "PREC", "geometry"]]

#
##
###
# remove counties coming from alternative data sources
dissolved.set_index(['county_nam'], inplace=True)

out = dissolved.drop(["Madison"], axis=0)
out_2 = out.drop(["Mississippi"], axis=0)
out_2.reset_index(inplace=True)

out_2.to_file("/Users/hopecj/projects/AR/Shapefiles/2_dissolved_removed/dissolved_removed.shp")
