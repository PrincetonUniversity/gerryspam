#################################
#            CLEANING          #
################################
python3 fetch_census.py # first clean census block-level data
python3 clean.py # prepare precinct-level data, create 'mo_prec_labeled_nopop.shp' (until line 63)

# activate virtual environment to label census blocks with precincts
# run the script WITHIN 'gerryspam/General' (move script there)
source areal_ve/bin/activate
python3 label_blocks_with_prec.py

python3 clean.py # merge census blocks and precincts (line 84-100)

#################################
#            SAMPLING           #
################################
# Amendment 3 test run 
python3 sampling.py "state_house" 0.01 1000
# Amendment 3 actual run 
python3 sampling.py "state_senate" 0.01 100000

# Baseline test run 
python3 sampling.py "state_house" 0.01 1000
# Baseline actual run 
python3 sampling.py "state_senate" 0.01 100000
