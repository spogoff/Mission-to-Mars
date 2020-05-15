
#import Splinter and BeautifulSoup
from bs4 import BeautifulSoup
from splinter import Browser 
import pandas as pd
import datetime as dt

def scrape_all():

    # Initiate headless driver for deployment
    browser = Browser("chrome", executable_path="chromedriver", headless=True)
    news_title, news_paragraph = mars_news(browser)
    # img_url, title = mars_hemisphere(browser)

    #Create a data dictionary
    data = {
        'news_title': news_title,
        'news_paragraph': news_paragraph,
        'featured_image': featured_image(browser),
        'facts': mars_facts(),
        'last_modified':dt.datetime.now()
        # 'img_url': img_url,
        # 'title' : title
    }

    #End the WebDriver and return the scraped data
    browser.quit()
    return data


def mars_news(browser):

    #set the url and visit it by sprinter
    url = 'https://mars.nasa.gov/news'
    browser.visit(url)
    browser.is_element_present_by_css('ul.item_list li.slide', wait_time = 1)


    # set and parse the html object 
    html = browser.html
    news_soup = BeautifulSoup(html, 'html.parser')

        
    # Add try/except for error handling
    try:
        slide_elem = news_soup.select_one('ul.item_list li.slide')
        # Use the parent element to find the first `a` tag and save it as `news_title`
        news_title = slide_elem.find('div', class_ = 'content_title').get_text()
        # Use the parent element to find the paragraph text
        news_p = slide_elem.find("div", class_="article_teaser_body").get_text()

    except AttributeError:
        return None, None

    #set the parent elemenet 
    slide_elem.find("div", class_='content_title')

    slide_elem.find("div", class_='article_teaser_body')

    return news_title, news_p

# "### Featured Images"

# Visit URL

def featured_image(browser):

    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)  


    full_image_elem = browser.find_by_id('full_image')
    full_image_elem.click()


    # Find the more info button and click that
    browser.is_element_present_by_text('more info', wait_time=1)
    more_info_elem = browser.find_link_by_partial_text('more info')
    more_info_elem.click()


    # Parse the resulting html with soup
    html= browser.html
    img_soup = BeautifulSoup(html, 'html.parser')


    try:
        # Find the relative image url
        img_url_rel = img_soup.select_one('figure.lede a img').get('src')
        img_url_rel

    except AttributeError:
        return None 
    


    # Use the base URL to create an absolute URL
    img_url = f'https://www.jpl.nasa.gov{img_url_rel}'
    
    return img_url

def mars_facts():

    try:
     
        #read html and turn to daraframe
        df = pd.read_html('https://space-facts.com/mars/')[0]

    except BaseException:
        return None

    # Assign columns and set index of dataframe
    df.columns = ['description','value']
    df.set_index('description',inplace=True)
    df

    # Convert dataframe into HTML format, add bootstrap
    return df.to_html()



# def mars_hemisphere(browser):
#     #set the url and visit it by sprinter
#     url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
#     browser.visit(url)
    
#     # set and parse the html object 
#     html = browser.html
#     hemisphere_soup = BeautifulSoup(html, 'html.parser')

#     try:
        
#         # find all 4 cases of hemisphere 
#         hemisphere_elems = hemisphere_soup.find_all('h3')

#     except AttributeError as e:
#         print(e)

#     #iterate through hemisphere_elems
#     for hemisphere_elem in hemisphere_elems:
#         title = hemisphere_elem.text()
#         hemisphere_elem.click()
#         image_elem = browser.find_by_id('wide-image-toggle')
#         image_elem.click()
#         image_url_rel = hemisphere_elem.find('img', class_="wide_image").get('src')
#         image_url = f'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars{image_url_rel}'
#         return title, image_url

    


if __name__ == "__main__":
    # If running as script, print scraped data
    print(scrape_all())






