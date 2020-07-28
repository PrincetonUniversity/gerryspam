#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import geopandas as gpd
import numpy as np


# In[2]:


#paste path to raw election results which have candidates as rows
raw_elec = '/Users/laeocrnkovic-rubsamen/Desktop/NY1/20181106__ny__general__precinct.csv'

elec_df = gpd.read_file(raw_elec)
elec_df['loc_prec'] = elec_df['county'].map(str) + ',' + elec_df['precinct']


# In[3]:


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


# In[8]:


#make dic for column name replacement using the columns printed in module above
#columns can only have 10 character names'

##quick standardization function to reduce number of column numbers
def standardize(word):
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
    
    return word

count = 0;
length = len(prec_elec.columns)
while (count < length):
    name = prec_elec.columns[count]
    print(name)
    new_name = standardize(name)
    prec_elec.rename (columns ={name : new_name})
    print(prec_elec.columns[count])

    
    for col in prec_elec.columns:
        if new_name == col:
            prec_elec["New"] = prec_elec[new_name] + prec_elec[col]
            prec_elec.drop([col])
            prec_elec.drop([new_name])
            prec_elec.rename(columns ={"New" : new_name})
            length = length - 1
            
            
    count = count +1
            
print(len(prec_elec.columns))
print(prec_elec.columns.values)
