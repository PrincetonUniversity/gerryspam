import geopandas as gpd
import pandas as pd
import numpy as np
import re

shp_path = '/Users/hopecj/projects/AR/Shapefiles/AR Precincts 10_11_2019/ELECTION_PRECINCTS.shp'
elec_path = '/Users/hopecj/projects/AR/elections/AR_G18.csv'

elec_df = pd.read_csv(elec_path)

shp_df = gpd.read_file(shp_path)
shp_df = shp_df[['county_nam', 'precinct','geometry']]
shp_df.groupby(['county_nam']).ngroups #sigh.....75 counties

out = shp_df.loc[shp_df['county_nam'] == 'St. Francis']
out = out.drop(['geometry', 'county_nam'], axis=1)
out.to_csv("/Users/hopecj/projects/AR/stfrancis.csv")

# function to clean
def ar_prec_transform(dat, county, custom_transformation=None, upper=True, 
       chop_five_digs=False, chop_three_digs=False, chop_six_digs=False, dash_to_slash=False, 
       jefferson_transform=False, marion_transform=False, perry_transform=False, pope_transform=False,
       pulaski_transform=False, saline_transform=False, sebastian_transform=True):
       dat_out = dat.loc[dat['county_nam'] == county]
       dat_out['prec_new'] = dat_out['precinct'].copy()
       if chop_three_digs:
              dat_out['prec_new'] = dat_out['prec_new'].str.slice(start = 3)
       if chop_five_digs:
              dat_out['prec_new'] = dat_out['prec_new'].str.slice(start = 5)
       if chop_six_digs:
              dat_out['prec_new'] = dat_out['prec_new'].str.slice(start = 6)
       if dash_to_slash: 
              dat_out['prec_new'] = dat_out['prec_new'].str.replace(" - ", "/")
       if jefferson_transform:
              dat_out['prec_new'] = dat_out['prec_new'].str.lstrip("0")
              dat_out['prec_new'] = dat_out['prec_new'].str.rstrip("X")
       if perry_transform:
              dat_out['prec_new'] = dat_out['prec_new'].str.slice(start = 1, stop = 2) + '-' + dat_out['prec_new'].str.slice(start = 5)
       if marion_transform:
              dat_out['prec_new'] = 'P00' + dat_out['prec_new'].str.slice(start = 9)
       if pope_transform: 
              # last_char = dat_out['prec_new'].str[-1]
              # last_char_num_bool = last_char.str.isnumeric()
             # if dat_out[dat_out['prec_new'].str.contains("Russellville")]: # if it contains Russellville, remove the dash
              dat_out['prec_new'] = dat_out['prec_new'].str.replace('-','')
              # elif last_char_num_bool: # else, if it contains a number, put a '#' before a number 
              #        dat_out['prec_new'] = dat_out['prec_new'].str[0:-2] + '#' + dat_out['prec_new'].str[-1]
                     # dat_out['prec_new'] = dat_out['prec_new'].str.slice(start = 0, stop = -2) + '#' + dat_out['prec_new'].str.slice(start = -1, stop = -1)
       if pulaski_transform:
              dat_out['prec_new'] = dat_out['prec_new'].str.slice(start = 9)
              dat_out['prec_new'] = dat_out['prec_new'].str.lstrip("0")
       if saline_transform: 
              dat_out['prec_new'] = 'Precinct ' + dat_out['prec_new']
       if sebastian_transform:
              dat_out['prec_new'] = dat_out['prec_new'].str.slice(start = 9)
       dat_out = dat_out.replace(
              custom_transformation # NB: the replace will edit the old column, so if you want the original 'precinct' from shp, merge it back in
       )
       if upper:
              dat_out['prec_new'] = dat_out['prec_new'].str.upper()
       return dat_out



# arkansas cnty
c1 = ar_prec_transform(shp_df, 'Arkansas', 
       {'DEWITT 1': 'DEWITT WARD 1', 
       'DEWITT 2': 'DEWITT WARD 2',
       'DEWITT 3': 'DEWITT WARD 3',
       'STUTTGART 1': 'STUTTGART WARD 1',
       'STUTTGART 2': 'STUTTGART WARD 2', 
       'STUTTGART 3': 'STUTTGART WARD 3'},
       chop_five_digs=True)

# ashley cnty
c2 = ar_prec_transform(shp_df, 'Ashley',
       {'CROSSETT WARD 1': 'CW 1',
       'CROSSETT WARD 2': 'CW 2',
       'CROSSETT WARD 3': 'CW 3',
       'FOUNTAIN HILL CITY': 'FH CITY',
       'FOUNTAIN HILL CITY': 'FH RURAL',
       'HAMBURG WARD 1': 'HW1',
       'HAMBURG WARD 2': 'HW2',
       'HAMBURG WARD 3': 'HW3',
       'MT. ZION': 'MT ZION',
       'NORTH CROSSETT EAST': 'NCE',
       'NORTH CROSSETT WEST': 'NCW',
       'SNYDER / TRAFALGAR': 'SNY/TRA',
       'VO - TECH': 'VOTECH',
       'WEST CROSSETT RURAL': 'WCR'},
       chop_five_digs=True)

# baxter cnty
c3 = ar_prec_transform(shp_df, 'Baxter', upper=False)

# benton cnty
c4 = ar_prec_transform(shp_df, 'Benton', {
       'Precinct 01': 'Precinct 1',
       'Precinct 02': 'Precinct 2',
       'Precinct 03': 'Precinct 3',
       'Precinct 04': 'Precinct 4',
       'Precinct 05': 'Precinct 5',
       'Precinct 06': 'Precinct 6',
       'Precinct 07': 'Precinct 7',
       'Precinct 08': 'Precinct 8',
       'Precinct 09': 'Precinct 9'}, 
       upper=False)

# boone cnty
# COME BACK after contacting county
# big mismatch in number of precincts (more in election results)
c5 = ar_prec_transform(shp_df, 'Boone', )

# bradley cnty
c6 = ar_prec_transform(shp_df, 'Bradley', {
       'Warren Ward 1': 'Ward 1',
       'Warren Ward 2': 'Ward 2',
       'Warren Ward 3': 'Ward 3'},  
       upper=False, 
       chop_five_digs=True
)

# calhoun cnty 
# COME BACK & figure out the deal with watson addition in election results
c7 = ar_prec_transform(shp_df, 'Calhoun', upper=False)

# carroll cnty
c8 = ar_prec_transform(shp_df, 'Carroll', {
       'Berryville Ward 1': 'BV Ward 1',
       'Berryville Ward 2': 'BV Ward 2',
       'Eureka Springs Ward 1': 'ES Ward 1',
       'Eureka Springs Ward 2': 'ES Ward 2',
       'Eureka Springs Ward 3': 'ES Ward 3',
       'Green Forest Ward 1': 'GF Ward 1',
       'Green Forest Ward 2': 'GF Ward 2',
       'North East Hickory': 'NE Hickory',
       'Northwest Hickory': 'NW Hickory',
       'Long Creek': 'Lng Crk',
       'SW & SE HICKORY': 'SW/SE HICKORY'})

# chicot cnty
# might need to chop another digit
c9 = ar_prec_transform(shp_df, 'Chicot', {
       'Carlton': 'Carlton 1'},
       upper=False,
       chop_five_digs=True)

# clark cnty
c10 = ar_prec_transform(shp_df, 'Clark', {
       'Central 1': 'Central',
       'Curtis 1': 'Curtis',
       'East County 1': 'East County',
       'Gum Springs Outside 1': 'Gum Springs Outside',
       'Gum Springs 1': 'Gum Springs Inside',
       'Gurdon Gen 1': 'Gurdon General',
       'North East County': 'Northeast County',
       'Okolona City 1': 'Okolona City',
       'South County 1': 'South County',
       'West County 1': 'West County',
       'Whelen Springs 1': 'Whelen Springs'})

# clay county
c11 = ar_prec_transform(shp_df, 'Clay', {
       'Bennett & Lemmons': 'Bennett and Lemmons',
       'E Oak Bluff & Blue Cane': 'East Oak Bluff & Blue Cane',
       'Liddell & chalk Bluff': 'Liddell & Chalk Bluff',
       'Cleveland & N Kilgore': 'N Kilgore & Cleveland',
       'North St Francis': 'North St. Francis',
       'Gleghorn & S Kilgore': 'S Kilgore & Gleghorn',
       'South St Francis': 'South St. Francis'},
       upper=False,
       chop_five_digs=True)

# cleburne county
# also transformed the elections data to remove last three numbers
c12 = ar_prec_transform(shp_df, 'Cleburne', chop_five_digs=True)

# cleveland county
c13 = ar_prec_transform(shp_df, 'Cleveland', upper=False, chop_five_digs=True)

# columbia county
c14 = ar_prec_transform(shp_df, 'Columbia', {
       'Taylor City': 'Taylor',
       'Waldo City': 'Waldo'})

# conway county
c15 = ar_prec_transform(shp_df, 'Conway', {
       'St Vincent': 'St. Vincent',
       'Lick Mountain': 'Lick Mtn.'})

# craighead
# took the "precinct" out of elections data
c16 = ar_prec_transform(shp_df, 'Craighead',
       upper=False)

# crawford 
c17 = ar_prec_transform(shp_df, 'Crawford', {
       'Alma 01': 'Alma 1', 
       'Alma 02': 'Alma 2', 
       'Alma 03': 'Alma 3', 
       'Alma 04': 'Alma 4', 
       'Cove City': 'Cove City CSD',
       'Lee Creek': 'Lee Creek CSD',
       'Mulberry 01': 'Mulberry 1',
       'Mulberry 02': 'Mulberry 2',
       'Mulberry 03': 'Mulberry 3'},
       upper=False)

# crittenden
# need to revisit. none of these names match up
c18 = ar_prec_transform(shp_df, 'Crittenden', chop_five_digs=False)

# cross
c19 = ar_prec_transform(shp_df, 'Cross', {
       'Bay Village / Birdeye': 'Bay Village, Birdeye',
       'Cherry Valley': 'Cherry Valley City',
       'Tyronza / Twist': 'Tyronza, Twist',
       'Wynne Ward 1': 'WYNNE WARD 1',
       'Wynne Ward 2': 'WYNNE WARD 2',
       'Wynne Ward 3': 'WYNNE WARD 3',
       'Wynne Ward 4': 'WYNNE WARD 4',
       'Wynne Ward 5': 'WYNNE WARD 5'},
       upper=False)

# dallas
c20 = ar_prec_transform(shp_df, 'Dallas', upper=False, chop_five_digs=True)

# desha cnty
c21 = ar_prec_transform(shp_df, 'Desha', {
       'Bowie W1': 'Bowie 1',
       'Bowie W2': 'Bowie 2',
       'Bowie W3': 'Bowie 3',
       'Mitcheville': 'Mitchellville',
       'Rand W1': 'Randolph 1',
       'Rand W2': 'Randolph 2',
       'Rand W3': 'Randolph 3',
       'Rand W4': 'Randolph 4',
       'Rand Rural': 'Randolph Rural',
       'Silver Lake': 'Silverlake'},
       chop_five_digs=True)

# drew cnty
c22 = ar_prec_transform(shp_df, 'Drew', {
       'Mar N Box 1': 'MN BOX 1 - RH Cumb. Presb', # need to confirm
       'Mar N Box 2': 'MN Box 2 - RH Baptist Chu', # need to confirm
       'Marion South': 'Marion South - Shady Grov'},
       upper=False,
       chop_five_digs=True)

# faulkner cnty
c23 = ar_prec_transform(shp_df, 'Faulkner', {
       'Wilson 35': '35 Wilson',
       'West Cadron 14': '14 W Cadron',
       'Walker 38': '38 Walker',
       'Vilonia City 21': '21 Vilonia',
       'Union 37': ' 37 Union',
       'Pine Mt 36': '36 Pine Mt.',
       'Palarm 39': ' 39 Palarm',
       'Newton 34': '34 Newton',
       'Mountain 32': '32 Mountain',
       'Mount Vernon 33': '33 Mt. Vernon',
       'Matthews 31': '31 Matthews',
       'Harve 30': '30 Harve',
       'Hardin Rural 28': '28 Hardin',
       'Hardin City West (GB) 55': '55.01 Hardin GB West',
       'Hardin City East (GB) 29': '29.01 Hardin GB East',
       'Enola 27': '27 Enola',
       'East Fork 26': '26 East Fork',
       'Eagle 25': '25 Eagle',
       'E Cadron C 48': '48 E Cadron C',
       'E Cadron B 13': '13 E Cadron B',
       'E Cadron A 12': '12  E Cadron A',
       'Danley Rural 23': '23 Danley',
       'Danley City (Mayflower) 24': '24 Mayflower',
       'Cypress Rural 22': '22 Cypress',
       'Clifton 19': '19 Clifton',
       'California 18': '18 CA',
       'Bristol 17': '17 Bristol',
       'Benton 16': '16 Benton',
       'Benedict 15': '15 Benedict',
       '4f Conway City 05': '05 4F',
       '4e Conway City 03': '03.01 4E',
       '4d Conway City 04': '04.01 4D',
       '4c Conway City 11': '11 4C',
       '4b Conway City 02': '02 4B',
       '4a Conway City 01': '01.01 4A',
       '3g Conway City 54': '54 3G',
       '3f Conway City 53': '53 3F',
       '3e Conway City 45': '45.01 3E',
       '3d Conway City 50': '50.01 3D',
       '3c-West Conway City 46': '46 3C-W',
       '3c-East Conway City 09': '09 3C-E',
       '3b Conway City 08': '08 3B',
       '3a Conway City 10': '10 3A',
       '2c Conway City 49': '49 2C',
       '2b Conway City 06': '06.01 2B',
       '2a Conway City 07': '07 2A',
       '1e-West Conway City 44': '44 1E-W',
       '1e-East Conway City 43': '43 1E-E',
       '1c-South Conway City 42': '42 1C-S',
       '1c-North Conway City 41': '41 1C-N'},
       upper=False)

# franklin cnty
c22 = ar_prec_transform(shp_df, 'Franklin', {
       '7-C (Etna)': '7-C Etna',
       '6-B (Altus City)': '6-B Altus City',
       '7-A (Cecil)': '7-A Cecil',
       '3-E (Watalula)': '3-E Watalula',
       '2-D (Wallace/Ivy)': '2-D Wallace/Ivy',
       '1-B (Oz Wd 3)': '1-B Ozark Wd. 3',
       '2-A (Oz Wd 2)': '2-A Ozark Wd. 2',
       '3-F (Mountain)': '3-F Mountain',
       '5-A (Wallace/Ivy)': '5-A Wallace/Ivy',
       '9-A (Charleston Wd 2)': '9-A Charleston Wd. 2',
       '3-A (Lonelm/Cravens)': '3-A Lone Elm/Cravens',
       '8-A (Branch City)': '8-A Branch City',
       '4-B (Watalula)': '4-B Watalula',
       '3-D (Jethro)': '3-D Jethro',
       '3-B (Fern)': '3-B Fern',
       '7-D (Donald Rural)': '7-D Donald',
       '3-C (Boston)': '3-C Boston',
       '8-B (Charleston Wd 1)': '8-B Charleston Wd. 1',
       '8-D (Vesta)': '8-D Vesta',
       '6-D (Weiderkehr Village)': '6-D W.V. City',
       '8-F (Cecil)': '8-F Cecil',
       '5-C (Webb City)': '5-C Webb City',
       '2-C (Lonelm/Cravens)': '2-C Lone Elm/Cravens',
       '4-C (WV Rural)': '4-C W-V Rural',
       '6-A (Altus Rural)': '6-A Altus Rural',
       '6-C (Denning)': '6-C Denning City',
       '4-D (Oz Rural)': '4-D Ozark Rural',
       '4-A (Philpot)': '4-A Philpot',
       '8-E (Donald Rural)': '8-E Donald',
       '9-C (Charleston Rural)': '9-C Charleston Rural',
       '7-B (Webb City)': '7-B Webb City',
       '8-G (Donald Rural)': '8-G Donald',
       '1-A (Oz Wd 1)': '1-A Ozark Wd.1',
       '5-B (Oz Rural)': '5-B Ozark Rural',
       '2-B (Oz Rural)': '2-B Ozark Rural',
       '9-B (Charleston Wd 3)': '9-B Charleston Wd. 3',
       '2-E (Oz Wd 3)': '2-E Ozark Wd. 3',
       '1-C (Oz WD 2)': '1-B Ozark Wd. 3',
       '8-C (Charleston Rural)': '8-C Charleston Rural'},
       upper=False)

# fulton cnty
c23 = ar_prec_transform(shp_df, 'Fulton', {
       'MS - Afton': 'MAMMOTH SPRING/AFTON',
       'Fulton - Mt. Calm': 'FULTON/MT CALM'},
       dash_to_slash=True)

# garland cnty
c24 = ar_prec_transform(shp_df, 'Garland', upper=False)

# grant county
c25 = ar_prec_transform(shp_df, 'Grant', upper=False, chop_five_digs=True)

# greene county 
c26 = ar_prec_transform(shp_df, "Greene", {
       'Delaplaine - Jones': 'Delaplaine-Jones',
       'Lafe - Breckenridge': 'Lafe-Breckenridge',
       'Marmaduke - Hurricane': 'Marmaduke-Hurricane',
       'Oak Grove - Union': 'Oak Grove-Union'},
       upper=False,
       chop_five_digs=True)

# Hempstead county
c27 = ar_prec_transform(shp_df, 'Hempstead', chop_three_digs=True, upper=False)

# hot spring county
c28 = ar_prec_transform(shp_df, 'Hot Spring', {
       'Friendship City': 'Friendship'},
       upper=False)

# howard county
c29 = ar_prec_transform(shp_df, 'Howard', upper=False, chop_five_digs=True)

# independence county
c30 = ar_prec_transform(shp_df, 'Independence', {
       'Big Bottom / Wycough / Logan': 'Big Bottom Wycough Logan',
       'Black River / Marshall': 'Black River/Marshall',
       'Cushman / Union': 'Cushman/Union',
       'Greenbrier - Desha': 'Greenbrier-Desha',
       'Greenbrier - Jamestown': 'Greenbrier-Jamestown',
       'Greenbrier - Locust Grove': 'Greenbrier-Locust Grove'},
       upper=False)

# izard county
c31 = ar_prec_transform(shp_df, 'Izard', {
       'Calico Rock Ward 1': 'CALICO ROCK - WARD 1',
       'Calico Rock Ward 2': 'CALICO ROCK - WARD 2',
       'Calico Rock Ward 3': 'CALICO ROCK - WARD 3',
       'Calico Rock Ward 4': 'CALICO ROCK - WARD 4',
       'Horseshoe Bend Ward 1': 'HORSESHOE BEND - WARD 1',
       'Horseshoe Bend Ward 2': 'HORSESHOE BEND - WARD 2',
       'Horseshoe Bend Ward 3': 'HORSESHOE BEND - WARD 3',
       'Horseshoe Bend Ward 4': 'HORSESHOE BEND - WARD 4',
       'Melbourne Ward 1': 'MELBOURNE - WARD 1',
       'Melbourne Ward 2': 'MELBOURNE - WARD 2',
       'Melbourne Ward 3': 'MELBOURNE - WARD 3',
       'Melbourne Ward 4': 'MELBOURNE - WARD 4',
       'Mt. Pleasant City': 'MOUNT PLEASANT CITY',
       'Mt. Pleasant Rural': 'MOUNT PLEASANT RURAL'})

#Jackson county
c32 = ar_prec_transform(shp_df, 'Jackson', {
       'Crossroads -37': 'CROSSROADS-37',
       'Gourdneck - Citizenship': 'GOURDNECK-CITIZENSHIP',
       'Newport Ward 1-A': 'Newport W 1-A', 
       'Newport Ward 1-B': 'Newport W 1-B', 
       'Newport Ward 2-A': 'Newport W 2-A', 
       'Newport Ward 3-C': 'Newport W 3-C', 
       'Newport Ward 4-A': 'Newport W 4-A', 
       'Newport Ward 4-B': 'Newport W 4-B', 
       'Newport Ward 2-C': 'Newport W 2-C', 
       'Newport Ward 2-B': 'Newport W 2-B', 
       'Newport Ward 3-C': 'Newport W 3-C', 
       'Newport Ward 3-B': 'Newport W 3-B'},
       chop_five_digs=True)

# jefferson county
c33 = ar_prec_transform(shp_df, 'Jefferson', {
       '610-1': '610',
       '712-1': '712',
       '713-1': '713',
       '714-1': '714',
       '721-1': '721',
       '731-1': '731',
       '732-1': '732',
       '733-1': '733',
       '810-1': '810',
       '820-1': '820',
       '830-1': '830',
       '820-1': '820'},
       jefferson_transform=True)

# johnson county
c34 = ar_prec_transform(shp_df, 'Johnson', upper=False)

# lafayette county
c35 = ar_prec_transform(shp_df, 'Lafayette', {
       'Stamps Ward 1, Prec 1': 'Stamps Ward 1, Pct 1',
       'Stamps Ward 1, Prec 2': 'Stamps Ward 1, Pct 2',
       'Bradley City': 'Bradley',
       'Buckner City': 'Buckner',
       'Lewisville Out': 'Lewisville Ward 1 (Out)',
       'Stamps W1 P2 Out': 'Stamps Ward 1, Pct 2 (Out)',
       'Stamps W2 Out': 'Stamps Ward 2 (Out)',
       'Buckner Out': 'Buckner (Out)',
       'Bradley Out': 'Bradley (Out)'},
       chop_six_digs=True,
       upper=False)

# lawrence county
c36 = ar_prec_transform(shp_df, 'Lawrence', {
       'Boas #1': 'Boas 1',
       'Boas #2': 'Boas 2',
       'Boas #3': 'Boas 3',
       'Campbell #1': 'Campbell 1',
       'Campbell #2': 'Campbell 2',
       'Campbell #3': 'Campbell 3',
       'Campbell #4': 'Campbell 4',
       'Reeds Creek Saffell': "Reed's Creek Saffell",
       'Reeds Creek Strawberry': "REED'S CREEK STRAWBERRY"},
       chop_five_digs=True)

# lee county
c37 = ar_prec_transform(shp_df, 'Lee', {
       'Precinct 1': 'JP01',
       'Precinct 2': 'JP02',
       'Precinct 3': 'JP03',
       'Precinct 4': 'JP04',
       'Precinct 5': 'JP05',
       'Precinct 6': 'JP06',
       'Precinct 7': 'JP07',
       'Precinct 8': 'JP08',
       'Precinct 9': 'JP09'},
       upper=False)

# lincoln county
c38 = ar_prec_transform(shp_df, 'Lincoln', {
       'Tarry': 'Bar/Tarry',
       'Yorktown': 'Bar/Yorktown',
       'Lone Pine / Garnett': 'Lone Pine/Garnett',
       'Lone Pine / Mt Home': 'Lone Pine/Mt. Home',
       'Owen / Glendale': 'Owen/Glendale',
       'Owen / Palmyra': 'Owen/Palmyra',
       'Wells Bayou': 'Wells Bayou/FS'}, # need to confirm
       chop_six_digs=True,
       upper=False)

# little river county
c39 = ar_prec_transform(shp_df, 'Little River', {
       'Arden Township': 'Arden',
       'Arkinda Township': 'Arkinda',
       'Burke Township': 'Burke',
       'Caney Township': 'Caney',
       'Cleveland Township': 'Cleveland',
       'Franklin Township': 'Franklin',
       'Jackson Township': 'Jackson',
       'Jefferson Township': 'Jefferson',
       'Jewell Township': 'Jewell',
       'Johnson Township': 'Johnson',
       'Lick Creek Township': 'Lick Creek',
       'Little River Township': 'Little River',
       'Red River Township': 'Red River',
       'Wallace / Richland': 'Wallace/Richland'})

# logan river
c40 = ar_prec_transform(shp_df, 'Logan', {
       'Sht Mtn WD 1': 'Short Mtn Ward 1',
       'Sht Mtn WD 2': 'Short Mtn Ward 2',
       'Sht Mtn WD 3': 'Short Mtn Ward 3',
       'Sht Mtn WD 4': 'Short Mtn Ward 4',
       'Blue Mountain City': 'Blue Mtn City',
       'Blue Mountain Rural': 'Blue Mtn Rural',
       'Boone WD 1': 'Boone Ward 1',
       'Boone WD 2': 'Boone Ward 2',
       'Boone WD 3': 'Boone Ward 3',
       'Boone WD 4': 'Boone Ward 4'},
       chop_six_digs=True,
       upper=False)

# lonoke river
c41 = ar_prec_transform(shp_df, 'Lonoke', {
       '05 - Cabot City Ward 1': '05 - Cabot City W/1',
       '06 - Cabot City Ward 2': '06 - Cabot City W/2',
       '07 - Cabot City Ward 3': '07 - Cabot City W/3',
       '08 - Cabot City Ward 4': '08 - Cabot City W/4',
       '13 - Carlisle TWP': '13 - Carlisle Twp.',
       '34 - Lonoke City Ward 1': '34 - Lonoke City W/1',
       '35 - Lonoke City Ward 2': '35 - Lonoke City W/2',
       '36 - Lonoke City Ward 3': '36 - Lonoke City W/3',
       '37 - Lonoke City Ward 4': '37 - Lonoke City W/4',
       '42 - Prairie TWP': '42 - Prairie Twp.',
       '45 - Totten TWP': '45 - Totten Twp.',
       '46 - Walls TWP': '46 - Walls Twp.',
       '47 - Ward City Ward 1': '47 - Ward City W/1',
       '48 - Ward City Ward 2': '48 - Ward City W/2',
       '49 - Ward City Ward 3': '49 - Ward City W/3',
       '51 - Williams TWP': '51 - Williams Twp.',
       '53 - Lonoke City Ward 5': '53 - Lonoke City W/5',
       '54 - Lonoke City Ward 6': '54 - Lonoke City W/6',
       '55 - Lonoke City Ward 7': '55 - Lonoke City W/7',
       '55 - Lonoke City Ward 8': '55 - Lonoke City W/8'},
       upper=False)

# madison
# need to come back to this, very few matches
c42 = ar_prec_transform(shp_df, 'Madison', upper=False)

# marion
c43 = ar_prec_transform(shp_df, 'Marion', upper=False, marion_transform=True)

# miller
c44 = ar_prec_transform(shp_df, 'Miller', {
       'Hickory St': 'Hickory Street',
       'Hickory St South': 'Hickory Street South',
       'Ozan Inghram': 'Ozan'},
       upper=False)

# mississippi 
# need to return, no matches
c45 = ar_prec_transform(shp_df, 'Mississippi')

# monroe 
# need to return gotta come back to it
c46 = ar_prec_transform(shp_df, 'Monroe',
       chop_five_digs=True)

# montgomery 
c47 = ar_prec_transform(shp_df, 'Montgomery', {
       'MOUNT IDA - IN': 'Mount Ida - Inside',
       'MOUNT IDA - OUT': 'Mount Ida - Outside',
       'NORMAN - IN': 'Norman - Inside',
       'NORMAN - OUT': 'Norman - Outside',
       'ODEN - IN': 'Oden - Inside',
       'ODEN - OUT': 'Oden - Outside'},
       chop_five_digs=True,
       upper=False)

# nevada
# return
c48 = ar_prec_transform(shp_df, 'Nevada', upper=False)

# newton 
c49 = ar_prec_transform(shp_df, 'Newton', {
       'Mt Sherman': 'Mt. Sherman'},
       upper=False)

# ouachita
# return - almost no matches here
c50 = ar_prec_transform(shp_df, 'Ouachita', )

# perry
c51 = ar_prec_transform(shp_df, 'Perry', perry_transform=True)

# phillips
# return
c52 = ar_prec_transform(shp_df, 'Phillips', )

# pike
c53 = ar_prec_transform(shp_df, 'Pike', chop_five_digs=True)

# poinsett
# return
c54 = ar_prec_transform(shp_df, 'Poinsett', )

# polk
# confirmed with county clerk 12/16/19
c55 = ar_prec_transform(shp_df, 'Polk', {
       '09 - DALLAS VALLEY/ SHADY': '09 - Dallas Valley', 
       '01- MENA': '01 - Precinct 1',
       '02- MENA': '02 - Precinct 2',
       '03- MENA': '03 - Precinct 3'})
c55 = ar_prec_transform(c55, 'Polk', chop_five_digs=True)

# pope 
# need to come back to this and fix the code! started the pope_transform, finish soon
c56 = ar_prec_transform(shp_df, 'Pope', chop_five_digs=True, pope_transform=True)

# prairie
c57 = ar_prec_transform(shp_df, 'Prairie', {
       'Belcher / Tyler': 'Belcher/Tyler',
       'White River Ward 1': 'Wattensaw City Ward 1',
       'White River Ward 2': 'Wattensaw City Ward 2',
       'White River Ward 3': 'Wattensaw City Ward 3'})

# pulaski
c58 = ar_prec_transform(shp_df, 'Pulaski', pulaski_transform=True, upper=False)

# randolph
c58 = ar_prec_transform(shp_df, 'Randolph', {
       'Okean': "O'kean",
       'Ward One': 'Ward 1',
       'Ward Two': 'Ward 2',
       'Ward Three': 'Ward 3'},
       chop_five_digs=True)

# saline
c59 = ar_prec_transform(shp_df, 'Saline', saline_transform=True)

# scott
c60 = ar_prec_transform(shp_df, 'Scott', {
       'Lewis 1': 'Lewis Ward 1',
       'Lewis 2': 'Lewis Ward 2',
       'Lewis 3': 'Lewis Ward 3'},
       chop_five_digs=True)

# searcy
c61 = ar_prec_transform(shp_df, 'Searcy')

# sebastian
c62 = ar_prec_transform(shp_df, 'Sebastian', sebastian_transform=True)

# sevier 
c63 = ar_prec_transform(shp_df, 'Sevier')

# sharp
c64 = ar_prec_transform(shp_df, 'Sharp')

# st francis
# return to it
c65 = ar_prec_transform(shp_df, 'St. Francis', {

})

# stone
c66 = ar_prec_transform(shp_df, 'Stone', {
       'Angora Mtn': 'Angora Mountain',
       'Dodd Mtn': 'Dodd Mountain'})

# union
c67 = ar_prec_transform(shp_df, 'Union', )

# van buren 
c68 = ar_prec_transform(shp_df, 'Van Buren')

# washington 
#return. need to change the elections to rm the first 4 characters in every cell
c69 = ar_prec_transform(shp_df, 'Washington', {
       'Prairie Gr City - House': 'Prairie Gr City-House',
       'Prairie Gr City - Senate': 'Prairie Gr City-Senate',
       'Richland - Senate': 'Richland-Senate'})

# white
c70 = ar_prec_transform(shp_df, 'White', chop_five_digs=True)

# woodruff 
# return with answers. eventually, remove spaces at -3 and -5
c71 = ar_prec_transform(shp_df, 'Woodruff', {
       'Augusta - 01': 'Augusta Armory -01',
       'Augusta - 02': 'Augusta Armory -02',
       'Augusta - 03': 'Augusta Armory -03',
       'Cotton Plant - 08': 'Babbs/Cotton Plant-08',
       'Cotton Plant - 09': 'Babbs/Cotton Plant-09',
       'Cotton Plant/ Freeman - 07': 'Babbs Cottn PL/Freeman-07',
       'Fakes Chapel - 20': 'Fairgrounds Fakes Chpl-20',
       'Gregory - 06': 'Gregory-06',
       'Hilleman - 13': 'White Hall Church-13',
       'Howell - 12': 'Fairgrounds/Howell-12',
       'Hunter - 11': 'Hunter Methodist-11',
       'McCrory - 17': 'McCrory Civic Center-17',
       'McCrory - 18': 'McCrory Civic-18',
       'McCrory Rural - 15': '',
       'Morton - 14': 'Frgrnds/McCrory Rural-15',
       'North Rural Augusta - 04': 'Augusta Armory-04',
       'Patterson - 16': 'Patterson Fire Station-16',
       'Pumkin Bend - 19': 'Pumpkin Bend Church-19',
       'Rural Hunter - 10': 'Hunter Methodist/Rural-10',
       'South Rural Augusta - 05': 'Augusta Armory-05'})

# yell
c72 = ar_prec_transform(shp_df, 'Yell', chop_five_digs=True)







elec_df = pd.read_csv(elec_path)
elec_df['NAME'] = elec_df['NAME'].str.strip()
elec_df = elec_df[['NAME', 'precinct', 'G18DGOV', 'G18RGOV', 'G18LGOV',
       'G18DHOR', 'G18RHOR', 'G18DStSEN', 'G18RStSEN', 'G18DStHou',
       'G18RStHou', 'G18LStHou', 'G16DPRS', 'G16RPRS', 'G16LPRS', 'G16GPRS',
       'G16CPRS', 'G16NPPRS', 'G16NAPRS', 'G16DSEN', 'G16RSEN', 'G16LSEN',
       'G16NASEN', 'G16NPSEN', 'G16DHOR', 'G16RHOR', 'G16LHOR', 'G16NAHOR',
       'G16NPHOR', 'G16DStHou', 'G16RStHou', 'G16CStHou', 'G16IStHou',
       'G16NAStHou', 'G16NPStHou', 'G14RGOV', 'G14CGOV', 'G14LGOV', 'G14NAGOV',
       'G14NPGOV', 'G14DSEN', 'G14RSEN', 'G14LSEN', 'G14NASEN', 'G14NPSEN',
       'G14DHOR', 'G14RHOR', 'G14LHOR', 'G14NPHOR', 'G14DStSEN', 'G14RStSEN',
       'G14NAStSEN', 'G14NPStSEN', 'G14DStHou', 'G14RStHou', 'G14CStHou',
       'G14LStHou', 'G14NAStHou', 'G14NPStHou']]

merged = pd.merge(shp_df, elec_df, on='NAME', how = 'outer')


merged.to_file('/Volumes/GoogleDrive/Shared drives/princeton_gerrymandering_project/OpenPrecincts/States for site/Alaska/Final/AK_Prec_G14_16_18.shp')
#merged.to_csv('/Volumes/GoogleDrive/Shared drives/princeton_gerrymandering_project/OpenPrecincts/States for site/Alaska/Final/AK_Prec_G14_16_18_test.csv')

for i in shp_df:
   geom = shp_df['geometry']
   if geom.geom_type=='MultiPolygon':
      print(geom)
