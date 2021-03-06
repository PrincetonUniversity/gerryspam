# Arkansas 2018 Election Shapefile

This shapefile comes from the Arkansas state government and was matched with 2018 general election results by the Princeton Gerrymandering Project. 

## Metadata

* `county_nam`: County name
* `state_fips`: State FIPS code
* `county_fip`: County FIPS code 
* `precinct`: Precinct name
* `precinct_old`: Pre-edit, pre-merge precinct name (from shapefile)
* `G18DGOV`: General 2018 Governor Democratic Party Candidate
* `G18LGOV`: General 2018 Governor Libertarian Party Candidate
* `G18RGOV`: General 2018 Governor Republican Party Candidate
* `G18DATG`: General 2018 Attorney General Democratic Candidate
* `G18RATG`: General 2018 Attorney General Republican Candidate
* `G18LATG`: General 2018 Attorney General Libertarian Candidate
* `G18DSecS`: General 2018 Secretary of State Democratic Candidate
* `G18LSecS`: General 2018 Secretary of State Libertarian Candidate
* `G18RSecS`: General 2018 Secretary of State Republican Candidate
* `G18RTRES`: General 2018 Treasurer Republican Candidate
* `G18LTRES`: General 2018 Treasurer Libertarian Candidate
* `geometry`: Geometry

## Processing

All processing scripts are available in [this](https://github.com/PrincetonUniversity/gerryspam/tree/master/AR) public GitHub repository. To re-run the processing scripts, you will need to change the relative paths to all data files.

1. Download the raw shapefile and election results from the sources below.
2. Clean the raw election results using [this script](https://github.com/PrincetonUniversity/gerryspam/blob/master/AR/elec_candidates_to_elec_prec_AR_G18.py)
3. Clean shapefiles using [this script](https://github.com/PrincetonUniversity/gerryspam/blob/master/AR/run.sh)
4. In QGIS, merge together all of the cleaned shapefiles (ar18.shp and one-off counties)
5. Merge cleaned election results and final shapefile using [this script](https://github.com/PrincetonUniversity/gerryspam/blob/master/AR/final_merge.py)


## Sources

__Election results__

On November 7th, downloaded raw data from here: https://github.com/openelections/openelections-data-ar/tree/master/2018

Changes: 
- Boone County: 
    - Combined votes from "District 1.1" and "District 1.2"
    - Combined "District 10.1" and "District 10.2 to 10.8"
    - Combined "District 11.1", "District 11.2", 
    and "District 11.3,11.4"
    - Combined "District 12.1 to 12.3" and "District 12.4", combined "District 2.1" and "District 2.2"
    - Combined "District 3.1, 3.3" and "District 3.2"
    - Combined "District 4.1" and "District 4.2"
    - Combined District 5.1", "District 5.2, 5.3, 5.5 to 5.9", and "District 5.4"
    - Combined "District 6.1", "District 6.2, 6.3, 6.5, to 6.8", and "District 6.4" 
    - Combined "District7.1,7.3,7.8", "District 7.2", and "District 7.4 to 7.7"
    - Combined "District 8.1,8.5" and "District 8.2 to 8.4"
    - Combined "District 9.1", "District 9.2 to 9.4,9.6", and "District 9.5"

- Calhoun County: Changed "Watson Addition" to "Tinsman Watson" based off of phone call to county clerk 
- Cleburne County: Removed last three characters from precinct names
- Craighead County: Removed the word "precinct" from precinct names
- Izard County: Added "OXFORD CITY IN BROCKWELL" precinct results to Brockwell precinct. Added "SAGE IN MELBOURNE WARD 4" to Melbourne Ward 4 precinct.
- Jefferson County: Deleted "Absentee" row of votes
- Ouachita County: 
    - Removed the leading zero from precincts "Camden Ward 1" through "Camden Ward 9"
    - Combined "Smackover Ward 1" and "Smackover Ward 2" into "Smackover Ward"
    - Combined "Valley 1" and "Valley 2" into "Valley"
- Phillips County: 
    - Removed "PRECINCT 0004" from election results based on exchange with county clerk
    - Combined results fom "PRECINCT 0005" and "PRECINCT 0006" into "PRECINCT 0005/0006"
- Pope County: Removed '#' from precinct names
- Stone County: Combined results from "Ben 1" and "Ben 2" precincts into "Ben" precinct. 
- Union County: Removed "EARLY VOTING" and "ZZ - PROVISIONAL" rows.
- Washington County: Removed first four characters from precinct names
- White County: 
    - Combined Higginson Wards 1-3 into "Higginson City" precinct. 
    - Deleted Pangburn Ward 3. 
    - Deleted Searcy Ward 1D. 
    - Deleted Searcy Ward 3E. 
    - Deleted Searcy Ward 4B.


__Shapefiles__

On October 16 2019, downloaded state-wide shapefile from here: http://gis.arkansas.gov/?product=election-precincts

All changes made to precinct names recorded in [this script](https://github.com/PrincetonUniversity/gerryspam/blob/master/AR/edit_prec_names.py)

For the counties below, the shapefile precincts did not match with the election precincts. We downloaded the county-specific shapefiles from the Census Partership archive, and cleaned the data using [this script](https://github.com/PrincetonUniversity/gerryspam/blob/master/AR/edit_alt_data_counties.py).

On March 4th 2020, Madison County downloaded from here: https://www.census.gov/geo/partnerships/pvs/partnership18v2/st05_ar.html
- Used "PVS_18_v2_vtd_05087.shp"

On March 4th 2020, Mississippi County downloaded from here: https://www.census.gov/geo/partnerships/pvs/partnership17v2/st05_ar.html 
- Used "PVS_17_v2_vtd_05103.shp" 

On March 11th 2020, Ouachita County downloaded from here: https://www.census.gov/geo/partnerships/pvs/partnership17v2/st05_ar.html 
- Used "PVS_17_v2_vtd_05103.shp" 

On March 12th 2020, Jefferson County downloaded from here: https://www.census.gov/geo/partnerships/pvs/partnership18v2/st05_ar.html
- Used "PVS_18_v2_vtd_05069.shp"

On March 13th 2020, White County downloaded from here: https://www.census.gov/geo/partnerships/pvs/partnership17v2/st05_ar.html
- Used "PVS_17_v2_vtd_05145.shp"

