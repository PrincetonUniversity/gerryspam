import geopandas as gpd
import pandas as pd
import numpy as np
import re
import shapely

shp_path = '/Users/hopecj/projects/AR/Shapefiles/clean_precnames/clean.shp'
shp = gpd.read_file(shp_path)
shp.set_index('county_nam', inplace=True)

# 
##
###

to_remove = ["Madison", "Oachita"]

def rm_county(dat, countyName):
    data_out = dat.drop(countyName, axis=0)
    return data_out 

for county in to_remove:
    rm_county(shp, county)

data_out.to_file("/Users/hopecj/projects/AR/Shapefiles/removed_counties.shp")

###
##
#

def carroll(dat):
    dat["PREC"] = dat["prec_final"].replace({
        "bv ward 1": "bv wards 1 and 2",
        "bv ward 2": "bv wards 1 and 2",
        "es ward 1": "es wards 1, 2, 3",
        "es ward 2": "es wards 1, 2, 3",
        "es ward 3": "es wards 1, 2, 3",
        "gf ward 1": "gf wards 1 and 2",
        "gf ward 2": "gf wards 1 and 2",
        "ne hickory":  "ne/nw hickory/coin/lng crk",
        "nw hickory": "ne/nw hickory/coin/lng crk",
        "coin": "ne/nw hickory/coin/lng crk",
        "lng crk": "ne/nw hickory/coin/lng crk",
        "cabanal": "prairies/cabanal",
        "ne prairie": "prairies/cabanal",
        "nw & sw prairie": "prairies/cabanal",
})
    
def crittenden(dat):
    dat["PREC"] = dat["prec_final"].replace({
        "11 - ward 1 precinct 1": "1ST BAPTIST CHURCH WMPH",
        "12 - ward 1 precinct 2": "1ST BAPTIST CHURCH WMPH",
        "41 - ward 4 precinct 1": "7TH STREET CHURCH WMPH",
        "42 - ward 4 precinct 2": "7TH STREET CHURCH WMPH",
        "79 - bob ward 2": "ANTHONYVILLE CITY HALL",
        "70 - lucas": "BONDS MARINE",
        "32 - ward 3 precinct 2": "CALVARY WMPH",
        "21 - ward 2 precinct 1": "CIVIC CENTER",
        "22 - ward 2 precinct 2": "CIVIC CENTER",
        "63 - jackson 1":  "CRAWFORDSVILLE",
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
        "68 - jasper 2": "MARION IMMANUEL HWY 77",                 # need to figure this one out: == Immanuel Baptist church?
        "78 - jasper country box (lakes": "MARION IMMANUEL HWY 77", # need to figure this one out: == Immanuel Baptist church?
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
    dat["PREC"] = dat["prec_final"].replace({
        "2d conway city 40": "07 2a"
})
    
def independence(dat):
    dat["PREC"] = dat["prec_final"].replace({
        "big bottom ward 1": "Big Bottom Wards 1,2,3",
        "big bottom ward 2": "Big Bottom Wards 1,2,3",
        "big bottom ward 3": "Big Bottom Wards 1,2,3",
}) 

def monroe(dat):
    dat["PREC"] = dat["prec_final"].replace({
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
    dat["PREC"] = dat["prec_final"].replace({
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
    dat["PREC"] = dat["prec_final"].replace({
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
    dat["PREC"] = dat["prec_final"].replace({
        "24 - Bonair": "Bonair",
        "16 - Tuni": "Bonair",
        "17 - Bonair": "Bonair",
        "26 - Bonair": "Bonair",
        "23 - Caldwell Country": "Caldwell",
        "22 - Caldwell City": "Caldwell",
        "20 - Colt City": "Colt",
        "27 - Pine Tree": "Colt",
        "21 - Colt Country": "Colt",
        "57 - Forrest City Ward 1-6": "FC Ward 1",
        "35 - Forrest City Ward 1-1": "FC Ward 1",
        "38 - Forrest City Ward 1-4": "FC Ward 1",
        "43 - Forrest City Ward 2-3": "FC Ward 2",
        "45 - Forrest City Ward 2-4": "FC Ward 2",
        "41 - Forrest City Ward 2-2": "FC Ward 2",
        "55 - Forrest City Ward 2-6": "FC Ward 2",
        "50 - Forrest City Ward 2-2": "FC Ward 2",
        "40 - Forrest City Ward 2-1": "FC Ward 2",
        "53 - Forrest City Ward 3-5": "FC Ward 3",
        "52 - Forrest City Ward 3-4": "FC Ward 3",
        "49 - Forrest City Ward 3-1": "FC Ward 3",
        "65 - Forrest City Ward 4-5": "FC Ward 4",
        "66 - Forrest City Ward 4-6": "FC Ward 4",
        "56 - Forrest City Ward 4-2": "FC Ward 4",
        "26 - Forrest City Country West": "Forrest City Country West",
        "06 - Heth": "Heth/Blackfish",
        "13 - Round Pond Mosley GW": "Heth/Blackfish",
        "11 - Round Pond Mosley GE": "Heth/Blackfish",
        "07 - Blackfish": "Heth/Blackfish",
        "02 - Hughes Ward 2": "Hughes",
        "01 - Hughes Ward 1": "Hughes",
        "03 - Hughes Ward 3": "Hughes",
        "05 - Rawlison": "Hughes",
        "04 - Hughes Country": "Hughes",
        "14 - Madison City": "Madison",
        "15 - Madison Country": "Madison",
        "19 - Newcastle": "Newcastle/Parrott",
        "18 - Parrott": "Newcastle/Parrott",
        "25 - Parrot/Newcastle": "Newcastle/Parrott",
        "29 - Palestine City 2": "Palestine",
        "30 - Palestine City 3": "Palestine",
        "32 - Goodwin": "Palestine",
        "31 - Palestine Country": "Palestine",
        "28 - Palestine City 1": "Palestine",
        "34 - Wheatley Country": "Wheatley",
        "33 - Wheatley City": "Wheatley",
        "10 - Widener City GE": "Widener",
        "09 - Widener County GW": "Widener",
})
    
def stone(dat):
    dat["PREC"] = dat["prec_final"].replace({
        "fifty six": "northwest"
})
    
def washington(dat):
    dat["PREC"] = dat["prec_final"].replace({
        "Fay 09a": "Fay 9",
        "Fay 09b": "Fay 9",
        "Farmington-3": "Farmington 2",
        "Prairie Gr City-1": "Prairie Gr City",
        "Prairie Gr City-2": "Prairie Gr City",
})

countyToDissolve = {
    "Carroll": carroll,
    "Crittenden": crittenden, # need to double-check this when erin emails me back
    "Independence": independence,
    "Monroe": monroe,
    "Nevada": nevada,
    "Poinsett": poinsett,
    "St. Francis": st_francis,
    "Stone": stone
    }

shp = shp.sort_values(by=['county_nam']) # you have to sort the counties alphabetically whowwwwww

counties = pd.Series(shp['county_nam']).unique()
shp["prec"] = shp["precinct"].copy()
shp.set_index(['county_nam', 'precinct'], inplace=True)

for county in counties: 
    county_dat = shp.loc[county]
    changed = countyToDissolve.get(county, lambda x: x)(county_dat) 
    shp.update(county_dat)

dissolved = shp.dissolve(by='prec_to-agg')
dissolved.reset_index(inplace=True)
#dissolved = dissolved.buffer(0)

# check for topology errors
dissolved.is_valid

dissolved.to_file("/Users/hopecj/projects/AR/Shapefiles/dissolved.shp")


###
###
###
# Mississippi County treatment
####
###


ms_shp_path = '/Users/hopecj/projects/AR/Shapefiles/mississippi_partnership17/partnership_shapefiles_17v2_05093/PVS_17_v2_vtd_05093.shp'
ms_shp = gpd.read_file(ms_shp_path)


def mississippi(dat):
    dat["PREC"] = dat["prec_final"].replace({
        "Bassett Precinct 54A": "Bassett CH",
        "Big Lake TWP Precinct 24": "Gosnell Comm Center",
        "Big Lake TWP Precinct 25": "Gosnell Comm Center",
        "Birdsong Precinct 46A": "Bassett CH",
        "Blytheville Precinct 1A": "Trinity Baptist Church",
        "Blytheville Precinct 1B": "Trinity Baptist Church",
        "Blytheville Precinct 1C": "Trinity Baptist Church",
        "Blytheville Precinct 1D": "Trinity Baptist Church",
        "Blytheville Precinct 1E": "Trinity Baptist Church",
        "Blytheville Precinct 2A": "Frim Foundation Ministrie",
        "Blytheville Precinct 2C": "Osceola Main Street",
        "Blytheville Precinct 2E": "Osceola Main Street",
        "Blytheville Precinct 3A": "Frim Foundation Ministrie",
        "Blytheville Precinct 3B": "Frim Foundation Ministrie",
        "Blytheville Precinct 3D": "Frim Foundation Ministrie",
        "Blytheville Precinct 3F": "Trinity Baptist Church",
        "Blythville Precinct 3C": "Frim Foundation Ministrie",
        "Bowen TWP Precinct 12": "Dell Community Center",
        "Burdette Precinct 27A": "Gosnell School",
        "Burdette TWP Precinct 27": "Gosnell School",
        "Canadian TWP Precinct 10": "Miss County Election Cent",
        "Carson TWP Precinct 38": "Etowah FS",
        "Carson TWP Precinct 39": "Etowah FS",
        "Chickasawba TWP Precinct 6": "Osceola Main Street",
        "Chickasawba TWP Precinct 7": "Osceola Main Street",  
        "Clear Lake TWP Precinct 11A": "Osceola Main Street", 
        "Clear Lake TWP Precinct 11B": "Osceola Main Street", 
        "Dell Precinct 14": "ANC Burdette",
        "Dyess Precinct 47": "Dyess City Hall",
        "Dyess TWP Precinct 48": "Dyess City Hall",
        "Etowach City Precinct 50A": "Birdsong FS",
        "Fletcher TWP Precinct 30": "Manila Depot",
        "Golden Lake TWP Precinct 40": "Etowah FS",
        "Gosnell Precinct 12-1": "AAMOD Bldg",
        "Gosnell Precinct 12-2": "Armorel Planting Co",
        "Gosnell Precinct 12-3": "Dell Community Center",
        "Half Moon TWP Precinct 13": "ANC Burdette",
        "Hector TWP Precinct 15": "ANC Burdette",
        "Joiner Precinct 44": "Joiner CH",
        "Keiser Precinct 37-1": "Wilson Library",
        "Keiser Precinct 37-2": "Wilson Library",
        "Leachville Precinct 16": "Leachville City Hall",
        "Leachville Precinct 17": "Leachville City Hall",
        "Leachville Precinct 18": "Leachville City Hall",
        "Little River Precinct 50": "Birdsong FS",
        "Luxora Precinct 29-1": "Manila Depot",
        "Luxora Precinct 29-2": "Manila Depot",
        "Luxora Precinct 29-3": "Manila Depot",
        "Manila Precinct 21A": "Gosnell Comm Center",
        "Manila Precinct 21B": "Gosnell Comm Center",
        "Manila Precinct 22": "Gosnell Comm Center",
        "Manila Precinct 23": "Gosnell Comm Center",
        "Marie Precinct 39A": "Etowah FS",
        "McGavock TWP Precinct 45": "Joiner CH",
        "Monroe TWP Precinct 35": "Keiser FBC",
        "Monroe TWP Precinct 36": "Wilson Library",
        "Neal TWP Precinct 19": "Leachville City Hall",
        "Osceola Precinct 32A": "Keiser FBC",
        "Osceola Precinct 32B": "Keiser FBC",
        "Osceola Precinct 33A": "Keiser FBC",
        "Osceola Precinct 33B": "Keiser FBC",
        "Osceola Precinct 33C": "Keiser FBC",
        "Osceola Precinct 33D": "Keiser FBC",
        "Osceola Precinct 34A": "Keiser FBC",
        "Osceola Precinct 34B": "Keiser FBC",
        "Osceola Precinct 34C": "Keiser FBC",
        "Precinct 54": "Bassett CH",
        "Victoria Precinct 30A": "Charles Strong CC",
        "Whitton TWP Precinct 46": "Bassett CH",
        "Wilson Precinct 41": "Etowah FS",
        "Wilson Precinct 42": "Etowah FS",
    })
