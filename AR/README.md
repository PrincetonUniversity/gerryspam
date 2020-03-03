__Election results__

On November 7th, downloaded raw data from here: https://github.com/openelections/openelections-data-ar/tree/master/2018

Used the file https://github.com/PrincetonUniversity/gerryspam/blob/master/AR/elec_candidates_to_elec_prec_AR_G18.py to transform the file to AR_G18.csv 

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
- Pope County: Removed '#' from precinct names
- Stone County: Combined results from "Ben 1" and "Ben 2" precincts into "Ben" precinct. 
- Washington County: Removed first four characters from precinct names


__Shapefiles__

On October 16 2019, downloaded from here: http://gis.arkansas.gov/?product=election-precincts

All changes made to precinct names recorded here: https://github.com/PrincetonUniversity/gerryspam/blob/master/AR/processing_scraps_AR.py