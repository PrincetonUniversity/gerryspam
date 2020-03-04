import geopandas as gpd
import pandas as pd
import numpy as np

#list states you need data for
states = ['Michigan']

#filepath to country wide 2018 precinct level returns
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
    state_offices = ['State Senate', 'State House Position 1','State House Position 2', 'US House', 'US Senate']
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
        'votes democrat State House Position 1' : 'G18DStHou1',
        'votes democrat State House Position 2' : 'G18DStHou2', 
        'votes democrat State Senate' : 'G18DStSen',
        'votes democrat US House'  : 'G18DHOR',
        'votes democrat US Senate' : 'G18DSEN',
        'votes independent State House Position 1' : 'G18IStHou1',
        'votes independent State House Position 2' : 'G18IStHou2',
        'votes independent State Senate' : 'G18IStSen',
        'votes independent republican State Senate' : 'G18IStSen',
        'votes libertarian State House Position 1' : 'G18LStHou1',
        'votes libertarian State House Position 2' : 'G18LStHou2',
        'votes libertarian State Senate'  : 'G18LStSen',
        'votes libertarian US House' : 'G18LHOR',
        'votes no party preference State House Position 1' : 'G18NPStHou1',
        'votes no party preference State House Position 2' : 'G18NPStHou2',
        'votes no party preference State Senate' : 'G18NPStSen',
        'votes no party preference US House' : 'G18NPHOR',
        'votes no party preference US Senate' : 'G18NPSEN',
        'votes republican State House Position 1' : 'G18RStHou1',
        'votes republican State House Position 2'  : 'G18RStHou2',
        'votes republican State Senate' : 'G18RStSen',
        'votes republican US House'  : 'G18RHOR',
        'votes republican US Senate' : 'G18RSEN'})
    

#get rid of other columns and save
#this is ready to be matched to precinct names now
prec_elec_rn = prec_elec_rn.fillna(0)
#prec_elec_rn['G18OGOV'] = prec_elec_rn['G18OGOV1'].astype(int) + prec_elec_rn['G18OGOV2'].astype(int)+ prec_elec_rn['G18OGOV3'].astype(int)

#this is ready to be matched to precinct names now

prec_elec_rn.to_csv('/Volumes/GoogleDrive/Shared drives/princeton_gerrymandering_project/OpenPrecincts/States for site/Washington/GA_G18_MIT.csv')