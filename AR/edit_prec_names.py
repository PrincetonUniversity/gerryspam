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


def ashley(dat):
    chop_five(dat)
    dat["prec"] = dat["prec"].replace({
        "Crossett Ward 1": "CW1",
        "Crossett Ward 2": "CW2",
        "Crossett Ward 3": "CW3",
        "Cross Roads": "CROSSROADS",
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

def baxter(dat):
    dat["prec"] = dat["prec"] + "b"


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

def boone(dat):
    dat["prec"] = dat["prec"].replace(
        {
            "Diamond City (12)": "District 12",
        })

def bradley(dat):
    chop_five(dat)
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
            "SW & SE Hickory": "SW/SE HICKORY",
        })


def chicot(dat):
    chop_five(dat)
    dat["prec"] = dat["prec"].replace(
        {" Carlton": "Carlton 1 & 2",
         " Carlton 2": "Carlton 1 & 2",
         })

def clark(dat):
    dat["prec"] = dat["prec"].replace(
        {
            "Central 1": "Central",
            "Curtis 1": "Curtis",
            "East County 1": "East County",
            "Gum Springs Outside 1": "Gum Springs Outside",
            "Gum Springs 1": "Gum Springs Inside",
            "Gurdon Gen 1": "Gurdon General",
            "Hollywood 1": "Hollywood",
            "North East County": "Northeast County",
            "Okolona City 1": "Okolona City",
            "South County 1": "South County",
            "West County 1": "West County",
            "Whelen Springs 1": "Whelen Springs",
        })


def clay(dat):
    chop_five(dat)
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
    
def cleveland(dat):
    chop_five(dat)
    dat["prec"] = dat["prec"].replace(
        {" Kingsland Out": "Kingsland outside", })




def columbia(dat):
    dat["prec"] = dat["prec"].replace(
        {"Taylor City": "Taylor", "Waldo City": "Waldo"})


def conway(dat):
    dat["prec"] = dat["prec"].str.slice(start=6)
    dat["prec"] = dat["prec"].replace(
        {"St Vincent": "St. Vincent", 
         "Lick Mountain": "Lick Mtn.",
         "Morrilton Ward 1": "Ward 1",
         "Morrilton Ward 2": "Ward 2",
         "Morrilton Ward 3": "Ward 3",
         "Morrilton Ward 4": "Ward 4",
         "nifee City": "menifee city",
         })


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

def dallas(dat):
    chop_five(dat)
    dat["prec"] = dat["prec"].replace(
        {" District 5 -": "district 5", 
    })

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
            "1-C (Oz WD 2)": "1-C Ozark Wd.2",
            "8-C (Charleston Rural)": "8-C Charleston Rural",
        })


def fulton(dat):
    dat["prec"] = dat["prec"].replace(
        {"MS - Afton": "MAMMOTH SPRING/AFTON",
         "Fulton - Mt. Calm": "FULTON/MT CALM"
         })
    dat["prec"] = dat["prec"].str.replace(" - ", "/")

def garland(dat): 
    dat["prec"] = dat["prec"].str.lstrip("0")


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
    dat["prec"] = dat["prec"].replace(
        {"Cross Roads": "Crossroads",
         })

def hotspring(dat):
    dat["prec"] = dat["prec"].replace(
        {"Friendship City": "Friendship",
        "Malvern W-1": "ward 1",
        "Malvern W-2": "ward 2",
        "Malvern W-3": "ward 3",
        "Malvern W-4": "ward 4",
         }
    )

def howard(dat):
    chop_five(dat)
    dat["prec"] = dat["prec"].replace(
        {
        "ineral Spring 3": "Mineral spring 3",
         }
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
            "Newport Ward 3-C": "Newport W 3-A-C",
            "Newport Ward 4-A": "Newport W 4-A",
            "Newport Ward 4-B": "Newport W 4-B",
            "Newport Ward 2-C": "Newport W 2-C",
            "Newport Ward 2-B": "Newport W 2-B",
            "Newport Ward 3-B": "Newport W 3-B",
            "Penninghton Balch": "PENNINGTON BALCH",
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
            "E Lincoln Co FD": "SE Lincoln Co FD",
            "ells Bayou": "Wells Bayou/FS",
            "Tarry": "Bar/Tarry",
            "Yorktown": "Bar/Yorktown",
            "Lone Pine / Garnett": "Lone Pine/Garnett",
            "Lone Pine / Mt Home": "Lone Pine/Mt. Home",
            "Owen / Glendale": "Owen/Glendale",
            "Owen / Palmyra": "Owen/Palmyra",
            "Wells Bayou": "Wells Bayou/FS",
            "Grady City W1 & W2": "Grady City W1& W2",
            "ould City W1": "Gould City W1",
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
            "01 - Allport City": "01- Allport City",
            "11 - Carlisle City Ward 2": "11 -Carlisle City Ward 2",
            "19 - England City Ward 3": "19- England City Ward 3",
            "56 - Lonoke City Ward 8": "56 - Lonoke City W/8",
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

def montgomery(dat):
    chop_five(dat)
    dat["prec"] = dat["prec"].replace(
        {"MOUNT IDA - IN": "Mount Ida - Inside",
         "MOUNT IDA - OUT": "Mount Ida - Outside",
         "NORMAN - IN": "Norman - Inside",
         "NORMAN - OUT": "Norman - Outside",
         "ODEN - IN": "Oden - Inside",
         "ODEN - OUT": "Oden - Outside",
         })

def newton(dat):
    dat["prec"] = dat["prec"].replace(
        {"Mt Sherman": "Mt. Sherman"}
    )


def perry(dat):
    dat["prec"] = dat["prec"].str.lstrip("0")
    dat["prec"] = dat["prec"].replace(
        {"1 - Aplin": "1-aplin",
         "10 - Perry": "10-perry",
         "11 - Petit Jean": "11-petit jean",
         "12 - Rankin": "12-rankin",
         "13 - Rose Creek": "13-rose creek",
         "14 - Tyler": "14-tyler",#
         "15 - Union": "15-union",
         "16 - Union Valley": "16-union valley",
         "17 - Wye": "17-Wye",
         "2 - Casa": "2-Casa",
         "3 - Cherry Hill": "3-Cherry Hill",
         "4 - Fourche": "4-Fourche",
         "5 - Houston": "5-Houston",
         "6 - Kenney": "6-Kenney",
         "7 - Lake": "7-Lake",
         "8 - Maumelle": "8-Maumelle",
         "9 - New Tennessee": "9-New Tennessee",
         })


def phillips(dat):
    dat["prec"] = dat["prec"].replace(
        {
            "Bush": "PRECINCT 0001",
            "Cleburne I": "PRECINCT 0008",
            "Cleburne II": "PRECINCT 0008",
            "Cleveland": "PRECINCT 0014",
            "Cypress": "PRECINCT 0014",
            "Elaine I": "PRECINCT 0016",
            "Elaine II": "PRECINCT 0016",
            "Helena West Helena 1": "PRECINCT 0001",
            "Helena West Helena 2": "PRECINCT 0003",
            "Helena West Helena 3": "PRECINCT 0005/0006",
            "Hickory Ridge Marvell 1": "PRECINCT 0013",
            "Hickory Ridge Marvell I": "PRECINCT 0013",
            "Hickory Ridge Marvell II": "PRECINCT 0013",
            "Hickory Ridge Marvell III": "PRECINCT 0013",
            "Hicksville": "PRECINCT 0013",
            "Honor VII": "PRECINCT 0007",
            "Hornor": "PRECINCT 0007",
            "Hornor II": "PRECINCT 0007",
            "Hornor III": "PRECINCT 0007",
            "Hornor IV": "PRECINCT 0007",
            "Hornor V": "PRECINCT 0007",
            "Hornor VI": "PRECINCT 0007",
            "L-Anquille": "PRECINCT 0001",
            "Lake": "PRECINCT 0002",
            "Lakeview City": "PRECINCT 0015",
            "Lexa City": "PRECINCT 0010",
            "Lower Big Creek": "PRECINCT 0014",
            "Marion": "PRECINCT 0011",
            "Marion I": "PRECINCT 0011",
            "Mooney": "PRECINCT 0017",
            "Searcy I": "PRECINCT 0015",
            "Searcy II": "PRECINCT 0015",
            "Searcy III": "PRECINCT 0015",
            "Spring Creek I": "PRECINCT 0009",
            "Spring Creek II": "PRECINCT 0009",
            "Spring Creek III": "PRECINCT 0009",
            "Spring Creek IV": "PRECINCT 0010",
            "Spring Creek V": "PRECINCT 0009",
            "St Francis I": "PRECINCT 0001",
            "St Francis II": "PRECINCT 0001",
            "St Francis IV": "PRECINCT 0001",
            "Tappan I": "PRECINCT 0016",
            "Tappan II": "PRECINCT 0016",
            "Upper Big Creek": "PRECINCT 0012",
        })


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
            "White River Ward 1": "White River City Ward 1",
            "White River Ward 2": "White River City Ward 2",
            "White River Ward 3": "White River City Ward 3",
        })


def pulaski(dat):
    dat["prec"] = dat["prec"].str.slice(start=9)
    dat["prec"] = dat["prec"].str.lstrip("0")


def randolph(dat):
    chop_five(dat)
    dat["prec"] = dat["prec"].replace(
        {
            "Elevenpoint": "Eleven point",
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
            "Lewis 3": "Lewis Ward 3",
            "Mt. Pleasant": "Mount Pleasant",
        })


def sebastian(dat):
    dat["prec"] = dat["prec"].str.slice(start=9)

def sevier(dat):
    dat["prec"] = dat["prec"].replace(
        {
            "De Queen Northwest": "DQ northwest",
        })

def stone(dat):
    dat["prec"] = dat["prec"].replace(
        {
            "Angora Mtn": "Angora Mountain",
            "Dodd Mtn": "Dodd Mountain"
        })


def union(dat):
    dat["prec"] = dat["prec"].replace(
        {
            "Country Box # 1": "Country Box #1",
            "Country Box # 2": "Country Box #2",
            "Country Box # 3": "Country Box #3",
            "Country Box # 4": "Country Box #4",
            "Country Box # 5": "Country Box #5",
            "Country Box # 6": "Country Box #6",
            "Country Box # 7": "Country Box #7",
            "Mt Holly": "mt. holly",
            "Ward 1": "ward #1",
            "Ward 2": "ward #2",
            "Ward 3": "ward #3",
            "Ward 4": "ward #4",
            "Woolleys Store": "WOOLEYS STORE",
        })


def washington(dat):
    dat["prec"] = dat["prec"].replace(
        {
            "Prairie Gr City - House": "Prairie Gr City-House",
            "Prairie Gr City - Senate": "Prairie Gr City-Senate",
            "Richland - Senate": "Richland-Senate",
            "Fay 01": "Fay 1",
            "Fay 02": "Fay 2",
            "Fay 03": "Fay 3",
            "Fay 04": "Fay 4",
            "Fay 05": "Fay 5",
            "Fay 06": "Fay 6",
            "Fay 07": "Fay 7",
            "Fay 08": "Fay 8",
            "Spg 01": "Spg 1",
            "Spg 02": "Spg 2",
            "Spg 03": "Spg 3",
            "Spg 04": "Spg 4",
            "Spg 05": "Spg 5",
            "Spg 06": "Spg 6",
            "Spg 07": "Spg 7",
            "Spg 08": "Spg 8",
            "Spg 09": "Spg 9",
        })

def woodruff(dat):
    dat["prec"] = dat["prec"].replace(
        {
            "Augusta - 01": "Augusta Armory -01",
            "Augusta - 02": "Augusta Armory-02",
            "Augusta - 03": "Augusta Hsng Authority-03",
            "Cotton Plant - 08": "Babbs/Cotton Plant-08",
            "Cotton Plant - 09": "Babbs/Cotton Plant-09",
            "Cotton Plant/ Freeman - 07": "Babbs Cottn PL/Freeman-07",
            "Fakes Chapel - 20": "Fairgrounds Fakes Chpl-20",
            "Gregory - 06": "Gregory-06",
            "Hilleman - 13": "White Hall Church-13",
            "Howell - 12": "Fairgrounds/Howell-12",
            "Hunter - 11": "Hunter Methodist-11",
            "McCrory - 17": "McCrory Civic Center-17",
            "McCrory - 18": "McCrory Civic-18",
            "McCrory Rural - 15": "Frgrnds/McCrory Rural-15",
            "Morton - 14": "Morton Baptist-14",
            "North Rural Augusta - 04": "Augusta Armory-04",
            "Patterson - 16": "Patterson Fire Station-16",
            "Pumkin Bend - 19": "Pumpkin Bend Church-19",
            "Rural Hunter - 10": "Hunter Methodist/Rural-10",
            "South Rural Augusta - 05": "Augusta Armory-05",
        })

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
