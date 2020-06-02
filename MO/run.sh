# testing with only 1,000 iterations 
# 5% population deviation on the state house map
# NB : this doesn't work because the enacted plan apparently isn't within 5% pop. deviation??? strange
python3 sampling.py "state_house" 0.05 1000

python3 sampling.py "state_senate" 0.05 100000
