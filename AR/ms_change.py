import geopandas as gpd

ms_shp_path = '/Users/hopecj/projects/AR/Shapefiles/mississippi_partnership17/partnership_shapefiles_17v2_05093/PVS_17_v2_vtd_05093.shp'
ms_shp = gpd.read_file(ms_shp_path)
ms_shp["county_nam"] = "Mississippi"

ms_shp = ms_shp.rename(columns={"STATEFP": "state_fips", 
                       "COUNTYFP": "county_fip",
                       "NAMELSAD": "precinct"})

ms_shp = ms_shp[["state_fips", "county_fip", "county_nam", "precinct", "geometry"]]

def mississippi(dat):
    dat["prec_new"] = dat["prec_new"].replace({
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
    
ms_shp["prec_new"] = ms_shp["precinct"].copy()
ms_shp.set_index(['county_nam', 'precinct'], inplace=True)
    
mississippi(ms_shp)
ms_shp.reset_index(inplace=True)

dissolved = ms_shp.dissolve(by='prec_new', as_index=False)
dissolved['PREC'] = dissolved['prec_new'].str.lower()
dissolved = dissolved[["county_nam", "state_fips", "county_fip", "precinct", "PREC", "geometry"]]
print(dissolved)

dissolved.to_file("/Users/hopecj/projects/AR/Shapefiles/3_ms_clean/ms_clean.shp")


#####

# mad_shp_path = '/Users/hopecj/projects/AR/Shapefiles/3_madison_clean/madison_clean.shp'
# mad_shp = gpd.read_file(mad_shp_path)

# mad_shp = mad_shp.rename(columns={"precinct": "PREC"})
# mad_shp["precinct"] = ""

# mad_shp = mad_shp[["county_nam", "state_fips", "county_fip", "precinct", "PREC", "geometry"]]

# mad_shp.to_file('/Users/hopecj/projects/AR/Shapefiles/3_madison_clean/mad_clean.shp')

#####

ouachita_shp_path = '/Users/hopecj/projects/AR/Shapefiles/oachita_partnership17/partnership_shapefiles_17v2_05103/PVS_17_v2_vtd_05103.shp'
ouachita_shp = gpd.read_file(ouachita_shp_path)

ouachita_shp["county_nam"] = "Ouachita"

ouachita_shp = ouachita_shp.rename(columns={"STATEFP": "state_fips", 
                       "COUNTYFP": "county_fip",
                       "NAMELSAD": "precinct"})

ouachita_shp = ouachita_shp[["state_fips", "county_fip", "county_nam", "precinct", "geometry"]]


def ouachita(dat):
    dat["prec_new"] = dat["prec_new"].replace({
        "Red Hill Voting District": "Red Hill",
        "Behestian Voting District": "Behestian",
        "Carroll Voting District": "Carroll",
        "Freeo Voting District": "Freeo",
        "Union Voting District": "Union",
        "Cleveland Voting District": "Cleveland Township",
        "Valley Voting District": "Valley",
        "River Voting District": "River",
        "Bragg Voting District": "Bragg",
        "Liberty Voting District": "Liberty",
        "Ecore Fabre Voting District": "Ecore Fabre",
        "Bradley Voting District": "Bradley",
        "Lafayette A Voting District": "Lafayette A",
        "Lafayette B Voting District": "Lafayette B",
        "Marion Voting District": "Marion",
        "Jefferson Rural Voting District": "Jefferson",
        "Smackover Voting District": "Smackover ward",
        "Bridge Creek Voting District": "Bridge Creek",
        "Washington Voting District": "Washington Ward 1",
        "Camden Ward 13B": "Camden Ward 13",
        "Camden Ward 7A": "Camden Ward 7",
        
    })

ouachita_shp["prec_new"] = ouachita_shp["precinct"].copy()
ouachita_shp.set_index(['county_nam', 'precinct'], inplace=True)
    
ouachita(ouachita_shp)
ouachita_shp.reset_index(inplace=True)

dissolved = ouachita_shp.dissolve(by='prec_new', as_index=False)
dissolved['PREC'] = dissolved['prec_new'].str.lower()
dissolved = dissolved[["county_nam", "state_fips", "county_fip", "precinct", "PREC", "geometry"]]
print(dissolved)

dissolved.to_file("/Users/hopecj/projects/AR/Shapefiles/3_ouachita_clean/ouachita_clean.shp")


# oachita_shp = oachita_shp.rename(columns={"precinct": "PREC"})
# oachita_shp["precinct"] = ""

# oachita_shp = oachita_shp[["county_nam", "state_fips", "county_fip", "precinct", "PREC", "geometry"]]

# oachita_shp.to_file('/Users/hopecj/projects/AR/Shapefiles/3_oachita_clean/oachita_clean.shp')
