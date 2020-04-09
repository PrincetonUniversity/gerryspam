from selenium import webdriver

"""
scrape census partership files for all of the counties in a state, grab the VTDs, and concat them all together

helpful resource - https://towardsdatascience.com/controlling-the-web-with-python-6fceb22c5f08 

first, download a chrome web-driver that corresponds with your version of chrome from https://chromedriver.chromium.org/downloads 
put it in the directory from which you're running this script

if this stops working, can check census.gov/robots.txt to see what they're blocking 
"""

driver = webdriver.Chrome('./chromedriver')

# open browser window
partnership_url = 'https://www.census.gov/geo/partnerships/pvs/partnership16v1/st34_nj.html'
driver.get(partnership_url)

county_tags = each.find_elements_by_tag_name('td')
n_counties = len(county_tags)
n_cycles = int(n_counties / 5) + (n_counties % 5 > 0)

def get_five_counties(n_counties):
    for county in 

# grab the county buttons from the id 
county1 = driver.find_element_by_id('county1')
county1.click()
 
county2 = driver.find_element_by_id('county2')
county2.click()

# click submit button
submit_button = driver.find_elements_by_xpath('//*[@id="middle-column"]/div/form/input[4]')[0]
submit_button.click()

