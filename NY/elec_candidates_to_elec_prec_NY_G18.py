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
        
state_offices = ['Governor', 'Comptroller', 'Attorney General', 'U.S. Senate']

state_elec = elec_df.loc[elec_df['office'].isin(state_offices)]

state_elec_votes = state_elec['votes']

state_elec_votes = state_elec_votes.replace(r'^\s*$', '0', regex=True)
state_elec_votes = state_elec_votes.str.replace(',', '').astype(float)

print(state_elec_votes)

state_elec['votes'] = state_elec_votes
print('2')
print(state_elec)

#get table of elections by precinct

print('3')

prec_elec = pd.pivot_table(state_elec, values = ['votes'], index = ['loc_prec'], columns = ['office','candidate'],  aggfunc = np.sum)

prec_elec.columns = prec_elec.columns.to_series().str.join(' ')

columns = prec_elec.columns.values;

print(prec_elec)

#print columns and assign each one a 10 character name for the shapefile
print('3')
#print(columns)


# In[4]:


#make dic for column name replacement using the columns printed in module above
#columns can only have 10 character names'

##quick standardization function to reduce number of column numbers
def standardize(word):
    # delete middle initial with period
    period = word.find(".")
    size = len(word)
    if period >= 9:
        word = word[0:period-1] + word[period+1:size]
        
    #delete slash '/' character
    slash = word.find("/")
    while (slash != -1):
        size = len(word)
        word = word[0:slash] + " " + word[slash+1:size]
        slash = word.find("/")
        
    # delete extra spaces
    size = len(word)
    x = 0
    while (x < size-1):
        if word[x] == " ":
            if word[x+1] == " ":
                word = word[0:x] + word[x+1:size]
                size = len(word)
        x = x + 1
        
    # delete extra spaces
    size = len(word)
    x = 0
    while (x < size-1):
        if word[x] == " ":
            if word[x+1] == " ":
                word = word[0:x] + word[x+1:size]
                size = len(word)
        x = x + 1

    
    # delete middle initial without period
    size = len(word)
    x = 0
    while (x < size-2):
        if word[x] == " ":
            if word[x+2] == " ":
                word = word[0:x] + word[x+2:size]
                size = len(word)
        x = x + 1
    
    # delete the '\n' characters
    newLine = word.find("\n")
    while (newLine != -1):
        size = len(word)
        word = word[0:newLine] + " " + word[newLine+1:size]
        newLine = word.find("\n")
        


    #delete 'And' characters
    And = word.find("And ")
    while (And != -1):
        size = len(word)
        word = word[0:And] + " " + word[And+3:size]
        And = word.find("And ")

    # title case
    word = word.title()
    
    # delete trailing space
    size = len(word)
    if word[size-1] == " ":
        word = word[0:size-1]
    
    return word

count = 0
length = len(prec_elec.columns)
while (count < length):
    name = prec_elec.columns[count]
    print(name)
    new_name = standardize(name)
    prec_elec = prec_elec.rename(columns ={name : new_name})
    print(prec_elec.columns[count])
    count = count + 1


# In[5]:


prec_elec = prec_elec.groupby(axis=1, level=0).sum()
            
print(len(prec_elec.columns))
print(prec_elec.columns.values)


# In[6]:


## need to finish off these renamings
prec_elec_rn = prec_elec.rename(columns = {
        'Votes U.S. Senate Cc Farley': 'NYG18RUSS1',
        'Votes U.S. Senate Chele Chiavacci Farley': 'NYG18RUSS2',
        'Votes U.S. Senate Chele Farley': 'NYG18RUSS3',
        'Votes U.S. Senate Farley': 'NYG18RUSS4',
        'Votes U.S. Senate Gillibrand': 'NYG18DUSS1',
        'Votes U.S. Senate Kirsten E. Gillibra': 'NYG18DUSS2',
        'Votes U.S. Senate Kirsten E. Gillibrand': 'NYG18DUSS3',
        'Votes U.S. Senate Kirsten Gillibrand': 'NYG18DUSS4',
        'Votes U.S. Senate Kirstin E. Gillibrand': 'NYG18DUSS5',
        'Votes U.S. Senate Kristen E. Gillibrand': 'NYG18DUSS6',
    
        'Votes Governor Andrew Cuomo': 'NYG18DGOV1',
        'Votes Governor Andrew Cuomo Kathy Hochul': 'NYG18DGOV2',
        'Votes Governor Cuomo': 'NYG18DGOV3',
        'Votes Governor Hawkins': 'NYG18GGOV1',
        'Votes Governor Howie Hawkins': 'NYG18GGOV2',
        'Votes Governor Howie Hawkins Jia Lee': 'NYG18GGOV3',
        'Votes Governor Howle Hawkins': 'NYG18GGOV4',
        'Votes Governor Larry Sharpe': 'NYG18LGOV1',
        'Votes Governor Larry Sharpe Andrew Hollister': 'NYG18LGOV2',
        'Votes Governor Sharpe': 'NYG18LGOV3',
        'Votes Governor Marc Molinaro': 'NYG18RGOV1',
        'Votes Governor Marc Molinaro Julie Kilian': 'NYG18RGOV2',
        'Votes Governor Marc Molinaro Julie Killian': 'NYG18RGOV3',
        'Votes Governor Marcus Molinaro' : 'NYG18RGOV4',
        'Votes Governor Mark Molinaro': 'NYG18RGOV5',
        'Votes Governor Molinaro': 'NYG18RGOV6',

        'Votes Attorney General Christopher Garvey': 'NYG18LATG1',
        'Votes Attorney General Garvey': 'NYG18LATG2',
        'Votes Attorney General James': 'NYG18DATG1',
        'Votes Attorney General Laetita James':'NYG18DATG2',
        'Votes Attorney General Lenitia James':'NYG18DATG3',
        'Votes Attorney General Letitia James':'NYG18DATG4',
        'Votes Attorney General Keith Wofford':'NYG18RATG1',
        'Votes Attorney General Kieth Wofford':'NYG18RATG2',
        'Votes Attorney General Wofford':'NYG18RATG3',
        'Votes Attorney General Michael Sussman':'NYG18GATG',

        'Votes Comptroller Cruger Gallaudet': 'NYG18LCOM1',
        'Votes Comptroller Gallaudet' : 'NYG18LCOM2',
        'Votes Comptroller Dinapoli' : 'NYG18DCOM1',
        'Votes Comptroller Thomas Di Napoli' : 'NYG18DCOM2',
        'Votes Comptroller Thomas Dinapoli': 'NYG18DCOM3',
        'Votes Comptroller Dunlea': 'NYG18GCOM1',
        'Votes Comptroller Mark Dunlea' : 'NYG18GCOM2',
        'Votes Comptroller Jonathan Trichter': 'NYG18RCOM1',
        'Votes Comptroller Trichter': 'NYG18RCOM2'})
    
prec_elec_rn = prec_elec_rn.fillna(0)
    
prec_elec_rn['NYG18DATG'] = prec_elec_rn['NYG18DATG1'].astype(int) + prec_elec_rn['NYG18DATG2'].astype(int)+ prec_elec_rn['NYG18DATG3'].astype(int)+ prec_elec_rn['NYG18DATG4'].astype(int)
prec_elec_rn['NYG18RATG'] = prec_elec_rn['NYG18RATG1'].astype(int) + prec_elec_rn['NYG18RATG2'].astype(int)+ prec_elec_rn['NYG18RATG3'].astype(int)
prec_elec_rn['NYG18LATG'] = prec_elec_rn['NYG18LATG1'].astype(int) + prec_elec_rn['NYG18LATG2'].astype(int)
prec_elec_rn['NYG18DGOV'] = prec_elec_rn['NYG18DGOV1'].astype(int) + prec_elec_rn['NYG18DGOV2'].astype(int)+ prec_elec_rn['NYG18DGOV3'].astype(int)
prec_elec_rn['NYG18GGOV'] = prec_elec_rn['NYG18GGOV1'].astype(int) + prec_elec_rn['NYG18GGOV2'].astype(int)+ prec_elec_rn['NYG18GGOV3'].astype(int)+ prec_elec_rn['NYG18GGOV4'].astype(int)
prec_elec_rn['NYG18RGOV'] = prec_elec_rn['NYG18RGOV1'].astype(int) + prec_elec_rn['NYG18RGOV2'].astype(int)+ prec_elec_rn['NYG18RGOV3'].astype(int)+ prec_elec_rn['NYG18RGOV4'].astype(int)+ prec_elec_rn['NYG18RGOV5'].astype(int)+ prec_elec_rn['NYG18RGOV6'].astype(int)
prec_elec_rn['NYG18LGOV'] = prec_elec_rn['NYG18LGOV1'].astype(int) + prec_elec_rn['NYG18LGOV2'].astype(int)+ prec_elec_rn['NYG18LGOV3'].astype(int)
prec_elec_rn['NYG18DUSS'] = prec_elec_rn['NYG18DUSS1'].astype(int) + prec_elec_rn['NYG18DUSS2'].astype(int)+ prec_elec_rn['NYG18DUSS3'].astype(int)+ prec_elec_rn['NYG18DUSS4'].astype(int)+ prec_elec_rn['NYG18DUSS5'].astype(int)+ prec_elec_rn['NYG18DUSS6'].astype(int)
prec_elec_rn['NYG18RUSS'] = prec_elec_rn['NYG18RUSS1'].astype(int) + prec_elec_rn['NYG18RUSS2'].astype(int)+ prec_elec_rn['NYG18RUSS3'].astype(int)+ prec_elec_rn['NYG18RUSS4'].astype(int)
prec_elec_rn['NYG18LCOM'] = prec_elec_rn['NYG18LCOM1'].astype(int) + prec_elec_rn['NYG18LCOM2'].astype(int)
prec_elec_rn['NYG18DCOM'] = prec_elec_rn['NYG18DCOM1'].astype(int) + prec_elec_rn['NYG18DCOM2'].astype(int)+ prec_elec_rn['NYG18DCOM3'].astype(int)
prec_elec_rn['NYG18GCOM'] = prec_elec_rn['NYG18GCOM1'].astype(int) + prec_elec_rn['NYG18GCOM2'].astype(int)
prec_elec_rn['NYG18RCOM'] = prec_elec_rn['NYG18RCOM1'].astype(int) + prec_elec_rn['NYG18RCOM2'].astype(int)

prec_elec_rn = prec_elec_rn[[
        'NYG18DATG', 'NYG18RATG', 'NYG18LATG', 'NYG18GATG',
        'NYG18DGOV', 'NYG18RGOV', 'NYG18LGOV', 'NYG18GGOV',
        'NYG18DUSS', 'NYG18RUSS', 
        'NYG18DCOM', 'NYG18RCOM', 'NYG18LCOM', 'NYG18GCOM']]
#this is ready to be matched to precinct names now

prec_elec_rn.to_csv('/Users/laeocrnkovic-rubsamen/Desktop/NY/NY_G18.csv')

######################################################
# MEDSL RESULTS ######################################
######################################################


# In[ ]:




