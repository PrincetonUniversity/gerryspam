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
# test with only 1,000 iterations 
# 5% population deviation on the state house map
# NB : this doesn't work because the enacted plan apparently isn't within 5% pop. deviation??? strange
python3 sampling.py "state_house" 0.05 1000
python3 sampling.py "state_senate" 0.05 1000


python3 sampling.py "state_senate" 0.05 100000
