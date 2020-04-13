import geopandas as gpd
import pandas as pd
import numpy as np

#list states you need data for
states = ['Michigan']

#filepath to country wide 2018 precinct level returns
elec_fp = '/Volumes/GoogleDrive/Shared drives/princeton_gerrymandering_project/OpenPrecincts/States for site/Michigan/Raw Elections/MISOSprec.csv'
#load into dataframe
elec_df = pd.read_csv(elec_fp)#, encoding = "ISO-8859-1")
elec_df = elec_df.fillna(0)
elec_df['loc_prec'] = elec_df.county_name.map(str) + ',' + elec_df.city_name.map(str) + ',' + elec_df.CityTown.map(str) + ',' + elec_df.prec_num.map(str) + '-' + elec_df.prec_label.map(str) + ',' + elec_df.ward_num.map(str)


statewide_offices = []
parties = elec_df.cand_party.unique()
#get state-level dataset
for state in states:
    state_df = elec_df
    #state_df.precinct = state_df.county_name.map(str) + ',' + state_df.precinct.map(str)
    #make list of office titles
    offices_tot = state_df['office_name'].unique()
    counties_tot = state_df['county_name'].unique()
    state_offices = []
    counties_office = {}
    #loop through offices and find statewide ones
    for office in offices_tot:
        counties  = []
        counties.append(state_df.loc[state_df['office_name'] == office, 'county_name'])
        #list of counties that had an election for that office
        counties_office[office] = counties
        c = counties_office[office][0].values
        D = {I: True for I in c}
        count = D.keys()
        if len(count) ==  len(counties_tot):
            state_offices.append(office)
    state_elec = state_df.loc[state_df['office_name'].isin(state_offices)]
    statewide_offices.append(state_offices)
#get table of elections by precinct
prec_elec = pd.pivot_table(state_elec, index = ['loc_prec'], columns = ['cand_party','office_name'], values = ['prec_votes'], aggfunc = np.sum)

prec_elec.columns = prec_elec.columns.to_series().str.join(' ')

columns = prec_elec.columns.values
print(columns)

# =============================================================================
# def rename_vote_cols(columns):
#     ''' function to take long name after processing election data and put into 
#     10 char. string'''
#     for vote_col in columns:
#         rn_col = vote_col.replace('votes ','')
# 
# =============================================================================

#rename columns
prec_elec_rn = prec_elec.rename(columns = {
        'prec_votes DEM ATTORNEY GENERAL ' : 'G18DATG',
        'prec_votes DEM GOVERNOR' : 'G18DGOV',
        'prec_votes DEM MEMBER OF THE STATE BOARD OF EDUCATION' : 'G18DBoE',
        'prec_votes DEM REPRESENTATIVE IN CONGRESS' : 'G18DHOR',
        'prec_votes DEM REPRESENTATIVE IN STATE LEGISLATURE' : 'G18DStHou',
        'prec_votes DEM SECRETARY OF STATE'  : 'G18DSOS',
        'prec_votes DEM STATE SENATOR' : 'G18DStSen',
        'prec_votes DEM UNITED STATES SENATOR'  : 'G18DSEN',
        'prec_votes REP ATTORNEY GENERAL '  : 'G18RATG',
        'prec_votes REP GOVERNOR'  : 'G18RGOV',
        'prec_votes REP MEMBER OF THE STATE BOARD OF EDUCATION'  : 'G18RBoE',
        'prec_votes REP REPRESENTATIVE IN CONGRESS'  : 'G18RHOR',
        'prec_votes REP REPRESENTATIVE IN STATE LEGISLATURE'  : 'G18RStHou',
        'prec_votes REP SECRETARY OF STATE'   : 'G18RSOS',
        'prec_votes REP STATE SENATOR'  : 'G18RStSen',
        'prec_votes REP UNITED STATES SENATOR'   : 'G18RSEN',
        'prec_votes GRN GOVERNOR' : 'G18GGOV',
        'prec_votes GRN MEMBER OF THE STATE BOARD OF EDUCATION' : 'G18GBoE',
        'prec_votes GRN REPRESENTATIVE IN CONGRESS' : 'G18GHOR',
        'prec_votes GRN REPRESENTATIVE IN STATE LEGISLATURE' : 'G18GStHou',
        'prec_votes GRN STATE SENATOR' : 'G18GStSen',
        'prec_votes GRN UNITED STATES SENATOR'  : 'G18GSEN',
        'prec_votes LIB ATTORNEY GENERAL ' : 'G18LATG',
        'prec_votes LIB GOVERNOR' : 'G18LGOV',
        'prec_votes LIB MEMBER OF THE STATE BOARD OF EDUCATION' : 'G18LBoE',
        'prec_votes LIB REPRESENTATIVE IN CONGRESS' : 'G18LHOR',
        'prec_votes LIB REPRESENTATIVE IN STATE LEGISLATURE' : 'G18LStHou',
        'prec_votes LIB SECRETARY OF STATE'  : 'G18LSOS',
        'prec_votes LIB STATE SENATOR' : 'G18LStSen',
        'prec_votes NPA ATTORNEY GENERAL ' : 'G18NPATG',
        'prec_votes NPA GOVERNOR'  : 'G18NPGOV',
        'prec_votes NPA REPRESENTATIVE IN CONGRESS' : 'G18NPHOR',
        'prec_votes NPA REPRESENTATIVE IN STATE LEGISLATURE' : 'G18NPStHou',
        'prec_votes NPA STATE SENATOR' : 'G18NPStSen',
        'prec_votes NPA UNITED STATES SENATOR'  : 'G18NPSEN',
        'prec_votes UST ATTORNEY GENERAL ' : 'G18OATG',
        'prec_votes UST GOVERNOR' : 'G18OGOV1',
        'prec_votes UST MEMBER OF THE STATE BOARD OF EDUCATION' : 'G18OBoE1',
        'prec_votes UST REPRESENTATIVE IN CONGRESS' : 'G18OHOR1',
        'prec_votes UST REPRESENTATIVE IN STATE LEGISLATURE' : 'G18OStHou',
        'prec_votes UST SECRETARY OF STATE' : 'G18OSOS',
        'prec_votes UST STATE SENATOR' : 'G18OStSen1',
        'prec_votes UST UNITED STATES SENATOR' : 'G18OSEN1',
        'prec_votes WCP MEMBER OF THE STATE BOARD OF EDUCATION' : 'G18OBoE2',
        'prec_votes WCP REPRESENTATIVE IN CONGRESS' : 'G18OHOR2',
        'prec_votes WCP STATE SENATOR' : 'G18OStSen2',
        'prec_votes NLP GOVERNOR' : 'G18OGOV2',
        'prec_votes NLP UNITED STATES SENATOR' : 'G18OSEN2' })
    

#get rid of other columns and save
#this is ready to be matched to precinct names now
prec_elec_rn = prec_elec_rn.fillna(0)
#prec_elec_rn['G18OGOV'] = prec_elec_rn['G18OGOV1'].astype(int) + prec_elec_rn['G18OGOV2'].astype(int)+ prec_elec_rn['G18OGOV3'].astype(int)
prec_elec_rn = prec_elec_rn[['G18DATG', 'G18DGOV','G18DBoE','G18DHOR','G18DStHou', 'G18DSOS', 'G18DStSen','G18DSEN',
                             'G18GGOV', 'G18GBoE','G18GHOR','G18GStHou', 'G18GStSen','G18GSEN',
                             'G18LATG', 'G18LGOV','G18LBoE','G18LHOR','G18LStHou', 'G18LSOS', 'G18LStSen',
                             'G18RATG', 'G18RGOV','G18RBoE','G18RHOR','G18RStHou', 'G18RSOS', 'G18RStSen','G18RSEN',
                             'G18NPATG', 'G18NPGOV','G18NPHOR', 'G18NPStHou','G18NPStSen','G18NPSEN',
                             'G18OATG', 'G18OGOV1','G18OBoE1','G18OHOR1','G18OStHou', 'G18OSOS', 'G18OStSen1','G18OSEN1','G18OBoE2', 
                             'G18OHOR2', 'G18OStSen2','G18OGOV2','G18OSEN2']]
prec_elec_rn["G18OGOV"] = prec_elec_rn.G18OGOV1.astype(int) + prec_elec_rn.G18OGOV2.astype(int)
prec_elec_rn['G18OSEN'] = prec_elec_rn.G18OSEN1.astype(int) + prec_elec_rn.G18OSEN2.astype(int)
prec_elec_rn['G18OBoE'] = prec_elec_rn.G18OBoE1.astype(int) + prec_elec_rn.G18OBoE2.astype(int)
prec_elec_rn['G18OStSen'] = prec_elec_rn.G18OStSen1.astype(int) + prec_elec_rn.G18OStSen2.astype(int)
prec_elec_rn['G18OHOR'] = prec_elec_rn.G18OHOR1.astype(int) + prec_elec_rn.G18OHOR2.astype(int)

prec_elec_rn = prec_elec_rn[['G18DATG', 'G18DGOV', 'G18DSEN', 'G18DHOR', 'G18DSOS','G18DBoE','G18DStHou', 'G18DStSen',
                             'G18RATG', 'G18RGOV','G18RSEN', 'G18RHOR', 'G18RSOS','G18RBoE','G18RStHou',  'G18RStSen', 
                             'G18GGOV', 'G18GSEN', 'G18GHOR', 'G18GBoE', 'G18GStHou','G18GStSen', 
                             'G18LATG', 'G18LGOV',  'G18LHOR','G18LSOS','G18LBoE','G18LStHou',  'G18LStSen', 
                             'G18NPATG','G18NPGOV','G18NPSEN', 'G18NPHOR', 'G18NPStHou', 'G18NPStSen', 
                             'G18OATG','G18OGOV','G18OSEN', 'G18OHOR', 'G18OSOS','G18OBoE', 'G18OStHou',  'G18OStSen']]
#this is ready to be matched to precinct names now

prec_elec_rn.to_csv('/Volumes/GoogleDrive/Shared drives/princeton_gerrymandering_project/OpenPrecincts/States for site/Michigan/Elections/MI_G18_SOS.csv')