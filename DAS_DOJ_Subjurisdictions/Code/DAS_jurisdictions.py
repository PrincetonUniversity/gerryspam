
"""

DAS DOJ Jurisdictions Analysis: Part 1
6/3/21

Explore population deviations between DP 12.2 data and 2010 Census data
Applied to specified subjurisdictions in AZ, FL, CA, SD and TX
Take joined DP and 2010 data for each state, filter to subjurisdictions
Dissolve by district ID and write to file

"""

import pandas as pd
import geopandas as gpd
import numpy

#### SETUP

# import joined DP + 2010 data
az_data = pd.read_csv('D:/Census/Joined States/CSV/12.2/AZ_blocks_join_DP12_2.csv')
fl_data = pd.read_csv('D:/Census/Joined States/CSV/12.2/FL_blocks_join_DP12_2.csv')
ca_data = pd.read_csv('D:/Census/Joined States/CSV/12.2/CA_blocks_join_DP12_2.csv')
sd_data = pd.read_csv('D:/Census/Joined States/CSV/12.2/SD_blocks_join_DP12_2.csv')
tx_data = pd.read_csv('D:/Census/Joined States/CSV/12.2/TX_blocks_join_DP12_2.csv')

# fix geoid
fl_data['GEOID10'] = fl_data['GEOID10'].map(lambda x:str(x).zfill(15))
az_data['GEOID10'] = az_data['GEOID10'].map(lambda x:str(x).zfill(15))
ca_data['GEOID10'] = ca_data['GEOID10'].map(lambda x:str(x).zfill(15))
sd_data['GEOID10'] = sd_data['GEOID10'].map(lambda x:str(x).zfill(15))
tx_data['GEOID10'] = tx_data['GEOID10'].map(lambda x:str(x).zfill(15))


# original census block shapefiles
fl_shp = gpd.read_file('D:/GIS data/FL/Census/tl_2020_12_tabblock10/tl_2020_12_tabblock10.shp')
az_shp = gpd.read_file('D:/GIS data/AZ/Census/tl_2020_04_tabblock10/tl_2020_04_tabblock10.shp')
ca_shp = gpd.read_file('D:/GIS data/CA/Census/tl_2020_06_tabblock10/tl_2020_06_tabblock10.shp')
sd_shp = gpd.read_file('D:/GIS data/SD/Census/tl_2020_46_tabblock10/tl_2020_46_tabblock10.shp')
tx_shp = gpd.read_file('D:/GIS data/TX/Census/tl_2020_48_tabblock10/tl_2020_48_tabblock10.shp')

def checkDataFrame(df):
    ''' 
    take a data frame and find all columns with null values
    return all null columns
    '''

    df.isnull().values.any()
    null_columns=df.columns[df.isnull().any()]
    print("Null Columns: ", str(len(null_columns)))
    print(null_columns)
    return null_columns
    
def getSubset(fname, st_data, st_name, local_name):
    cur_file = pd.read_csv(fname, header=None)
    cur_file.rename(columns={0:'geoid', 1:'local_id'}, inplace=True) 
    cur_file['geoid'] = cur_file['geoid'].map(lambda x:str(x).zfill(15))
    joined_data = cur_file.merge(st_data, left_on='geoid', right_on='GEOID10', how='left')
    joined_data.set_index('geoid', inplace=True)
    
    checkDataFrame(joined_data)
    joined_data.to_csv('D:/Census/Localities/{0}/{0}_{1}_blocks.csv'.format(st_name, local_name)) # save block csv
    print('D:/Census/Localities/{0}/{0}_{1}.csv'.format(st_name, local_name))
    return joined_data

def createSHP(state_df, state_shp, st_name, local_name):
    joined_shp = state_shp.merge(state_df, left_on='GEOID10', right_on='GEOID10', how='right')
    joined_shp.to_file('D:/Census/Localities/{0}/{0}_{1}_blocks.shp'.format(st_name, local_name))
    print('D:/Census/Localities/{0}/{0}_{1}_blocks.shp'.format(st_name, local_name)) # save block shp
    block_cols = ['local_id', 'geometry'] + list(joined_shp.columns)[18:]
    joined_agg = joined_shp[block_cols]
    
    # dissolve by district
    dissolve_dists = joined_agg.dissolve(by='local_id', aggfunc="sum")
    dissolve_dists.to_file('D:/Census/Localities/{0}/{0}_{1}.shp'.format(st_name, local_name)) # save dissolved dist shp
    print('D:/Census/Localities/{0}/{0}_{1}.shp'.format(st_name, local_name))
    
    # csv only
    dissolve_df = pd.DataFrame(dissolve_dists.drop(columns='geometry')) 
    dissolve_df.to_csv('D:/Census/Localities/{0}/{0}_{1}.csv'.format(st_name, local_name)) # save dissolved dist csv
    print('D:/Census/Localities/{0}/{0}_{1}.csv'.format(st_name, local_name))
    checkDataFrame(dissolve_df)

####
#### AZ
####

# state setup
cur_data = az_data
cur_shp = az_shp
cur_name = 'AZ'

# AZ Apache Board of Supervisors  
filename =  'C:/Users/amand/Documents/PGP/DAS/Census_2010_Voting_2020/2011-4057_201.txt'
joined_df = getSubset(filename, cur_data, cur_name, 'Apache_BOS')
createSHP(joined_df, cur_shp, cur_name, 'Apache_BOS')


# AZ Gila Globe 
filename =  'C:/Users/amand/Documents/PGP/DAS/Census_2010_Voting_2020/2011-4802_201.txt'
joined_df = getSubset(filename, cur_data, cur_name, 'Gila_Globe')
createSHP(joined_df, cur_shp, cur_name, 'Gila_Globe')


# AZ Gila Commission
filename =  'C:/Users/amand/Documents/PGP/DAS/Census_2010_Voting_2020/2011-5000_201.txt'
joined_df = getSubset(filename, cur_data, cur_name, 'Gila_Comm')
createSHP(joined_df, cur_shp, cur_name, 'Gila_Comm')


# AZ Navajo Board of Supervisors
filename =  'C:/Users/amand/Documents/PGP/DAS/Census_2010_Voting_2020/2011-5445_201.txt'
joined_df = getSubset(filename, cur_data, cur_name, 'Navajo_BOS')
createSHP(joined_df, cur_shp, cur_name, 'Navajo_BOS')


# AZ Coconino Board of Supervisors
filename =  'C:/Users/amand/Documents/PGP/DAS/Census_2010_Voting_2020/2011-5485_201.txt'
joined_df = getSubset(filename, cur_data, cur_name, 'Coconino_BOS')
createSHP(joined_df, cur_shp, cur_name, 'Coconino_BOS')


# AZ Cochise Bisbee 
filename =  'C:/Users/amand/Documents/PGP/DAS/Census_2010_Voting_2020/2012-4234_201.txt'
joined_df = getSubset(filename, cur_data, cur_name, 'Cochise_Bisbee')
createSHP(joined_df, cur_shp, cur_name, 'Cochise_Bisbee')


####
#### FL
####

# state setup
cur_data = fl_data
cur_shp = fl_shp
cur_name = 'FL'


# FL Collier School Districts  2011-5300_201
filename =  'C:/Users/amand/Documents/PGP/DAS/Census_2010_Voting_2020/2011-5300_201.txt'
joined_df = getSubset(filename, cur_data, cur_name, 'Collier_SD')
createSHP(joined_df, cur_shp, cur_name, 'Collier_SD')


# FL Hendry Commission 2012-0840_201
filename =  'C:/Users/amand/Documents/PGP/DAS/Census_2010_Voting_2020/2012-0840_201.txt'
joined_df = getSubset(filename, cur_data, cur_name, 'Hendry_Comm')
createSHP(joined_df, cur_shp, cur_name, 'Hendry_Comm')


####
#### CA
####

# state setup
cur_data = ca_data
cur_shp = ca_shp
cur_name = 'CA'

# CA Merced Weaver SD 2011-5355_201
filename =  'C:/Users/amand/Documents/PGP/DAS/Census_2010_Voting_2020/2011-5355_201.txt'
joined_df = getSubset(filename, cur_data, cur_name, 'Merced_Weaver_SD')
createSHP(joined_df, cur_shp, cur_name, 'Merced_Weaver_SD')

# CA Kings Hanford Elem 2011-5444_201
filename =  'C:/Users/amand/Documents/PGP/DAS/Census_2010_Voting_2020/2011-5444_201.txt'
joined_df = getSubset(filename, cur_data, cur_name, 'Kings_Hanford_Elem')
createSHP(joined_df, cur_shp, cur_name, 'Kings_Hanford_Elem')

# CA Kings Riverdale SD 2012-0872_201
filename =  'C:/Users/amand/Documents/PGP/DAS/Census_2010_Voting_2020/2012-0872_201.txt'
joined_df = getSubset(filename, cur_data, cur_name, 'Kings_Riverdale_SD')
createSHP(joined_df, cur_shp, cur_name, 'Kings_Riverdale_SD')

####
#### SD
####

# state setup
cur_data = sd_data
cur_shp = sd_shp
cur_name = 'SD'

# SD Shannon County Commission 2012-0675_201
filename =  'C:/Users/amand/Documents/PGP/DAS/Census_2010_Voting_2020/2012-0675_201.txt'
joined_df = getSubset(filename, cur_data, cur_name, 'Shannon_Comm')
createSHP(joined_df, cur_shp, cur_name, 'Shannon_Comm')

# SD Todd County Commission 2012-0868_201
filename =  'C:/Users/amand/Documents/PGP/DAS/Census_2010_Voting_2020/2012-0868_201.txt'
joined_df = getSubset(filename, cur_data, cur_name, 'Todd_Comm')
createSHP(joined_df, cur_shp, cur_name, 'Todd_Comm')

# SD Charles Mix County Commission 2012-1584_201
filename =  'C:/Users/amand/Documents/PGP/DAS/Census_2010_Voting_2020/2012-1584_201.txt'
joined_df = getSubset(filename, cur_data, cur_name, 'Charles_Mix_Comm')
createSHP(joined_df, cur_shp, cur_name, 'Charles_Mix_Comm')


####
#### TX
####

# state setup
cur_data = tx_data
cur_shp = tx_shp
cur_name = 'TX'


# TX	FORT BEND, HARRIS	HOUSTON COMM. COLL.DIST.  
filename =  'C:/Users/amand/Documents/PGP/DAS/Census_2010_Voting_2020/2011-2483_201.txt'
joined_df = getSubset(filename, cur_data, cur_name, 'FtBend_Harris_Houston_Comm_Coll_Dist')
createSHP(joined_df, cur_shp, cur_name, 'FtBend_Harris_Houston_Comm_Coll_Dist')

# TX	KARNES	COMM. COURT
filename =  'C:/Users/amand/Documents/PGP/DAS/Census_2010_Voting_2020/2011-2630_201.txt'
joined_df = getSubset(filename, cur_data, cur_name, 'Karnes_Comm_Court')
createSHP(joined_df, cur_shp, cur_name, 'Karnes_Comm_Court')

# TX	OCHILTREE	COMM. COURT
filename =  'C:/Users/amand/Documents/PGP/DAS/Census_2010_Voting_2020/2011-2970_201.txt'
joined_df = getSubset(filename, cur_data, cur_name, 'Ochiltree_Comm_Court')
createSHP(joined_df, cur_shp, cur_name, 'Ochiltree_Comm_Court')

# TX	HARRIS	COMM. COURT
filename =  'C:/Users/amand/Documents/PGP/DAS/Census_2010_Voting_2020/2011-3066_201.txt'
joined_df = getSubset(filename, cur_data, cur_name, 'Harris_Comm_Court')
createSHP(joined_df, cur_shp, cur_name, 'Harris_Comm_Court')

# TX	MCCLENNAN	WACO ISD
filename =  'C:/Users/amand/Documents/PGP/DAS/Census_2010_Voting_2020/2011-3184_201.txt'
joined_df = getSubset(filename, cur_data, cur_name, 'McClennan_Waco_ISD')
createSHP(joined_df, cur_shp, cur_name, 'McClennan_Waco_ISD')

# TX	CALDWELL	COMM.CT/JP
filename =  'C:/Users/amand/Documents/PGP/DAS/Census_2010_Voting_2020/2011-3592_201.txt'
joined_df = getSubset(filename, cur_data, cur_name, 'Caldwell_Comm_CT_JP')
createSHP(joined_df, cur_shp, cur_name, 'Caldwell_Comm_CT_JP')

# TX	BEXAR	SAN ANTONIO ISD
filename =  'C:/Users/amand/Documents/PGP/DAS/Census_2010_Voting_2020/2011-3645_201.txt'
joined_df = getSubset(filename, cur_data, cur_name, 'Bexar_San_Antonio_ISD')
createSHP(joined_df, cur_shp, cur_name, 'Bexar_San_Antonio_ISD')

# TX	BEXAR	COMM.CT
filename =  'C:/Users/amand/Documents/PGP/DAS/Census_2010_Voting_2020/2011-3698_201.txt'
joined_df = getSubset(filename, cur_data, cur_name, 'Bexar_Comm_CT')
createSHP(joined_df, cur_shp, cur_name, 'Bexar_Comm_CT')

# TX	CROSBY	RALLS ISD
filename =  'C:/Users/amand/Documents/PGP/DAS/Census_2010_Voting_2020/2011-3775_201.txt'
joined_df = getSubset(filename, cur_data, cur_name, 'Crosby_Ralls_ISD')
createSHP(joined_df, cur_shp, cur_name, 'Crosby_Ralls_ISD')

# TX	HALE	PLAINVIEW ISD
filename =  'C:/Users/amand/Documents/PGP/DAS/Census_2010_Voting_2020/2011-3868_201.txt'
joined_df = getSubset(filename, cur_data, cur_name, 'Hale_Plainview_ISD')
createSHP(joined_df, cur_shp, cur_name, 'Hale_Plainview_ISD')

# TX	CASTRO	DIMMITT
filename =  'C:/Users/amand/Documents/PGP/DAS/Census_2010_Voting_2020/2011-3987_201.txt'
joined_df = getSubset(filename, cur_data, cur_name, 'Castro_Dimmitt')
createSHP(joined_df, cur_shp, cur_name, 'Castro_Dimmitt')

# TX	REAGAN	HOSPITAL DISTRICT
filename =  'C:/Users/amand/Documents/PGP/DAS/Census_2010_Voting_2020/2011-3989_201.txt'
joined_df = getSubset(filename, cur_data, cur_name, 'Reagan_Hospital_Dist')
createSHP(joined_df, cur_shp, cur_name, 'Reagan_Hospital_Dist')

# TX	BREWSTER	COMM.CT/CONS/JP
filename =  'C:/Users/amand/Documents/PGP/DAS/Census_2010_Voting_2020/2011-4193_202.txt'
joined_df = getSubset(filename, cur_data, cur_name, 'Brewster_Comm_CT_CONS_JP')
createSHP(joined_df, cur_shp, cur_name, 'Brewster_Comm_CT_CONS_JP')

# TX	GALVESTON	COMM.CT
filename =  'C:/Users/amand/Documents/PGP/DAS/Census_2010_Voting_2020/2011-4317_205.txt'
joined_df = getSubset(filename, cur_data, cur_name, 'Galveston_Comm_CT')
createSHP(joined_df, cur_shp, cur_name, 'Galveston_Comm_CT')

# TX	GALVESTON	CONS/JP
filename = 'C:/Users/amand/Documents/PGP/DAS/Census_2010_Voting_2020/2011-4374_202.txt'
joined_df = getSubset(filename, cur_data, cur_name, 'Galveston_CONS_JP')
createSHP(joined_df, cur_shp, cur_name, 'Galveston_CONS_JP')

# TX	HALE	COMM.CT/CON/JP
filename =  'C:/Users/amand/Documents/PGP/DAS/Census_2010_Voting_2020/2011-4444_202.txt'
joined_df = getSubset(filename, cur_data, cur_name, 'Hale_Comm_CT_CON_JP')
createSHP(joined_df, cur_shp, cur_name, 'Hale_Comm_CT_CON_JP')

# TX	TRAVIS	AUSTIN ISD 
filename =  'C:/Users/amand/Documents/PGP/DAS/Census_2010_Voting_2020/2011-4448_201.txt'
joined_df = getSubset(filename, cur_data, cur_name, 'Travis_Austin_ISD')
createSHP(joined_df, cur_shp, cur_name, 'Travis_Austin_ISD')

# TX	ECTOR	COMM.CT/CONS/JP 
filename =  'C:/Users/amand/Documents/PGP/DAS/Census_2010_Voting_2020/2011-4506_201.txt'
joined_df = getSubset(filename, cur_data, cur_name, 'Ector_Comm_CT_CONS_JP')
createSHP(joined_df, cur_shp, cur_name, 'Ector_Comm_CT_CONS_JP')

# TX	DAWSON	COMM.CT/CONS/JP
filename =  'C:/Users/amand/Documents/PGP/DAS/Census_2010_Voting_2020/2011-4528_201.txt'
joined_df = getSubset(filename, cur_data, cur_name, 'Dawson_Comm_CT_CONS_JP')
createSHP(joined_df, cur_shp, cur_name, 'Dawson_Comm_CT_CONS_JP')

# TX	HOCKLEY	COMM.CT/CONS/JP
filename =  'C:/Users/amand/Documents/PGP/DAS/Census_2010_Voting_2020/2011-4553_202.txt'
joined_df = getSubset(filename, cur_data, cur_name, 'Hockley_Comm_CT_CONS_JP')
createSHP(joined_df, cur_shp, cur_name, 'Hockley_Comm_CT_CONS_JP')

# TX	COLLIN	MCKINNEY ISD
filename =  'C:/Users/amand/Documents/PGP/DAS/Census_2010_Voting_2020/2011-4580_201.txt'
joined_df = getSubset(filename, cur_data, cur_name, 'Collin_McKinney_ISD')
createSHP(joined_df, cur_shp, cur_name, 'Collin_McKinney_ISD')

# TX	TERRY	COMM.CT/CONS/JP
filename =  'C:/Users/amand/Documents/PGP/DAS/Census_2010_Voting_2020/2011-4761_201.txt'
joined_df = getSubset(filename, cur_data, cur_name, 'Terry_Comm_CT_CONS_JP')
createSHP(joined_df, cur_shp, cur_name, 'Terry_Comm_CT_CONS_JP')

# TX	UPTON	COMM.CT/CONS/JP
filename =  'C:/Users/amand/Documents/PGP/DAS/Census_2010_Voting_2020/2011-4792_201.txt'
joined_df = getSubset(filename, cur_data, cur_name, 'Upton_Comm_CT_CONS_JP')
createSHP(joined_df, cur_shp, cur_name, 'Upton_Comm_CT_CONS_JP')

# TX	HAYS	KYLE
filename =  'C:/Users/amand/Documents/PGP/DAS/Census_2010_Voting_2020/2011-4805_201.txt'
joined_df = getSubset(filename, cur_data, cur_name, 'Hays_Kyle')
createSHP(joined_df, cur_shp, cur_name, 'Hays_Kyle')

# TX	BRAZORIA	ALVIN
filename =  'C:/Users/amand/Documents/PGP/DAS/Census_2010_Voting_2020/2011-4880_201.txt'
joined_df = getSubset(filename, cur_data, cur_name, 'Brazoria_Alvin')
createSHP(joined_df, cur_shp, cur_name, 'Brazoria_Alvin')


# TX	TITUS	COMM.CT/CONS/JP
filename =  'C:/Users/amand/Documents/PGP/DAS/Census_2010_Voting_2020/2011-4883_202.txt'
joined_df = getSubset(filename, cur_data, cur_name, 'Titus_Comm_CT_CONS_JP')
createSHP(joined_df, cur_shp, cur_name, 'Titus_Comm_CT_CONS_JP')

# TX	MOORE	COMM.CT/CONS/JP
filename =  'C:/Users/amand/Documents/PGP/DAS/Census_2010_Voting_2020/2011-4891_201.txt'
joined_df = getSubset(filename, cur_data, cur_name, 'Moore_Comm_CT_CONS_JP')
createSHP(joined_df, cur_shp, cur_name, 'Moore_Comm_CT_CONS_JP')

# TX	GAINES	COMM.CT/CONS/JP
filename =  'C:/Users/amand/Documents/PGP/DAS/Census_2010_Voting_2020/2011-4933_201.txt'
joined_df = getSubset(filename, cur_data, cur_name, 'Gaines_Comm_CT_CONS_JP')
createSHP(joined_df, cur_shp, cur_name, 'Gaines_Comm_CT_CONS_JP')

# TX	NOLAN	SWEETWATER
filename =  'C:/Users/amand/Documents/PGP/DAS/Census_2010_Voting_2020/2011-5015_201.txt'
joined_df = getSubset(filename, cur_data, cur_name, 'Nolan_Sweetwater')
createSHP(joined_df, cur_shp, cur_name, 'Nolan_Sweetwater')

# TX	KLEBERG	COMM.CT
filename =  'C:/Users/amand/Documents/PGP/DAS/Census_2010_Voting_2020/2011-5104_201.txt'
joined_df = getSubset(filename, cur_data, cur_name, 'Kleberg_Comm_CT')
createSHP(joined_df, cur_shp, cur_name, 'Kleberg_Comm_CT')

# TX	HOWARD	COMM.CT/CONS/JP 
filename =  'C:/Users/amand/Documents/PGP/DAS/Census_2010_Voting_2020/2011-5111_202.txt'
joined_df = getSubset(filename, cur_data, cur_name, 'Howard_Comm_CT_CONS_JP')
createSHP(joined_df, cur_shp, cur_name, 'Howard_Comm_CT_CONS_JP')

# TX	WHARTON	WHARTON
filename =  'C:/Users/amand/Documents/PGP/DAS/Census_2010_Voting_2020/2011-5211_201.txt'
joined_df = getSubset(filename, cur_data, cur_name, 'Wharton_Wharton')
createSHP(joined_df, cur_shp, cur_name, 'Wharton_Wharton')

# TX	MORRIS, TITUS	DAINGERFIELD-LONE STAR ISD
filename =  'C:/Users/amand/Documents/PGP/DAS/Census_2010_Voting_2020/2011-5235_201.txt'
joined_df = getSubset(filename, cur_data, cur_name, 'Morris_Titus_Lone_Star_ISD')
createSHP(joined_df, cur_shp, cur_name, 'Morris_Titus_Lone_Star_ISD')

# TX	CONCHO	COMM.CT/CONS/JP
filename =  'C:/Users/amand/Documents/PGP/DAS/Census_2010_Voting_2020/2011-5236_201.txt'
joined_df = getSubset(filename, cur_data, cur_name, 'Concho_Comm_CT_CONS_JP')
createSHP(joined_df, cur_shp, cur_name, 'Concho_Comm_CT_CONS_JP')

#TX	CALDWELL, HAYS, TRAVIS	HAYS ISD
filename =  'C:/Users/amand/Documents/PGP/DAS/Census_2010_Voting_2020/2011-5379_201.txt'
joined_df = getSubset(filename, cur_data, cur_name, 'Caldwell_Hayes_Travis_Hays_ISD')
createSHP(joined_df, cur_shp, cur_name, 'Caldwell_Hayes_Travis_Hays_ISD')

# TX	ATASCOSA, KARNES	KARNES CITY ISD
filename =  'C:/Users/amand/Documents/PGP/DAS/Census_2010_Voting_2020/2012-0012_201.txt'
joined_df = getSubset(filename, cur_data, cur_name, 'Atascosa_Karnes_City_ISD')
createSHP(joined_df, cur_shp, cur_name, 'Atascosa_Karnes_City_ISD')

# TX	BEXAR, WILSON	FLORESVILLE ISD
filename =  'C:/Users/amand/Documents/PGP/DAS/Census_2010_Voting_2020/2012-0102_201.txt'
joined_df = getSubset(filename, cur_data, cur_name, 'Bexar_Wilson_Floresville_ISD')
createSHP(joined_df, cur_shp, cur_name, 'Bexar_Wilson_Floresville_ISD')

# TX	BEXAR	JUDSON ISD
filename =  'C:/Users/amand/Documents/PGP/DAS/Census_2010_Voting_2020/2012-0188_201.txt'
joined_df = getSubset(filename, cur_data, cur_name, 'Bexar_Judson_ISD')
createSHP(joined_df, cur_shp, cur_name, 'Bexar_Judson_ISD')

# TX	GUADALUPE	GROUNDWATER DIST
filename =  'C:/Users/amand/Documents/PGP/DAS/Census_2010_Voting_2020/2012-0421_201.txt'
joined_df = getSubset(filename, cur_data, cur_name, 'Guadalupe_Groundwater_Dist')
createSHP(joined_df, cur_shp, cur_name, 'Guadalupe_Groundwater_Dist')

# TX	ARANSAS, KLEBERG, NUECES, SAN PATRICIO	CORPUS CHRISTI
filename =  'C:/Users/amand/Documents/PGP/DAS/Census_2010_Voting_2020/2012-0732_201.txt'
joined_df = getSubset(filename, cur_data, cur_name, 'Ark_Kle_Nue_SanPat_Corpus_Christi')
createSHP(joined_df, cur_shp, cur_name, 'Ark_Kle_Nue_SanPat_Corpus_Christi')

# TX	SWISHER	TULIA
filename =  'C:/Users/amand/Documents/PGP/DAS/Census_2010_Voting_2020/2012-0743_201.txt'
joined_df = getSubset(filename, cur_data, cur_name, 'Swisher_Tulia')
createSHP(joined_df, cur_shp, cur_name, 'Swisher_Tulia')

# TX	STERLING	STERLING ISD
filename =  'C:/Users/amand/Documents/PGP/DAS/Census_2010_Voting_2020/2012-0869_201.txt'
joined_df = getSubset(filename, cur_data, cur_name, 'Sterling_Sterling_ISD')
createSHP(joined_df, cur_shp, cur_name, 'Sterling_Sterling_ISD')

# TX	DICKENS	SPUR
filename =  'C:/Users/amand/Documents/PGP/DAS/Census_2010_Voting_2020/2012-1182_201.txt'
joined_df = getSubset(filename, cur_data, cur_name, 'Dickens_Spur')
createSHP(joined_df, cur_shp, cur_name, 'Dickens_Spur')

# TX	CALDWELL	LULING
filename =  'C:/Users/amand/Documents/PGP/DAS/Census_2010_Voting_2020/2012-1242_201.txt'
joined_df = getSubset(filename, cur_data, cur_name, 'Caldwell_Luling')
createSHP(joined_df, cur_shp, cur_name, 'Caldwell_Luling')

# TX	CALDWELL	LOCKHART ISD
filename =  'C:/Users/amand/Documents/PGP/DAS/Census_2010_Voting_2020/2012-1249_201.txt'
joined_df = getSubset(filename, cur_data, cur_name, 'Caldwell_Lockhart_ISD')
createSHP(joined_df, cur_shp, cur_name, 'Caldwell_Lockhart_ISD')

# TX	ATASCOSA, BEXAR, MEDINA	LYTLE
filename =  'C:/Users/amand/Documents/PGP/DAS/Census_2010_Voting_2020/2012-1639_201.txt'
joined_df = getSubset(filename, cur_data, cur_name, 'Atascosa_Bexar_Medina_Lytle')
createSHP(joined_df, cur_shp, cur_name, 'Atascosa_Bexar_Medina_Lytle')

# TX	SUTTON	SONORA ISD
filename =  'C:/Users/amand/Documents/PGP/DAS/Census_2010_Voting_2020/2012-3559_201.txt'
joined_df = getSubset(filename, cur_data, cur_name, 'Sutton_Sonora_ISD')
createSHP(joined_df, cur_shp, cur_name, 'Sutton_Sonora_ISD')

# TX	VICTORIA	GROUNDWATER DIST
filename =  'C:/Users/amand/Documents/PGP/DAS/Census_2010_Voting_2020/2012-4835_201.txt'
joined_df = getSubset(filename, cur_data, cur_name, 'Victoria_Groundwater_Dist')
createSHP(joined_df, cur_shp, cur_name, 'Victoria_Groundwater_Dist')

# TX	BEXAR	SAN ANTONIO
filename =  'C:/Users/amand/Documents/PGP/DAS/Census_2010_Voting_2020/2012-5300_201.txt'
joined_df = getSubset(filename, cur_data, cur_name, 'Bexar_San_Antonio')
createSHP(joined_df, cur_shp, cur_name, 'Bexar_San_Antonio')












