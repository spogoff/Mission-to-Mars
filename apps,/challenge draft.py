#import Splinter and BeautifulSoup
from bs4 import BeautifulSoup
from splinter import Browser 
import pandas as pd
import datetime as dt

def mars_hemisphere(browser):
    #set the url and visit it by sprinter
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)
    
    # set and parse the html object 
    html = browser.html
    hemisphere_soup = BeautifulSoup(html, 'html.parser')

    # find all 4 cases of hemisphere 
    hemisphere_elems = hemisphere_soup.find_all('h3')
    print(hemisphere_elems)
    # for hemisphere_elem in hemisphere_elems:
    #     hemisphere_title = hemisphere_elem.text()
    #     hemisphere_elem.cli
    #     ck()
    #     full_image_elem = browser.find_by_id('splashy')
    #     full_image_elem.click()
    #     hemisphere_url = hemisphere_elem
    #     high_res_elem = 
    #     return hemisphere_title 