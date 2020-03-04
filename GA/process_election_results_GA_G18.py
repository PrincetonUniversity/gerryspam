import pandas as pd
import geopandas as gpd
import numpy as np

'''
This takes in raw elections in the form OpenElections publishes in
it looks for statewide offices and filters out local ones
Results in dataframe organized by precinct rather than vote total
'''

#paste path to raw election results which have candidates as rows
raw_elec = '/Users/hwheelen/Documents/GitHub/OpenElections/openelections-data-nv/2016/20161108__nv__general__precinct.csv'

elec_df = pd.read_csv(raw_elec)
elec_df['loc_prec']=elec_df['Jurisdiction'].map(str) + ',' + elec_df['Precinct']
#elec_df['prec_name'] = 'Prec ' + elec_df['PrecinctNumber'].map(str) + ',' + 'Ward ' + elec_df['WardNumber']

#make list of office titles
offices_tot = elec_df['Contest'].unique()
counties_tot = elec_df['Jurisdiction'].unique()
state_offices = []
counties_office = {}
#loop through offices and find statewide ones
for office in offices_tot:
    counties  = []
    counties.append(elec_df.loc[elec_df['Contest'] == office, 'Jurisdiction'])
    #list of counties that had an election for that office
    counties_office[office] = counties
    c = counties_office[office][0].values
    D = {I: True for I in c}
    count = D.keys()
    if len(count) ==  len(counties_tot):
        state_offices.append(office)
state_elec = elec_df.loc[elec_df['Contest'].isin(state_offices)]

#get table of elections by precinct
prec_elec = pd.pivot_table(state_elec, index = ['loc_prec'], columns = ['Contest','Selection'], values = ['Votes'], aggfunc = np.sum)

prec_elec.columns = prec_elec.columns.to_series().str.join(' ')


columns = prec_elec.columns.values

#print columns and assign each one a 10 character name for the shapefile
print(columns)

#make dic for column name replacement using the columns printed in module above
#columns can only have 10 character names
prec_elec_rn = prec_elec.rename(columns = {
        'Votes Attorney General DUNCAN, WES': 'G18RATG',
        'Votes Attorney General FORD, AARON': 'G18DATG',
        'Votes Attorney General Hansen, Joel F.': 'G18OATG',
        'Votes Attorney General None Of These Candidates': 'G18NAATG',
        'Votes Governor BEST, RUSSELL': 'G18OGOV1' ,
        'Votes Governor BUNDY, RYAN': 'G18OGOV2',
        'Votes Governor LAXALT, ADAM PAUL': 'G18RGOV', 
        'Votes Governor LORD, JARED': 'G18OGOV3',
        'Votes Governor None Of These Candidates': 'G18NAGOV', 
        'Votes Governor SISOLAK, STEVE': 'G18DGOV',
        'Votes Lieutenant Governor HANSEN, JANINE': 'G18OLtGOV1',
        'Votes Lieutenant Governor MARSHALL, KATE': 'G18DLtGOV',
        'Votes Lieutenant Governor None Of These Candidates': 'G18NALtGOV',
        'Votes Lieutenant Governor ROBERSON, MICHAEL':'G18RLtGOV',
        'Votes Lieutenant Governor UEHLING, ED': 'G18OLtGOV2',
        'Votes Secretary Of State ARAUJO, NELSON': 'G18RSST',
        'Votes Secretary Of State Cegavske, Barbara K.': 'G18DSST',
        'Votes Secretary Of State None Of These Candidates': 'G18NASST',
        'Votes State Controller BYRNE, CATHERINE': 'G18DStCon',
        'Votes State Controller Knecht, Ron': 'G18RStCon',
        'Votes State Controller None Of These Candidates': 'G18NAStCon',
        'Votes State Treasurer BEERS, BOB' : 'G18RStTRE',
        'Votes State Treasurer CONINE, ZACH': 'G18DStTRE',
        'Votes State Treasurer HOGE, BILL': 'G18OStTRE',
        'Votes State Treasurer None Of These Candidates': 'G18NAStTRE',
        'Votes United States Senator BAKARI, KAMAU A.': 'G18OSEN1',
        'Votes United States Senator HAGAN, TIM': 'G18OSEN2',
        'Votes United States Senator Heller, Dean': 'G18RSEN',
        'Votes United States Senator MICHAELS, BARRY': 'G18OSEN3',
        'Votes United States Senator None Of These Candidates': 'G18NASEN',
        'Votes United States Senator ROSEN, JACKY': 'G18DSEN'})

#get rid of other columns and save
#this is ready to be matched to precinct names now
prec_elec_rn = prec_elec_rn[['G18RATG', 'G18DATG', 'G18OATG', 'G18NAATG', 'G18OGOV1', 'G18OGOV2','G18RGOV', 'G18OGOV3', 'G18NAGOV',
                             'G18DGOV', 'G18OLtGOV1', 'G18DLtGOV','G18NALtGOV', 'G18RLtGOV', 'G18OLtGOV2', 'G18RSST', 'G18DSST',
                             'G18NASST', 'G18DStCon', 'G18RStCon', 'G18NAStCon','G18RStTRE', 'G18DStTRE', 'G18OStTRE', 'G18NAStTRE', 
                             'G18OSEN1','G18OSEN2', 'G18RSEN', 'G18OSEN3', 'G18NASEN', 'G18DSEN']]
prec_elec_rn = prec_elec_rn.fillna(0)
prec_elec_rn['G18OGOV'] = prec_elec_rn['G18OGOV1'].astype(int) + prec_elec_rn['G18OGOV2'].astype(int)+ prec_elec_rn['G18OGOV3'].astype(int)
prec_elec_rn['G18OLtGOV'] = prec_elec_rn['G18OLtGOV1'].astype(int) + prec_elec_rn['G18OLtGOV1'].astype(int)
prec_elec_rn['G18OSEN'] = prec_elec_rn['G18OSEN1'].astype(int) + prec_elec_rn['G18OSEN2'].astype(int)+ prec_elec_rn['G18OSEN3'].astype(int)

prec_elec_rn = prec_elec_rn[['G18RATG', 'G18DATG', 'G18OATG', 'G18NAATG','G18RGOV', 'G18NAGOV', 'G18DGOV', 'G18OGOV', 'G18DLtGOV','G18NALtGOV', 
                             'G18RLtGOV','G18OLtGOV','G18RSST', 'G18DSST','G18NASST', 'G18DStCon', 'G18RStCon', 'G18NAStCon', 'G18RStTRE',
                             'G18DStTRE', 'G18OStTRE', 'G18NAStTRE','G18RSEN','G18NASEN', 'G18DSEN','G18OSEN']]


prec_elec_rn.to_csv('/Volumes/GoogleDrive/Shared drives/princeton_gerrymandering_project/OpenPrecincts/States for site/Nevada/Election Data/Cleaned Election Data/NVG18.csv')
