import pandas as pd
import geopandas as gpd
import numpy as np

#paste path to raw election results which have candidates as rows
raw_elec = '/Users/hopecj/projects/AR/Elections/raw/openelections-data-ar-master/2018/20181106__ar__general__precinct.csv'

elec_df = gpd.read_file(raw_elec)
elec_df['loc_prec'] = elec_df['county'].map(str) + ',' + elec_df['precinct']

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
prec_elec = pd.pivot_table(state_elec, index = ['loc_prec', 'county', 'precinct'], columns = ['office','party','candidate'], values = ['votes'], aggfunc = np.sum)

prec_elec.columns = prec_elec.columns.to_series().str.join(' ')

columns = prec_elec.columns.values

#print columns and assign each one a 10 character name for the shapefile
print(columns)

#make dic for column name replacement using the columns printed in module above
#columns can only have 10 character names
prec_elec_rn = prec_elec.rename(columns = {
        'votes Attorney General DEM Mike Lee': 'G18DATG1',
        'votes Attorney General Dem Mike Lee': 'G18DATG2',
        'votes Attorney General LIB Kerry Hicks': 'G18LATG1',
        'votes Attorney General Lib Kerry Hicks': 'G18LATG2',
        'votes Attorney General REP Attorney General Leslie Rutledge': 'G18RATG1',
        'votes Attorney General REP Leslie Rutledge': 'G18RATG2',
        'votes Attorney General Rep Attorney General Leslie Rutledge': 'G18RATG3',
        'votes Attorney General Rep Leslie Rutledge': 'G18RATG4',
        'votes Governor DEM Jared K. Henderson': 'G18DGOV1',
        'votes Governor Dem Jared K. Henderson': 'G18DGOV2',
        'votes Governor LIB Mark West': 'G18LGOV1',
        'votes Governor Lib Mark West':  'G18LGOV2',
        'votes Governor REP Asa Hutchinson': 'G18RGOV1',
        'votes Governor REP Governor Asa Hutchinson': 'G18RGOV2',
        'votes Governor Rep Governor Asa Hutchinson': 'G18RGOV3',
        'votes Secretary of State DEM Susan Inman': 'G18DSecS1',
        'votes Secretary of State Dem Susan Inman': 'G18DSecS2',
        'votes Secretary of State LIB Christopher Olson': 'G18LSecS1',
        'votes Secretary of State Lib Christopher Olson': 'G18LSecS2',
        'votes Secretary of State REP Commissioner of State Lands John Thurston': 'G18RSecS1',
        'votes Secretary of State REP John Thurston Com of State Lands': 'G18RSecS2',
        'votes Secretary of State REP John Thurston Commissioner of State Lands': 'G18RSecS3',
        'votes Secretary of State Rep John Thurston Commissioner of State Lands': 'G18RSecS4',
        'votes State Treasurer LIB Ashley Ewald': 'G18LTRES1',
        'votes State Treasurer Lib Ashley Ewald': 'G18LTRES2',
        'votes State Treasurer REP Treasurer of State Dennis Milligan': 'G18RTRES1',
        'votes State Treasurer Rep Treasurer of State Dennis Milligan': 'G18RTRES2'})

prec_elec_rn = prec_elec_rn.fillna(0)
    
prec_elec_rn['G18DATG'] = prec_elec_rn['G18DATG1'].astype(int) + prec_elec_rn['G18DATG2'].astype(int)
prec_elec_rn['G18LATG'] = prec_elec_rn['G18LATG1'].astype(int) + prec_elec_rn['G18LATG2'].astype(int)
prec_elec_rn['G18RATG'] = prec_elec_rn['G18RATG1'].astype(int) + prec_elec_rn['G18RATG2'].astype(int)+ prec_elec_rn['G18RATG3'].astype(int)+ prec_elec_rn['G18RATG4'].astype(int)
prec_elec_rn['G18DGOV'] = prec_elec_rn['G18DGOV1'].astype(int) + prec_elec_rn['G18DGOV2'].astype(int)
prec_elec_rn['G18LGOV'] = prec_elec_rn['G18LGOV1'].astype(int) + prec_elec_rn['G18LGOV2'].astype(int)
prec_elec_rn['G18RGOV'] = prec_elec_rn['G18RGOV1'].astype(int) + prec_elec_rn['G18RGOV2'].astype(int)+ prec_elec_rn['G18RGOV3'].astype(int)
prec_elec_rn['G18DSecS'] = prec_elec_rn['G18DSecS1'].astype(int) + prec_elec_rn['G18DSecS2'].astype(int)
prec_elec_rn['G18LSecS'] = prec_elec_rn['G18LSecS1'].astype(int) + prec_elec_rn['G18LSecS2'].astype(int)
prec_elec_rn['G18RSecS'] = prec_elec_rn['G18RSecS1'].astype(int) + prec_elec_rn['G18RSecS2'].astype(int)+ prec_elec_rn['G18RSecS3'].astype(int)+ prec_elec_rn['G18RSecS4'].astype(int)
prec_elec_rn['G18LTRES'] = prec_elec_rn['G18LTRES1'].astype(int) + prec_elec_rn['G18LTRES2'].astype(int)
prec_elec_rn['G18RTRES'] = prec_elec_rn['G18RTRES1'].astype(int) + prec_elec_rn['G18RTRES2'].astype(int)


prec_elec_rn = prec_elec_rn[[
        'G18DGOV', 'G18LGOV', 'G18RGOV', 
        'G18DATG', 'G18RATG', 'G18LATG',
        'G18DSecS', 'G18LSecS', 'G18RSecS',
        'G18RTRES', 'G18LTRES']]
#this is ready to be matched to precinct names now

prec_elec_rn.to_csv('/Users/hopecj/projects/AR/Elections/AR_G18.csv')