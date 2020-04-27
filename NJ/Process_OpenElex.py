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
        'votes President R': 'D16RPRS1', 
        'votes President REP': 'D16RPRS2',
         'votes President Rep': 'D16RPRS3',
         'votes President Republican': 'D16RPRS',
        'votes President and Vice President of the United States REP': 'G16RPRS',
        'votes U.S. House DEM' : 'G16DHOR',
        'votes U.S. House IAP' : 'G16IHOR',
        'votes U.S. House LPN': 'G16LHOR',
        'votes U.S. House REP' : 'G16RHOR',
        'votes United States Senator DEM': 'G16DSEN',
        'votes United States Senator IAP' : 'G16ISEN',
        'votes United States Senator REP': 'G16RSEN'})

#prec_elec_rn['G16OGOV'] = prec_elec_rn['G16OGOV1'].astype(int) + prec_elec_rn['G16OGOV2'].astype(int)+ prec_elec_rn['G16OGOV3'].astype(int)


#get rid of other columns and save
#this is ready to be matched to precinct names now
prec_elec_rn.to_csv('/Volumes/GoogleDrive/Shared drives/princeton_gerrymandering_project/OpenPrecincts/States for site/Nevada/Election Data/Cleaned Election Data/NVG16.csv')
