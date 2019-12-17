__Election results__

On November 7th, downloaded raw data from here: https://github.com/openelections/openelections-data-ar/tree/master/2018

Used the file https://github.com/PrincetonUniversity/gerryspam/blob/master/AR/elec_candidates_to_elec_prec_AR_G18.py to transform the file to AR_G18.csv 

Changes: 
- Cleburne County: Removed last three characters from precinct names
- Craighead County: Removed the word "precinct" from precinct names
- Washington County: Remove first four characters from precinct names
- 

__Shapefiles__

On October 16 2019, downloaded from here: http://gis.arkansas.gov/?product=election-precincts

Transformations made to precinct names recorded here: https://github.com/PrincetonUniversity/gerryspam/blob/master/AR/processing_scraps_AR.py

Merges/splits: 
- Stone County: Merged precinct Fifty six into Northwest