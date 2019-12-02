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

# function to clean
def ar_prec_transform(dat, county, custom_transformation = None, upper = True, chop_five_digs = True):
       dat_out = dat.loc[dat['county_nam'] == county]
       dat_out['prec_new'] = dat_out['precinct'].copy()
       if chop_five_digs:
              dat_out['prec_new'] = dat_out['prec_new'].str.slice(start = 5)
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
       'STUTTGART 3': 'STUTTGART WARD 3'}
       )

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
       'WEST CROSSETT RURAL': 'WCR'}
       )

# baxter cnty
c3 = ar_prec_transform(shp_df, 'Baxter', upper=False, chop_five_digs=False)

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
       'Precinct 09': 'Precinct 9'}, upper=False, chop_five_digs=False, 
)

# boone cnty
# COME BACK after contacting county
# big mismatch in number of precincts (more in election results)
c5 = ar_prec_transform(shp_df, 'Boone', )

# bradley cnty
c6 = ar_prec_transform(shp_df, 'Bradley', {
       'Warren Ward 1': 'Ward 1',
       'Warren Ward 2': 'Ward 2',
       'Warren Ward 3': 'Ward 3'},  
       upper=False
)

# calhoun cnty 
# COME BACK & figure out the deal with watson addition in election results
c7 = ar_prec_transform(shp_df, 'Calhoun', upper=False, chop_five_digs=False)

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
       'SW & SE HICKORY': 'SW/SE HICKORY'}, 
       chop_five_digs=False)

# chicot cnty
# might need to chop another digit
c9 = ar_prec_transform(shp_df, 'Chicot', {
       'Carlton': 'Carlton 1'},
       upper=False)

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
       'Whelen Springs 1': 'Whelen Springs'},
       chop_five_digs=False)

# clay county
c11 = ar_prec_transform(shp_df, 'Clay', {
       'Bennett & Lemmons': 'Bennett and Lemmons',
       'E Oak Bluff & Blue Cane': 'East Oak Bluff & Blue Cane',
       'Liddell & chalk Bluff': 'Liddell & Chalk Bluff',
       'Cleveland & N Kilgore': 'N Kilgore & Cleveland',
       'North St Francis': 'North St. Francis',
       'Gleghorn & S Kilgore': 'S Kilgore & Gleghorn',
       'South St Francis': 'South St. Francis'},
       upper=False)

# cleburne county
# also transformed the elections data to remove last three numbers
c12 = ar_prec_transform(shp_df, 'Cleburne')

# cleveland county
c13 = ar_prec_transform(shp_df, 'Cleveland', upper=False)

# columbia county
c14 = ar_prec_transform(shp_df, 'Columbia', {
       'Taylor City': 'Taylor',
       'Waldo City': 'Waldo'},
       chop_five_digs=False)

# conway county
c15 = ar_prec_transform(shp_df, 'Conway', {
       'St Vincent': 'St. Vincent',
       'Lick Mountain': 'Lick Mtn.'})

# craighead
# took the "precinct" out of elections data
c16 = ar_prec_transform(shp_df, 'Craighead',
       chop_five_digs=False,
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
       chop_five_digs=False,
       upper=False)

# crittenden
# need to revisit. none of these names match up
c18 = ar_prec_transform(shp_df, 'Crittenden')

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
       chop_five_digs=False,
       upper=False)

# dallas
c20 = ar_prec_transform(shp_df, 'Dallas', upper=False)

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
       'Silver Lake': 'Silverlake'})

# drew cnty
c22 = ar_prec_transform(shp_df, 'Drew', {
       'Mar N Box 1': 'MN BOX 1 - RH Cumb. Presb', # need to confirm
       'Mar N Box 2': 'MN Box 2 - RH Baptist Chu', # need to confirm
       'Marion South': 'Marion South - Shady Grov'},
       upper=False)

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
       upper=False,
       chop_five_digs=False)

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
       upper=False,
       chop_five_digs=False)

#






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
