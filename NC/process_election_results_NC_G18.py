import pandas as pd
import geopandas as gpd
import numpy as np

'''
This takes in raw elections in the form OpenElections publishes in
it looks for statewide offices and filters out local ones
Results in dataframe organized by precinct rather than vote total
'''

#paste path to raw election results which have candidates as rows
raw_elec = './NC/20181106__nc__general__precinct__raw.csv'

elec_df = pd.read_csv(raw_elec)
elec_df['loc_prec']=elec_df['parent_jurisdiction'].map(str) + elec_df['jurisdiction']
#elec_df['prec_name'] = 'Prec ' + elec_df['PrecinctNumber'].map(str) + ',' + 'Ward ' + elec_df['WardNumber']

#make list of office titles
offices_tot = elec_df['office'].unique()
counties_tot = elec_df['parent_jurisdiction'].unique()
state_offices = []
counties_office = {}
#loop through offices and find statewide ones
for office in offices_tot:
    counties  = []
    counties.append(elec_df.loc[elec_df['office'] == office, 'parent_jurisdiction'])
    #list of counties that had an election for that office
    counties_office[office] = counties
    c = counties_office[office][0].values
    D = {I: True for I in c}
    count = D.keys()
    if len(count) ==  len(counties_tot):
        state_offices.append(office)
state_elec = elec_df.loc[elec_df['office'].isin(state_offices)]

#get table of elections by precinct
prec_elec = pd.pivot_table(state_elec, index = ['loc_prec'], columns = ['party','office'], values = ['votes'], aggfunc = np.sum)

prec_elec.columns = prec_elec.columns.to_series().str.join(' ')

columns = prec_elec.columns.values

#print columns and assign each one a 10 character name for the shapefile
print(columns)

#make dic for column name replacement using the columns printed in module above
#columns can only have 10 character names
prec_elec_rn = prec_elec.rename(columns = {'votes CST NC HOUSE OF REPRESENTATIVES' : 'G18CStHOR',
                                           'votes CST NC STATE SENATE' : 'G18CStSen',
                                           'votes CST US HOUSE OF REPRESENTATIVES' : 'G18CHOR',
                                           'votes DEM NC HOUSE OF REPRESENTATIVES' : 'G18DStHOR',
                                           'votes DEM NC STATE SENATE' : 'G18DStSEN',
                                           'votes DEM US HOUSE OF REPRESENTATIVES' : 'G18DHOR',
                                           'votes GRE NC HOUSE OF REPRESENTATIVES' : 'G18GStHOR',
                                           'votes GRE US HOUSE OF REPRESENTATIVES' : 'G18GHOR',
                                           'votes LIB NC HOUSE OF REPRESENTATIVES' : 'G18LStHOR',
                                           'votes LIB NC STATE SENATE' : 'G18LStSEN',
                                           'votes LIB US HOUSE OF REPRESENTATIVES' : 'G18LHOR',
                                           'votes REP NC HOUSE OF REPRESENTATIVES' : 'G18RStHOR',
                                           'votes REP NC STATE SENATE' : 'G18RStSEN',
                                           'votes REP US HOUSE OF REPRESENTATIVES' : 'G18RHOR',
                                           'votes UNA NC HOUSE OF REPRESENTATIVES' : 'G18UnaHOR'})

#get rid of other columns and save
#this is ready to be matched to precinct names now
#prec_elec_rn = prec_elec_rn[[]]


prec_elec_rn.to_csv('./NC/Cleaned Results/NCG18.csv')
