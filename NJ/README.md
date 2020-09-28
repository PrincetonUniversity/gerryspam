# New Jersey 2016 Election Shapefile 

This shapefile comes from the Census Partnership file program and was matched to 2016 general election results by the Princeton Gerrymandering Project. 

## Metadata

* `county_nam`: County name
* `STATEFP`: State FIPS code
* `COUNTYFP`: County FIPS code 
* `countynam`: County name
* `precinct`: Precinct name
* `G16DPRS`: Democratic votes President
* `G16RPRS`: Republican votes President
* `G16DHOR`: Democratic votes US House
* `G16RHOR`: Republican votes US House
* `geometry`: Geometry

## Processing

All processing scripts are available in [this](https://github.com/PrincetonUniversity/gerryspam/tree/master/NJ) public GitHub repository. To re-run the processing scripts, you will need to change the relative paths to all data files.

The following processing scripts were used to match a precinct-level shapefile of New Jersey with precinct-level election results from the 2016 election:
1. Transform raw election results: https://github.com/PrincetonUniversity/gerryspam/blob/master/NJ/Process_OpenElex.py 
2. Scrape county-specific shapefiles and build a state-wide shapefile: https://github.com/PrincetonUniversity/gerryspam/blob/master/General/scrape_partnership.py 
3. Clean election precinct names: https://github.com/PrincetonUniversity/gerryspam/blob/master/NJ/elec-name-edits.py 
4. Clean shapefile precinct names: https://github.com/PrincetonUniversity/gerryspam/blob/master/NJ/shp-name-edits.py 
5. Merge clean shapefile and clean election results: https://github.com/PrincetonUniversity/gerryspam/blob/master/NJ/merge_shp_elec.py 

## Sources
Our shapefile was sourced from the Census Bureau's Partnership Files (https://www.census.gov/geo/partnerships/pvs/partnership16v1/st34_nj.html).

Election results for 2016 were downloaded from [OpenElections](https://github.com/openelections/openelections-data-nj/blob/master/2016/20161108__nj__general__precinct.csv) on April 24th, named `20161108__nj__general__precinct.csv`. 

Election results for 2016 were downloaded from MEDSL by way of the Harvard Dataverse [(link)](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/PSKDUJ) on April 1st, 2020. Only Hudson County election results were used from the MEDSL data.

Note that our matched precincts are missing two counties: Burlington and Gloucester. Precinct-level election results were not available for these counties. 

