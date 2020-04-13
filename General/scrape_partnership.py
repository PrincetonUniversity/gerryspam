from selenium import webdriver
from shutil import unpack_archive
from pathlib import Path

"""
scrape census partership files for all of the counties in a state, grab the VTDs, and concat them all together

helpful resource - https://towardsdatascience.com/controlling-the-web-with-python-6fceb22c5f08 

first, download a chrome web-driver that corresponds with your version of chrome from https://chromedriver.chromium.org/downloads 
put it in the directory from which you're running this script

if this stops working, can check census.gov/robots.txt to see what they're blocking 
"""

## tried to set default download to a specific path; couldn't get it working
# options = webdriver.ChromeOptions() 
# options.add_argument("download.default_directory=/Users/hopecj/projects/gerryspam/NJ/dat/partnership-2016")
# driver = webdriver.Chrome('./chromedriver', options=options)

driver = webdriver.Chrome('./chromedriver')

# open browser window
# replace this with the url of the year/state you want to download 
partnership_url = 'https://www.census.gov/geo/partnerships/pvs/partnership16v1/st34_nj.html'
driver.get(partnership_url)

county_tags = driver.find_elements_by_tag_name('td')
n_counties = len(county_tags)
print("number of counties total is:", n_counties)

# need to add some type of wait here
start_index = 1
while (start_index < n_counties+1):
    county_str = 'county' + str(start_index)
    county_box = driver.find_element_by_id(county_str)
    county_box.click()
    submit_button = driver.find_elements_by_xpath('//*[@id="middle-column"]/div/form/input[4]')[0]
    submit_button.click()
    county_box.click() # de-select it
    start_index += 1

# extract all the zip files 
# will like need to the relative path in 'p'
p = Path.home() / "projects" / "gerryspam" / "NJ" / "dat" / "partnership-2016"
all = p / 'unzipped' / 'extracted' / 'precincts'
all.mkdir(exist_ok=True, parents=True)

up = p / 'unzipped'
for zip in p.glob('*.zip'):
    unpack_archive(str(zip), extract_dir= up) # first unzip - each zip has two zipped files in it!

ex = up / 'extracted'
for zip in up.glob('*.zip'):
    unpack_archive(str(zip), extract_dir= ex) # second unzip

