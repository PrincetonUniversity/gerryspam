#!/usr/bin/env python
# coding: utf-8

# In[21]:


import pandas as pd
import geopandas as gpd
import numpy as np


# In[22]:


#paste path to raw election results which have candidates as rows
raw_elec = '/Users/laeocrnkovic-rubsamen/Desktop/NY1/20181106__ny__general__precinct.csv'

elec_df = gpd.read_file(raw_elec)
elec_df['loc_prec'] = elec_df['county'].map(str) + ',' + elec_df['precinct']


# In[23]:


#make list of office titles
offices_tot = elec_df['office'].unique()
print(offices_tot)
print('1')
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

        
state_offices = ['Governor', 'Comptroller', 'Attorney General', 'U.S. Senate',
       'U.S. House', 'State Senate', 'State Assembly']

state_elec = elec_df.loc[elec_df['office'].isin(state_offices)]



print('2')
print(state_elec)

#get table of elections by precinct

print('3')

prec_elec = pd.pivot_table(state_elec, index = ['loc_prec', 'county', 'precinct'], columns = ['office','candidate'], values = ['votes'], aggfunc = np.sum);

prec_elec.columns = prec_elec.columns.to_series().str.join(' ');

columns = prec_elec.columns.values;

#print(prec_elec)

#print columns and assign each one a 10 character name for the shapefile
print('3')
#print(columns)


# In[38]:


#make dic for column name replacement using the columns printed in module above
#columns can only have 10 character names'

##quick standardization function to reduce number of column numbers
def standardize(word):
    print(word)
    # delete middle initial with period
    period = word.find(".")
    length = len(word)
    if period >= 9:
        word = word[0:period-2] + word[period+1:length]
    
    # delete middle initial without period
    length = len(word)
    x = 0
    while (x < length-2):
        if word[x] == " ":
            if word[x+2] == " ":
                word = word[0:x] + word[x+2:length]
                length = len(word)
        x = x + 1
    
    # delete the '\n' characters
    newLine = word.find("\n")
    while (newLine != -1):
        length = len(word)
        word = word[0:newLine] + " " + word[newLine+1:length]
        newLine = word.find("\n")

    # title case
    word = word.title()
    
    # delete trailing space
    length = len(word)
    if word[length-1] == " ":
        word = word[0:length-1]
    
    print(word)
    return word

count = 0;
while (count < len(prec_elec.columns)):
    name = prec_elec.columns[count]
    new_name = standardize(name)
    prec_elec.rename(columns ={name : new_name})
    
    for col in prec_elec.columns:
        if new_name == col:
            prec_elec["New"] = prec_elec[new_name] + prec_elec[col]
            prec_elec.drop([col])
            prec_elec.drop([new_name])
            prec_elec.rename(columns ={"New" : new_name})

            
            
    count = count +1
            
print(len(prec_elec.columns))
print(prec_elec.columns.values)


# In[5]:





prec_elec_rn = prec_elec.rename(columns = {
    'votes Comptroller Cruger E Gallaudet': 'NYG18LCOM1',
    'votes Comptroller Cruger E. Gallaudet': 'NYG18LCOM2',
    'votes Comptroller Cruger E. Gallaudet\n': 'NYG18LCOM3',
    'votes Comptroller Cruger E. Gallaudet ': 'NYG18LCOM4',
    'votes Comptroller Cruger Gallaudet': 'NYG18LCOM5',
    'votes Comptroller Gallaudet': 'NYG18LCOM6',
    'votes Comptroller Gallaudet ': 'NYG18LCOM7',

    'votes Comptroller DiNapoli'
    'votes Comptroller Thomas A. DiNapoli'
    'votes Comptroller Thomas DiNapoli'
    'votes Comptroller Thomas P Di Napoli'
    'votes Comptroller Thomas P.\nDiNapoli\n'
    'votes Comptroller Thomas P. DiNapoli'
    'votes Comptroller Thomas P. DiNapoli\n'
    'votes Comptroller Thomas P. DiNapoli '

    'votes Comptroller Dunlea'
    'votes Comptroller Mark Dunlea'
    'votes Comptroller Mark Dunlea\n'
    'votes Comptroller Mark Dunlea   '

    'votes Comptroller Jonathan Trichter'
    'votes Comptroller Jonathan Trichter\n'
    'votes Comptroller Jonathan Trichter '
    'votes Comptroller Trichter'

    'votes Attorney General LETITIA A. JAMES': 'NYG18DATG1',
    'votes Attorney General Laetita A. James': 'NYG18DATG2',
    'votes Attorney General Lenitia James': 'NYG18DATG3',
    'votes Attorney General Letitia A James': 'NYG18DATG4',
    'votes Attorney General Letitia A. James': 'NYG18DATG5',
    'votes Attorney General Letitia A. James\n': 'NYG18DATG6',
    'votes Attorney General Letitia James': 'NYG18DATG7',
    'votes Attorney General James': 'NYG18DATG8',
    'votes Attorney General CHRISTOPHER B. GARVEY': 'NYG18LATG1',
    'votes Attorney General Christopher B Garvey': 'NYG18LATG2',
    'votes Attorney General Christopher B.\nGarvey\n': 'NYG18LATG3',
    'votes Attorney General Christopher B. Garvey': 'NYG18LATG4',
    'votes Attorney General Christopher B.Garvey': 'NYG18LATG5',
    'votes Attorney General Christopher G. Garvey': 'NYG18LATG6',
    'votes Attorney General Christopher Garvey': 'NYG18LATG7',
    'votes Attorney General Christopher P. Garvey': 'NYG18LATG8',
    'votes Attorney General Garvey': 'NYG18LATG9',
    'votes Attorney General Keith Wofford': 'NYG18RATG1',
    'votes Attorney General Keith Wofford\n': 'NYG18RATG2',
    'votes Attorney General Kieth Wofford': 'NYG18RATG3',
    'votes Attorney General MICHAEL SUSSMAN': 'NYG18GATG1',
    'votes Attorney General Michael Sussman': 'NYG18GATG2',
    'votes Attorney General Michael Sussman\n': 'NYG18GATG3',
    'votes Attorney General Michael Sussman ': 'NYG18GATG4',
    'votes Attorney General NANCY B. SILWA': 'NYG18IATG1',
    'votes Attorney General Nancy B Sliwa': 'NYG18IATG2',
    'votes Attorney General Nancy B. Silwa': 'NYG18IATG3',
    'votes Attorney General Nancy B. Sliwa': 'NYG18IATG4',
    'votes Attorney General Nancy B. Sliwa\n': 'NYG18IATG5',
    'votes Attorney General Nancy B. Sliwa ': 'NYG18IATG6',
    'votes Attorney General Nancy Sliwa': 'NYG18IATG7',

    'votes Attorney General Ref Nancy Sliwa': 'NYG18IATG2',
    'votes Governor Dem Andrew Cuomo': 'NYG18DGOV1',
    'votes Governor Ind Andrew Cuomo': 'NYG18DGOV2',
    'votes Governor Wor Andrew Cuomo': 'NYG18DGOV3',
    'votes Governor WEP Andrew Cuomo': 'NYG18DGOV4',
    'votes Governor Rep Marc Molinaro': 'NYG18RGOV1',
    'votes Governor Con Marc Molinaro': 'NYG18RGOV2',
    'votes Governor Ref Marc Molinaro': 'NYG18RGOV3',
    'votes Governor Grn Howie Hawkins': 'NYG18IGOV1',
    'votes Governor Sam Stephanie Miner': 'NYG18IGOV2',
    'votes Governor Lib Larry Sharpe': 'NYG18IGOV3',
    'votes U.S. Sentate Dem Kirsten Gillibrand': 'NYG18DUSS1',
    'votes U.S. Sentate Wor Kirsten Gillibrand': 'NYG18DUSS2',
    'votes U.S. Sentate Ind Kirsten Gillibrand': 'NYG18DUSS3',
    'votes U.S. Sentate WEP Kirsten Gillibrand': 'NYG18DUSS4',
    'votes U.S. Sentate Rep Chele Farley': 'NYG18RUSS1',
    'votes U.S. Sentate Con Chele Farley': 'NYG18RUSS2',
    'votes U.S. Sentate Ref Chele Farley': 'NYG18RUSS3'})

prec_elec_rn = prec_elec_rn.fillna(0)

prec_elec_rn['NYG18DATG'] = prec_elec_rn['NYG18DATG1'].astype(int) + prec_elec_rn['NYG18DATG2'].astype(int)+ prec_elec_rn['NYG18DATG3'].astype(int)
prec_elec_rn['NYG18RATG'] = prec_elec_rn['NYG18RATG1'].astype(int) + prec_elec_rn['NYG18RATG2'].astype(int)
prec_elec_rn['NYG18IATG'] = prec_elec_rn['NYG18IATG1'].astype(int) + prec_elec_rn['NYG18IATG2'].astype(int)+ prec_elec_rn['NYG18IATG3'].astype(int)
prec_elec_rn['NYG18DGOV'] = prec_elec_rn['NYG18DGOV1'].astype(int) + prec_elec_rn['NYG18DGOV2'].astype(int)+ prec_elec_rn['NYG18DGOV3'].astype(int)+ prec_elec_rn['NYG18DGOV4'].astype(int)
prec_elec_rn['NYG18RGOV'] = prec_elec_rn['NYG18RGOV1'].astype(int) + prec_elec_rn['NYG18RGOV1'].astype(int)+ prec_elec_rn['NYG18RGOV3'].astype(int)
prec_elec_rn['NYG18IGOV'] = prec_elec_rn['NYG18IGOV1'].astype(int) + prec_elec_rn['NYG18IGOV2'].astype(int)+ prec_elec_rn['NYG18IGOV3'].astype(int)
prec_elec_rn['NYG18DUSS'] = prec_elec_rn['NYG18DUSS1'].astype(int) + prec_elec_rn['NYG18DUSS2'].astype(int)+ prec_elec_rn['NYG18DUSS3'].astype(int)+ prec_elec_rn['NYG18DUSS4'].astype(int)
prec_elec_rn['NYG18RUSS'] = prec_elec_rn['NYG18RUSS1'].astype(int) + prec_elec_rn['NYG18RUSS2'].astype(int)+ prec_elec_rn['NYG18RUSS3'].astype(int)

prec_elec_rn = prec_elec_rn[[
    'NYG18DATG', 'NYG18RATG', 'NYG18IATG', 
    'NYG18DGOV', 'NYG18RGOV', 'NYG18IGOV',
    'NYG18DUSS', 'NYG18RUSS', 'NYG18IUSS']]
#this is ready to be matched to precinct names now

prec_elec_rn.to_csv('/Users/laeocrnkovic-rubsamen/Desktop/NY/NY_G18.csv')

######################################################
# MEDSL RESULTS ######################################
######################################################


# In[ ]:




