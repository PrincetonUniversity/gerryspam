import geopandas as gpd
import pandas as pd
import numpy as np

#list states you need data for
states = ['Georgia']

#filepath to MEDSEL country wide 2018 precinct level returns
elec_fp = '/Users/hwheelen/Documents/GitHub/MEDSL/2018-elections-official/precinct_2018.csv'
#load into dataframe
elec_df = pd.read_csv(elec_fp, encoding = "ISO-8859-1")

#states = elec_df.state.unique()
statewide_offices = []
parties = elec_df.party.unique()
#get state-level dataset
for state in states:
    state_df = elec_df.loc[elec_df.state == state]
    state_df.precinct = state_df.county.map(str) + ',' + state_df.precinct.map(str)
    #make list of office titles
    offices_tot = state_df['office'].unique()
    counties_tot = state_df['county'].unique()
    state_offices = []
    counties_office = {}
    #loop through offices and find statewide ones
    for office in offices_tot:
        counties  = []
        counties.append(state_df.loc[state_df['office'] == office, 'county'])
        #list of counties that had an election for that office
        counties_office[office] = counties
        c = counties_office[office][0].values
        D = {I: True for I in c}
        count = D.keys()
        if len(count) ==  len(counties_tot):
            state_offices.append(office)
    state_offices = ['Governor','Lieutenant Governor','Secretary Of State','Attorney General',
                     'Commissioner Of Agriculture','Commissioner Of Insurance','State School Superintendent',
                     'Commissioner Of Labor','Public Service Commission','State Senate']
    state_elec = state_df.loc[state_df['office'].isin(state_offices)]
    #statewide_offices.append(state_offices)
#get table of elections by precinct
prec_elec = pd.pivot_table(state_elec, index = ['precinct'], columns = ['party','office'], values = ['votes'], aggfunc = np.sum)

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
        'votes democratic Attorney General': 'G18DATG',
        'votes democratic Commissioner Of Agriculture': 'G18DCmAg',
        'votes democratic Commissioner Of Insurance': 'G18DCmIns',
        'votes democratic Commissioner Of Labor' : 'G18DCmLab',
        'votes democratic Governor': 'G18DGOV',
        'votes democratic Lieutenant Governor': 'G18DLTG',
        'votes democratic Public Service Commission': 'G18DPbSrv',
        'votes democratic Secretary Of State': 'G18DSOS',
        'votes democratic State School Superintendent': 'G18DSchSpr',
        'votes democratic State Senate': 'G18DStSen',
        'votes libertarian Commissioner Of Insurance': 'G18LCmIns',
        'votes libertarian Governor': 'G18LGOV',
        'votes libertarian Public Service Commission': 'G18LPbSrv',
        'votes libertarian Secretary Of State': 'G18LSOS',
        'votes republican Attorney General': 'G18RATG',
        'votes republican Commissioner Of Agriculture': 'G18RCmAg',
        'votes republican Commissioner Of Insurance': 'G18RCmIns',
        'votes republican Commissioner Of Labor' : 'G18RCmLab',
        'votes republican Governor': 'G18RGOV',
        'votes republican Lieutenant Governor': 'G18RLTG',
        'votes republican Public Service Commission' : 'G18RPbSrv',
        'votes republican Secretary Of State': 'G18RSOS',
        'votes republican State School Superintendent': 'G18RSchSpr',
        'votes republican State Senate': 'G18RStSen'})
    

#get rid of other columns and save
#this is ready to be matched to precinct names now
prec_elec_rn = prec_elec_rn.fillna(0)
#prec_elec_rn['G18OGOV'] = prec_elec_rn['G18OGOV1'].astype(int) + prec_elec_rn['G18OGOV2'].astype(int)+ prec_elec_rn['G18OGOV3'].astype(int)

#this is ready to be matched to precinct names now

prec_elec_rn.to_csv('/Volumes/GoogleDrive/Shared drives/princeton_gerrymandering_project/OpenPrecincts/States for site/Georgia/GA_G18_MIT.csv')