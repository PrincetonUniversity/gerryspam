import geopandas as gpd
import pandas as pd
import numpy as np

#list states you need data for
states = ['Michigan']

#filepath to country wide 2018 precinct level returns
elec_fp = '/Users/hwheelen/Documents/GitHub/MEDSL/2018-elections-official/precinct_2018.csv'
#load into dataframe
elec_df = pd.read_csv(elec_fp, encoding = "ISO-8859-1")


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
    state_elec = state_df.loc[state_df['office'].isin(state_offices)]
    statewide_offices.append(state_offices)
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
        'votes democrat Attorney General' 
        'votes democrat Governor'
        'votes democrat Governor of Wayne State University'
        'votes democrat Member of the State Board of Education'
        'votes democrat Regent of the University of Michigan'
        'votes democrat Secretary of State' 'votes democrat State House'
        'votes democrat State Senate'
        'votes democrat Trustee of Michigan State University'
 'votes democrat US House' 'votes democrat US Senate'
 'votes green Governor'
 'votes green Member of the State Board of Education'
 'votes green Regent of the University of Michigan'
 'votes green State House' 'votes green State Senate'
 'votes green Trustee of Michigan State University' 'votes green US House'
 'votes green US Senate' 'votes libertarian Attorney General'
 'votes libertarian Governor'
 'votes libertarian Governor of Wayne State University'
 'votes libertarian Member of the State Board of Education'
 'votes libertarian Regent of the University of Michigan'
 'votes libertarian Secretary of State' 'votes libertarian State House'
 'votes libertarian State Senate'
 'votes libertarian Trustee of Michigan State University'
 'votes libertarian US House' 'votes natural law Governor'
 'votes natural law Regent of the University of Michigan'
 'votes natural law Trustee of Michigan State University'
 'votes natural law US Senate'
 'votes no party affiliation Attorney General'
 'votes no party affiliation Governor'
 'votes no party affiliation Justice of Supreme Court'
 'votes no party affiliation State House'
 'votes no party affiliation State Proposal - 18-1: Legislative Initiative: Coalition To Regulate Marijuana Like Alcohol'
 'votes no party affiliation State Proposal - 18-2: Constitutional Amendment: Voters Not Politicians'
 'votes no party affiliation State Proposal - 18-3: Constitutional Amendment: Promote the Vote'
 'votes no party affiliation State Senate'
 'votes no party affiliation Trustee of Michigan State University'
 'votes no party affiliation US House'
 'votes no party affiliation US Senate'
 'votes republican Attorney General' 'votes republican Governor'
 'votes republican Governor of Wayne State University'
 'votes republican Member of the State Board of Education'
 'votes republican Regent of the University of Michigan'
 'votes republican Secretary of State' 'votes republican State House'
 'votes republican State Senate'
 'votes republican Trustee of Michigan State University'
 'votes republican US House' 'votes republican US Senate'
 'votes us taxpayers Attorney General' 'votes us taxpayers Governor'
 'votes us taxpayers Governor of Wayne State University'
 'votes us taxpayers Member of the State Board of Education'
 'votes us taxpayers Regent of the University of Michigan'
 'votes us taxpayers Secretary of State' 'votes us taxpayers State House'
 'votes us taxpayers State Senate'
 'votes us taxpayers Trustee of Michigan State University'
 'votes us taxpayers US House' 'votes us taxpayers US Senate'
 'votes working class Member of the State Board of Education'
 'votes working class State Senate' 'votes working class US House'})
    

#get rid of other columns and save
#this is ready to be matched to precinct names now
prec_elec_rn = prec_elec_rn.fillna(0)
#prec_elec_rn['G18OGOV'] = prec_elec_rn['G18OGOV1'].astype(int) + prec_elec_rn['G18OGOV2'].astype(int)+ prec_elec_rn['G18OGOV3'].astype(int)

#this is ready to be matched to precinct names now

prec_elec_rn.to_csv('/Volumes/GoogleDrive/Shared drives/princeton_gerrymandering_project/mapping/MI/Election Results/MI_G18_MIT.csv')