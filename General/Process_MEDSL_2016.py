import geopandas as gpd
import pandas as pd
import numpy as np

#list states you need data for
states = ['Georgia']

#filepath to country wide 2018 precinct level returns
elec_fp = '/Users/hwheelen/Documents/GitHub/MEDSL/official-precinct-returns/2016-precinct-house/2016-precinct-house/2016-precinct-house.csv'
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
    #state_offices = ['State Senate', 'State House Position 1','State House Position 2', 'US House', 'US Senate']
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
        'votes democratic Attorney General'
        'votes democratic Commissioner Of Agriculture'
        'votes democratic Commissioner Of Insurance'
        'votes democratic Commissioner Of Labor' 
        'votes democratic Governor'
        'votes democratic Lieutenant Governor'
        'votes democratic Public Service Commission'
        'votes democratic Secretary Of State'
        'votes democratic State School Superintendent'
        'votes democratic State Senate'
        'votes libertarian Commissioner Of Insurance'
        'votes libertarian Governor'
        'votes libertarian Public Service Commission'
        'votes libertarian Secretary Of State'
        'votes republican Attorney General'
        'votes republican Commissioner Of Agriculture'
        'votes republican Commissioner Of Insurance'
        'votes republican Commissioner Of Labor' 'votes republican Governor'
        'votes republican Lieutenant Governor'
        'votes republican Public Service Commission'
        'votes republican Secretary Of State'
        'votes republican State School Superintendent',
        'votes republican State Senate']
})
    

#get rid of other columns and save
#this is ready to be matched to precinct names now
prec_elec_rn = prec_elec_rn.fillna(0)
#prec_elec_rn['G18OGOV'] = prec_elec_rn['G18OGOV1'].astype(int) + prec_elec_rn['G18OGOV2'].astype(int)+ prec_elec_rn['G18OGOV3'].astype(int)

#this is ready to be matched to precinct names now

prec_elec_rn.to_csv('/Volumes/GoogleDrive/Shared drives/princeton_gerrymandering_project/OpenPrecincts/States for site/Washington/GA_G18_MIT.csv')