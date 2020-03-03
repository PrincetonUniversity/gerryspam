import geopandas as gpd 
import pandas as pd 

shp_path = "/Users/hopecj/projects/AR/Shapefiles/AR Precincts 10_11_2019/ELECTION_PRECINCTS.shp"
elec_path = "/Users/hopecj/projects/gerryspam/AR/AR_G18.csv"

elec_df = pd.read_csv(elec_path)
shp_df = gpd.read_file(shp_path)
shp_df = shp_df[["state_fips", "county_fip", "county_nam", "precinct", "geometry"]]

"""
general helper functions for all counties 
"""
def chop_five(dat):
    dat["prec"] = dat["prec"].str.slice(start=5)

"""
county-specific cleaning counties
"""
def arkansas(dat):
    dat["prec"] = dat["prec"].str.slice(start=5)
    dat["prec"] = dat["prec"].replace({
        "DeWitt 1": "Dewitt ward 1",
        "Dewitt 2": "Dewitt ward 2",
        "Dewitt 3": "Dewitt WARD 3",
        "Stuttgart 1": "Stuttgart ward 1",
        "Stuttgart 2": "Stuttgart ward 2",
        "Stuttgart 3": "Stuttgart ward 3",
    })
    
def ashley(dat):
    dat["prec"] = dat["prec"].str.slice(start=5)
    dat["prec"] = dat["prec"].replace({
        "Crossett Ward 1": "CW 1",
        "Crossett Ward 2": "CW 2",
        "Crossett Ward 3": "CW 3",
        "Fountain Hill City": "FH CITY",
        "Fountain Hill Rural": "FH RURAL",
        "Hamburg Ward 1": "HW1",
        "Hamburg Ward 2": "HW2",
        "Hamburg Ward 3": "HW3",
        "Mt. Zion": "MT ZION",
        "North Crossett East": "NCE",
        "North Crossett West": "NCW",
        "Snyder / Trafalgar": "SNY/TRA",
        "VO - Tech": "VOTECH",
        "West Crossett Rural": "WCR",
    })

def benton(dat):
    dat["prec"] = dat["prec"].replace(
        {
        "Precinct 01": "Precinct 1",
        "Precinct 02": "Precinct 2",
        "Precinct 03": "Precinct 3",
        "Precinct 04": "Precinct 4",
        "Precinct 05": "Precinct 5",
        "Precinct 06": "Precinct 6",
        "Precinct 07": "Precinct 7",
        "Precinct 08": "Precinct 8",
        "Precinct 09": "Precinct 9",
    })
    
def bradley(dat):
    dat["prec"] = dat["prec"].str.slice(start=5)
    dat["prec"] = dat["prec"].replace(
        {"Warren Ward 1": "Ward 1", 
            "Warren Ward 2": "Ward 2", 
            "Warren Ward 3": "Ward 3"})
    
def carroll(dat):
    dat["prec"] = dat["prec"].replace(
        {
        "Berryville Ward 1": "BV Ward 1",
        "Berryville Ward 2": "BV Ward 2",
        "Eureka Springs Ward 1": "ES Ward 1",
        "Eureka Springs Ward 2": "ES Ward 2",
        "Eureka Springs Ward 3": "ES Ward 3",
        "Green Forest Ward 1": "GF Ward 1",
        "Green Forest Ward 2": "GF Ward 2",
        "North East Hickory": "NE Hickory",
        "Northwest Hickory": "NW Hickory",
        "Long Creek": "Lng Crk",
        "SW & SE HICKORY": "SW/SE HICKORY",
    })

def chicot(dat):
    dat["prec"] = dat["prec"].str.slice(start=5)
    dat["prec"] = dat["prec"].replace(
        {"Carlton": "Carlton 1"})

def clark(dat):
    dat["prec"] = dat["prec"].replace(
        {
        "Central 1": "Central",
        "Curtis 1": "Curtis",
        "East County 1": "East County",
        "Gum Springs Outside 1": "Gum Springs Outside",
        "Gum Springs 1": "Gum Springs Inside",
        "Gurdon Gen 1": "Gurdon General",
        "North East County": "Northeast County",
        "Okolona City 1": "Okolona City",
        "South County 1": "South County",
        "West County 1": "West County",
        "Whelen Springs 1": "Whelen Springs",
    })
    
def clay(dat):
    dat["prec"] = dat["prec"].str.slice(start=5) # need to figure out what's going on here -- possibly remove this
    dat["prec"] = dat["prec"].replace(
        {
        "Bennett & Lemmons": "Bennett and Lemmons",
        "E Oak Bluff & Blue Cane": "East Oak Bluff & Blue Cane",
        "Liddell & chalk Bluff": "Liddell & Chalk Bluff",
        "Cleveland & N Kilgore": "N Kilgore & Cleveland",
        "North St Francis": "North St. Francis",
        "Gleghorn & S Kilgore": "S Kilgore & Gleghorn",
        "South St Francis": "South St. Francis",
    })

def columbia(dat):
     dat["prec"] = dat["prec"].replace(
         {"Taylor City": "Taylor", "Waldo City": "Waldo"})   

def conway(dat):
    dat["prec"] = dat["prec"].replace(
        {"St Vincent": "St. Vincent", "Lick Mountain": "Lick Mtn."})    

def crawford(dat):
    dat["prec"] = dat["prec"].replace(
        {
        "Alma 01": "Alma 1",
        "Alma 02": "Alma 2",
        "Alma 03": "Alma 3",
        "Alma 04": "Alma 4",
        "Cove City": "Cove City CSD",
        "Lee Creek": "Lee Creek CSD",
        "Mulberry 01": "Mulberry 1",
        "Mulberry 02": "Mulberry 2",
        "Mulberry 03": "Mulberry 3"})    

def cross(dat):
    dat["prec"] = dat["prec"].replace(
        {
        "Bay Village / Birdeye": "Bay Village, Birdeye",
        "Cherry Valley": "Cherry Valley City",
        "Tyronza / Twist": "Tyronza, Twist",
        "Wynne Ward 1": "WYNNE WARD 1",
        "Wynne Ward 2": "WYNNE WARD 2",
        "Wynne Ward 3": "WYNNE WARD 3",
        "Wynne Ward 4": "WYNNE WARD 4",
        "Wynne Ward 5": "WYNNE WARD 5"})     
    
def desha(dat):
    chop_five(dat)
    dat["prec"] = dat["prec"].replace(
    {
        "Bowie W1": "Bowie 1",
        "Bowie W2": "Bowie 2",
        "Bowie W3": "Bowie 3",
        "Mitcheville": "Mitchellville",
        "Rand W1": "Randolph 1",
        "Rand W2": "Randolph 2",
        "Rand W3": "Randolph 3",
        "Rand W4": "Randolph 4",
        "Rand Rural": "Randolph Rural",
        "Silver Lake": "Silverlake",
    })
    
def drew(dat):
    chop_five(dat)
    dat["prec"] = dat["prec"].replace(
    {
        "Mar N Box 1": "MN BOX 1 - RH Cumb. Presb",  
        "Mar N Box 2": "MN Box 2 - RH Baptist Chu",  
        "Marion South": "Marion South - Shady Grov",
    })

def faulkner(dat):
    dat["prec"] = dat["prec"].replace(
    {
        "Wilson 35": "35 Wilson",
        "West Cadron 14": "14 W Cadron",
        "Walker 38": "38 Walker",
        "Vilonia City 21": "21 Vilonia",
        "Union 37": " 37 Union",
        "Pine Mt 36": "36 Pine Mt.",
        "Palarm 39": " 39 Palarm",
        "Newton 34": "34 Newton",
        "Mountain 32": "32 Mountain",
        "Mount Vernon 33": "33 Mt. Vernon",
        "Matthews 31": "31 Matthews",
        "Harve 30": "30 Harve",
        "Hardin Rural 28": "28 Hardin",
        "Hardin City West (GB) 55": "55.01 Hardin GB West",
        "Hardin City East (GB) 29": "29.01 Hardin GB East",
        "Enola 27": "27 Enola",
        "East Fork 26": "26 East Fork",
        "Eagle 25": "25 Eagle",
        "E Cadron C 48": "48 E Cadron C",
        "E Cadron B 13": "13 E Cadron B",
        "E Cadron A 12": "12  E Cadron A",
        "Danley Rural 23": "23 Danley",
        "Danley City (Mayflower) 24": "24 Mayflower",
        "Cypress Rural 22": "22 Cypress",
        "Clifton 19": "19 Clifton",
        "California 18": "18 CA",
        "Bristol 17": "17 Bristol",
        "Benton 16": "16 Benton",
        "Benedict 15": "15 Benedict",
        "4f Conway City 05": "05 4F",
        "4e Conway City 03": "03.01 4E",
        "4d Conway City 04": "04.01 4D",
        "4c Conway City 11": "11 4C",
        "4b Conway City 02": "02 4B",
        "4a Conway City 01": "01.01 4A",
        "3g Conway City 54": "54 3G",
        "3f Conway City 53": "53 3F",
        "3e Conway City 45": "45.01 3E",
        "3d Conway City 50": "50.01 3D",
        "3c-West Conway City 46": "46 3C-W",
        "3c-East Conway City 09": "09 3C-E",
        "3b Conway City 08": "08 3B",
        "3a Conway City 10": "10 3A",
        "2c Conway City 49": "49 2C",
        "2b Conway City 06": "06.01 2B",
        "2a Conway City 07": "07 2A",
        "1e-West Conway City 44": "44 1E-W",
        "1e-East Conway City 43": "43 1E-E",
        "1c-South Conway City 42": "42 1C-S",
        "1c-North Conway City 41": "41 1C-N",
    })

def franklin(dat):
    dat["prec"] = dat["prec"].replace(
    {
        "7-C (Etna)": "7-C Etna",
        "6-B (Altus City)": "6-B Altus City",
        "7-A (Cecil)": "7-A Cecil",
        "3-E (Watalula)": "3-E Watalula",
        "2-D (Wallace/Ivy)": "2-D Wallace/Ivy",
        "1-B (Oz Wd 3)": "1-B Ozark Wd. 3",
        "2-A (Oz Wd 2)": "2-A Ozark Wd. 2",
        "3-F (Mountain)": "3-F Mountain",
        "5-A (Wallace/Ivy)": "5-A Wallace/Ivy",
        "9-A (Charleston Wd 2)": "9-A Charleston Wd. 2",
        "3-A (Lonelm/Cravens)": "3-A Lone Elm/Cravens",
        "8-A (Branch City)": "8-A Branch City",
        "4-B (Watalula)": "4-B Watalula",
        "3-D (Jethro)": "3-D Jethro",
        "3-B (Fern)": "3-B Fern",
        "7-D (Donald Rural)": "7-D Donald",
        "3-C (Boston)": "3-C Boston",
        "8-B (Charleston Wd 1)": "8-B Charleston Wd. 1",
        "8-D (Vesta)": "8-D Vesta",
        "6-D (Weiderkehr Village)": "6-D W.V. City",
        "8-F (Cecil)": "8-F Cecil",
        "5-C (Webb City)": "5-C Webb City",
        "2-C (Lonelm/Cravens)": "2-C Lone Elm/Cravens",
        "4-C (WV Rural)": "4-C W-V Rural",
        "6-A (Altus Rural)": "6-A Altus Rural",
        "6-C (Denning)": "6-C Denning City",
        "4-D (Oz Rural)": "4-D Ozark Rural",
        "4-A (Philpot)": "4-A Philpot",
        "8-E (Donald Rural)": "8-E Donald",
        "9-C (Charleston Rural)": "9-C Charleston Rural",
        "7-B (Webb City)": "7-B Webb City",
        "8-G (Donald Rural)": "8-G Donald",
        "1-A (Oz Wd 1)": "1-A Ozark Wd.1",
        "5-B (Oz Rural)": "5-B Ozark Rural",
        "2-B (Oz Rural)": "2-B Ozark Rural",
        "9-B (Charleston Wd 3)": "9-B Charleston Wd. 3",
        "2-E (Oz Wd 3)": "2-E Ozark Wd. 3",
        "1-C (Oz WD 2)": "1-B Ozark Wd. 3",
        "8-C (Charleston Rural)": "8-C Charleston Rural",
        })

def fulton(dat):
    dat["prec"] = dat["prec"].replace(
        {"MS - Afton": "MAMMOTH SPRING/AFTON", 
         "Fulton - Mt. Calm": "FULTON/MT CALM"
         })
    dat["prec"] = dat["prec"].str.replace(" - ", "/")

def greene(dat):
    chop_five(dat)
    dat["prec"] = dat["prec"].replace(
        {"Delaplaine - Jones": "Delaplaine-Jones",
        "Lafe - Breckenridge": "Lafe-Breckenridge",
        "Marmaduke - Hurricane": "Marmaduke-Hurricane",
        "Oak Grove - Union": "Oak Grove-Union",
         })

def hempstead(dat):
    dat["prec"] = dat["prec"].str.slice(start=3)

def hotspring(dat):
    dat["prec"] = dat["prec"].replace(
        {"Friendship City": "Friendship"}
    )    

def independence(dat):
    dat["prec"] = dat["prec"].replace(
        {
        "Big Bottom / Wycough / Logan": "Big Bottom Wycough Logan",
        "Black River / Marshall": "Black River/Marshall",
        "Cushman / Union": "Cushman/Union",
        "Greenbrier - Desha": "Greenbrier-Desha",
        "Greenbrier - Jamestown": "Greenbrier-Jamestown",
        "Greenbrier - Locust Grove": "Greenbrier-Locust Grove",
        })

def izard(dat):
    dat["prec"] = dat["prec"].replace(
        {
        "Calico Rock Ward 1": "CALICO ROCK - WARD 1",
        "Calico Rock Ward 2": "CALICO ROCK - WARD 2",
        "Calico Rock Ward 3": "CALICO ROCK - WARD 3",
        "Calico Rock Ward 4": "CALICO ROCK - WARD 4",
        "Horseshoe Bend Ward 1": "HORSESHOE BEND - WARD 1",
        "Horseshoe Bend Ward 2": "HORSESHOE BEND - WARD 2",
        "Horseshoe Bend Ward 3": "HORSESHOE BEND - WARD 3",
        "Horseshoe Bend Ward 4": "HORSESHOE BEND - WARD 4",
        "Melbourne Ward 1": "MELBOURNE - WARD 1",
        "Melbourne Ward 2": "MELBOURNE - WARD 2",
        "Melbourne Ward 3": "MELBOURNE - WARD 3",
        "Melbourne Ward 4": "MELBOURNE - WARD 4",
        "Mt. Pleasant City": "MOUNT PLEASANT CITY",
        "Mt. Pleasant Rural": "MOUNT PLEASANT RURAL",
        })    

def jackson(dat):
    chop_five(dat)
    dat["prec"] = dat["prec"].replace(
        {
        "Crossroads -37": "CROSSROADS-37",
        "Gourdneck - Citizenship": "GOURDNECK-CITIZENSHIP",
        "Newport Ward 1-A": "Newport W 1-A",
        "Newport Ward 1-B": "Newport W 1-B",
        "Newport Ward 2-A": "Newport W 2-A",
        "Newport Ward 3-C": "Newport W 3-C",
        "Newport Ward 4-A": "Newport W 4-A",
        "Newport Ward 4-B": "Newport W 4-B",
        "Newport Ward 2-C": "Newport W 2-C",
        "Newport Ward 2-B": "Newport W 2-B",
        "Newport Ward 3-C": "Newport W 3-C",
        "Newport Ward 3-B": "Newport W 3-B",
        })    

def jefferson(dat):
    dat["prec"] = dat["prec"].str.lstrip("0")
    dat["prec"] = dat["prec"].str.rstrip("X")
    dat["prec"] = dat["prec"].replace(
        {
        "610-1": "610",
        "712-1": "712",
        "713-1": "713",
        "714-1": "714",
        "721-1": "721",
        "731-1": "731",
        "732-1": "732",
        "733-1": "733",
        "810-1": "810",
        "820-1": "820",
        "830-1": "830",
        "820-1": "820",
        }) 

def lafayette(dat):
    dat["prec"] = dat["prec"].str.slice(start=6)
    dat["prec"] = dat["prec"].replace(
        {
        "Stamps Ward 1, Prec 1": "Stamps Ward 1, Pct 1",
        "Stamps Ward 1, Prec 2": "Stamps Ward 1, Pct 2",
        "Bradley City": "Bradley",
        "Buckner City": "Buckner",
        "Lewisville Out": "Lewisville Ward 1 (Out)",
        "Stamps W1 P2 Out": "Stamps Ward 1, Pct 2 (Out)",
        "Stamps W2 Out": "Stamps Ward 2 (Out)",
        "Buckner Out": "Buckner (Out)",
        "Bradley Out": "Bradley (Out)",
        })     
    
def lawrence(dat):
    chop_five(dat)
    dat["prec"] = dat["prec"].replace(
        {
        "Boas #1": "Boas 1",
        "Boas #2": "Boas 2",
        "Boas #3": "Boas 3",
        "Campbell #1": "Campbell 1",
        "Campbell #2": "Campbell 2",
        "Campbell #3": "Campbell 3",
        "Campbell #4": "Campbell 4",
        "Reeds Creek Saffell": "Reed's Creek Saffell",
        "Reeds Creek Strawberry": "REED'S CREEK STRAWBERRY",
        })    

def lee(dat):
    dat["prec"] = dat["prec"].replace(
        {
        "Precinct 1": "JP01",
        "Precinct 2": "JP02",
        "Precinct 3": "JP03",
        "Precinct 4": "JP04",
        "Precinct 5": "JP05",
        "Precinct 6": "JP06",
        "Precinct 7": "JP07",
        "Precinct 8": "JP08",
        "Precinct 9": "JP09",
        })

def lincoln(dat):
    dat["prec"] = dat["prec"].str.slice(start=6)
    dat["prec"] = dat["prec"].replace(
        {
        "Tarry": "Bar/Tarry",
        "Yorktown": "Bar/Yorktown",
        "Lone Pine / Garnett": "Lone Pine/Garnett",
        "Lone Pine / Mt Home": "Lone Pine/Mt. Home",
        "Owen / Glendale": "Owen/Glendale",
        "Owen / Palmyra": "Owen/Palmyra",
        "Wells Bayou": "Wells Bayou/FS",
        })

def littleriver(dat):
    dat["prec"] = dat["prec"].replace(
        {
        "Arden Township": "Arden",
        "Arkinda Township": "Arkinda",
        "Burke Township": "Burke",
        "Caney Township": "Caney",
        "Cleveland Township": "Cleveland",
        "Franklin Township": "Franklin",
        "Jackson Township": "Jackson",
        "Jefferson Township": "Jefferson",
        "Jewell Township": "Jewell",
        "Johnson Township": "Johnson",
        "Lick Creek Township": "Lick Creek",
        "Little River Township": "Little River",
        "Red River Township": "Red River",
        "Wallace / Richland": "Wallace/Richland",
        })
 
def logan(dat):
    dat["prec"] = dat["prec"].str.slice(start=6)
    dat["prec"] = dat["prec"].replace(
        {
        "Sht Mtn WD 1": "Short Mtn Ward 1",
        "Sht Mtn WD 2": "Short Mtn Ward 2",
        "Sht Mtn WD 3": "Short Mtn Ward 3",
        "Sht Mtn WD 4": "Short Mtn Ward 4",
        "Blue Mountain City": "Blue Mtn City",
        "Blue Mountain Rural": "Blue Mtn Rural",
        "Boone WD 1": "Boone Ward 1",
        "Boone WD 2": "Boone Ward 2",
        "Boone WD 3": "Boone Ward 3",
        "Boone WD 4": "Boone Ward 4",
        })

def lonoke(dat):
    dat["prec"] = dat["prec"].replace(
        {
        "05 - Cabot City Ward 1": "05 - Cabot City W/1",
        "06 - Cabot City Ward 2": "06 - Cabot City W/2",
        "07 - Cabot City Ward 3": "07 - Cabot City W/3",
        "08 - Cabot City Ward 4": "08 - Cabot City W/4",
        "13 - Carlisle TWP": "13 - Carlisle Twp.",
        "34 - Lonoke City Ward 1": "34 - Lonoke City W/1",
        "35 - Lonoke City Ward 2": "35 - Lonoke City W/2",
        "36 - Lonoke City Ward 3": "36 - Lonoke City W/3",
        "37 - Lonoke City Ward 4": "37 - Lonoke City W/4",
        "42 - Prairie TWP": "42 - Prairie Twp.",
        "45 - Totten TWP": "45 - Totten Twp.",
        "46 - Walls TWP": "46 - Walls Twp.",
        "47 - Ward City Ward 1": "47 - Ward City W/1",
        "48 - Ward City Ward 2": "48 - Ward City W/2",
        "49 - Ward City Ward 3": "49 - Ward City W/3",
        "51 - Williams TWP": "51 - Williams Twp.",
        "53 - Lonoke City Ward 5": "53 - Lonoke City W/5",
        "54 - Lonoke City Ward 6": "54 - Lonoke City W/6",
        "55 - Lonoke City Ward 7": "55 - Lonoke City W/7",
        "55 - Lonoke City Ward 8": "55 - Lonoke City W/8",
        })
    
def marion(dat):
    dat["prec"] = "P00" + dat["prec"].str.slice(start=9)

def miller(dat):
    dat["prec"] = dat["prec"].replace(
        {
        "Hickory St": "Hickory Street",
        "Hickory St South": "Hickory Street South",
        "Ozan Inghram": "Ozan",
        })

def monroe(dat):
    chop_five(dat)
    dat["prec"] = dat["prec"].replace(
        {"Duncan Township": "duncan",
         "Holly Grove Township": "holly grove",
         "Keevil Township": "keevil",
        })    

def newton(dat):
    dat["prec"] = dat["prec"].replace(
        {"Mt Sherman": "Mt. Sherman"}
        )     

def perry(dat):
    dat["prec"] = dat["prec"].str.slice(start=1, stop=2) + "-" + dat["prec"].str.slice(start=5)  

def polk(dat):
    dat["prec"] = dat["prec"].replace(
        {
        "09 - DALLAS VALLEY/ SHADY": "09 - Dallas Valley",
        "01- MENA": "01 - Precinct 1",
        "02- MENA": "02 - Precinct 2",
        "03- MENA": "03 - Precinct 3",
        })
    chop_five(dat)

def pope(dat):
    chop_five(dat)
    dat["prec"] = dat["prec"].str.replace("-", "")

def prairie(dat):
    dat["prec"] = dat["prec"].replace(
        {
        "Belcher / Tyler": "Belcher/Tyler",
        "White River Ward 1": "Wattensaw City Ward 1",
        "White River Ward 2": "Wattensaw City Ward 2",
        "White River Ward 3": "Wattensaw City Ward 3",
        })    

def pulaski(dat):
    dat["prec"] = dat["prec"].str.slice(start=9)
    dat["prec"] = dat["prec"].str.lstrip("0")

def randolph(dat):
    chop_five(dat)
    dat["prec"] = dat["prec"].replace(
        {
        "Okean": "O'kean",
        "Ward One": "Ward 1",
        "Ward Two": "Ward 2",
        "Ward Three": "Ward 3",
        })

def saline(dat):
    dat["prec"] = "Precinct " + dat["prec"]
    
def scott(dat):
    chop_five(dat)
    dat["prec"] = dat["prec"].replace(
        {
        "Lewis 1": "Lewis Ward 1",
        "Lewis 2": "Lewis Ward 2",
        "Lewis 3": "Lewis Ward 3"
        })
        
def sebastian(dat):
    dat["prec"] = dat["prec"].str.slice(start=9)

def stone(dat):
    dat["prec"] = dat["prec"].replace(
        {
        "Angora Mtn": "Angora Mountain",
        "Dodd Mtn": "Dodd Mountain"
        })
    
def washington(dat):
    dat["prec"] = dat["prec"].replace(
        {
        "Prairie Gr City - House": "Prairie Gr City-House",
        "Prairie Gr City - Senate": "Prairie Gr City-Senate",
        "Richland - Senate": "Richland-Senate",
        })

def woodruff(dat):   
    dat["prec"] = dat["prec"].map(lambda s: str(s)[-2:])

"""
overall call function
"""
countyToCountyCleaner = {
    "Arkansas": arkansas,
    "Ashley": ashley,
    "Benton": benton,
    "Bradley": bradley,
    "Carroll": carroll,
    "Chicot": chicot,
    "Clark": clark,
    "Clay": clay,
    "Cleburne": chop_five,
    "Cleveland": chop_five,
    "Columbia": columbia,
    "Conway": conway,
    "Crawford": crawford,
    "Cross": cross,
    "Dallas": chop_five,
    "Desha": desha,
    "Drew": drew,
    "Faulkner": faulkner,
    "Franklin": franklin,
    "Fulton": fulton,
    "Grant": chop_five,
    "Greene": greene,
    "Hempstead": hempstead,
    "Hot Spring": hotspring,
    "Howard": chop_five,
    "Independence": independence,
    "Izard": izard,
    "Jefferson": jefferson,
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
    "Newton": newton,
    "Perry": perry,
    "Pike": chop_five,
    "Polk": polk,
    "Pope": pope,
    "Prairie": prairie,
    "Pulaski": pulaski,
    "Randolph": randolph,
    "Saline": saline,
    "Scott": scott,
    "Stone": stone,
    "Washington": washington,
    "White": chop_five,
    "Woodruff": woodruff,
    "Yell": chop_five,
    }

# to test for select counties
# raw_df = shp_df.loc[
#    (shp_df['county_nam'] == "Desha") | 
#    (shp_df['county_nam'] == "Benton") | 
#    (shp_df['county_nam'] == "Woodruff")]

clean_df = shp_df.sort_values(by=['county_nam']) # you have to sort the counties alphabetically whowwwwww

counties = pd.Series(clean_df['county_nam']).unique()
clean_df["prec"] = clean_df["precinct"].copy()
clean_df.set_index(['county_nam', 'precinct'], inplace=True)

for county in counties: 
    county_dat = clean_df.loc[county]
    changed = countyToCountyCleaner.get(county, lambda x: x)(county_dat) # why lambda x?
    clean_df.update(county_dat)

clean_df['prec_final'] = clean_df['prec'].str.lower()
clean_df.reset_index(inplace=True)

clean_df.to_file("/Users/hopecj/projects/AR/Shapefiles/clean.shp")