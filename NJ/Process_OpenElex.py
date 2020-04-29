import pandas as pd
import geopandas as gpd
import numpy as np

'''
This takes in raw elections in the form OpenElections publishes in
it looks for statewide offices and filters out local ones
Results in dataframe organized by precinct rather than vote total
'''

#paste path to raw election results which have candidates as rows
raw_elec = 'https://raw.githubusercontent.com/openelections/openelections-data-nj/master/2016/20161108__nj__general__precinct.csv'

elec_df = pd.read_csv(raw_elec)
elec_df['loc_prec']=elec_df['county'].map(str).replace(' County','') + ',' + elec_df['precinct']
#elec_df['prec_name'] = 'Prec ' + elec_df['PrecinctNumber'].map(str) + ',' + 'Ward ' + elec_df['WardNumber']

#make list of office titles
offices_tot = elec_df['office'].unique()
counties_tot = elec_df['county'].unique()
state_offices = []
counties_office = {}
#loop through offices and find statewide ones
for office in offices_tot:
    counties  = []
    counties.append(elec_df.loc[elec_df['office'] == office, 'county'])
    #list of counties that had an election for that office
    counties_office[office] = counties
    c = counties_office[office][0].values
    D = {I: True for I in c}
    count = D.keys()
    if len(count) ==  len(counties_tot):
        state_offices.append(office)
state_elec = elec_df.loc[elec_df['office'].isin(state_offices)]

#get table of elections by precinct
prec_elec = pd.pivot_table(state_elec, index = ['loc_prec'], columns = ['office','party'], values = ['votes'], aggfunc = np.sum)
prec_elec.columns = prec_elec.columns.to_series().str.join(' ')
columns = prec_elec.columns.values
print(columns)

#make dic for column name replacement using the columns printed in module above
#columns can only have 10 character names
prec_elec_rn = prec_elec.rename(columns = {
        'votes President DEM': 'G16DPRS',
        'votes President Dem': 'G16DPRS2',
        'votes President D': 'G16DPRS3',
        'votes President Democratic': 'G16DPRS4',
        'votes President R': 'G16RPRS', 
        'votes President REP': 'G16RPRS2',
        'votes President Rep': 'G16RPRS3',
        'votes President Republican': 'G16RPRS4',
        'votes U.S. House D': 'G16DHOR',
        'votes U.S. House Dem': 'G16DHOR2',
        'votes U.S. House Democratic': 'G16DHOR3',
        'votes U.S. House DEM' : 'G16DHOR4',
        'votes U.S. House R': 'G16RHOR', 
        'votes U.S. House REP': 'G16RHOR2', 
        'votes U.S. House Rep': 'G16RHOR3', 
        'votes U.S. House Republican': 'G16RHOR4'})

prec_elec_rn.isnull().values.any()
prec_elec_rn = prec_elec_rn.fillna(0)

prec_elec_rn['G16DPRS'] = prec_elec_rn['G16DPRS'].astype(int) + prec_elec_rn['G16DPRS2'].astype(int)+ prec_elec_rn['G16DPRS3'].astype(int) + prec_elec_rn['G16DPRS4'].astype(int)
prec_elec_rn['G16RPRS'] = prec_elec_rn['G16RPRS'].astype(int) + prec_elec_rn['G16RPRS2'].astype(int)+ prec_elec_rn['G16RPRS3'].astype(int) + prec_elec_rn['G16RPRS4'].astype(int)
prec_elec_rn['G16DHOR'] = prec_elec_rn['G16DHOR'].astype(int) + prec_elec_rn['G16DHOR2'].astype(int)+ prec_elec_rn['G16DHOR3'].astype(int) + prec_elec_rn['G16DHOR4'].astype(int)
prec_elec_rn['G16RHOR'] = prec_elec_rn['G16RHOR'].astype(int) + prec_elec_rn['G16RHOR2'].astype(int)+ prec_elec_rn['G16RHOR3'].astype(int) + prec_elec_rn['G16RHOR4'].astype(int)

prec_elec_keep = prec_elec_rn[['G16DPRS', 'G16RPRS', 'G16DHOR', 'G16RHOR']]
prec_elec_keep["year"] = 2016
prec_elec_keep.head()

#get rid of other columns and save
#this is ready to be matched to precinct names now
prec_elec_keep.to_csv('/Users/hopecj/projects/gerryspam/NJ/dat/NJ_G16_OpenElex.csv')
