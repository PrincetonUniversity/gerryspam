import sys
sys.path.append('~/gerryspam/General') # will probably need to change the relative path; set it to gerryspam/General
import areal_interpolation as ai
import geopandas as gpd
import maup
import matplotlib

small = gpd.read_file('/Volumes/GoogleDrive/Shared drives/princeton_gerrymandering_project/OpenPrecincts/States for site/Michigan/Raw Precincts/2018_Voting_Precincts (1)/2018_Voting_Precincts.shp')
#nm = gpd.read_file('/Volumes/GoogleDrive/Shared drives/princeton_gerrymandering_project/mapping/NC/Shapefiles/precincts/2016/nc_2016.shp')
large = gpd.read_file('/Volumes/GoogleDrive/Shared drives/princeton_gerrymandering_project/mapping/MI/Counties/Counties_v17a/Counties_v17a.shp')
#nm = gpd.read_file('/Users/hwheelen/Desktop/VA/VA_Leg_Enacted_BH.shp’)

small = small.to_crs(large.crs)
# =============================================================================
# for col in cols:
#     small[col] = small[col].astype(int)
# =============================================================================
              
              

#small = agg.rename(columns = {'Dist_Name':'SD'})


agg = ai.aggregate(small, large, target_columns=['FIPSCODE','NAME'])[0] # this takes a while
agg = agg[['OBJECTID', 'ShapeSTAre', 'ShapeSTLen', 'FIPSCODE',
       'NAME', 'PRECINCTID', 'ELECTIONYE',
       'COUNTYFIPS', 'MCDFIPS', 'WARD', 'PRECINCT', 'geometry',]]

agg.to_file('/Volumes/GoogleDrive/Shared drives/princeton_gerrymandering_project/OpenPrecincts/States for site/Michigan/Raw Precincts/MIprec2018.shp')

agg_eq = agg[['GEOID10','VTDI10','ABCD_Distr']]

agg_eq.to_csv('/Volumes/GoogleDrive/Shared drives/princeton_gerrymandering_project/OpenPrecincts/States for site/Nevada/Shapefiles/AB_Maps/ABCD_vtd_eq.csv')

agg_final = agg[['county','locality','NAMELSAD']]
agg_final = agg_final.rename(columns={'NAMELSAD':'precinct'})

agg_final.to_csv('/Volumes/GoogleDrive/Team Drives/princeton_gerrymandering_project/mapping/PA/Pennsylvania/VTDs_Oct17/PA_VTD_Names.shp')




# =============================================================================
# from shapely.validation import explain_validity
# for row,index in census.iterrows():
#     print(explain_validity(prec.geometry[row]))
#     if explain_validity(prec.geometry[row]) != 'Valid Geometry':
#         
#         print(row, explain_validity(prec.geometry[row]))
# =============================================================================


