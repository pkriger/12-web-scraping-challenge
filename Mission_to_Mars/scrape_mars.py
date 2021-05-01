#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Dependencies
from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

def scrape():
    # # NASA Mars News
    mars_data = {}
    # In[164]:


    # URL of page to be scraped
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)


    # In[165]:


    url = "https://redplanetscience.com/"
    browser.visit(url)


    # In[166]:


    # Retrieve page with the requests module

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    news_title = soup.find('div', class_='content_title')
    news_p = soup.find('div', class_='article_teaser_body')
        
    print(news_title.text)
    print(news_p.text)


    # # JPL Mars Space Images - Featured Image

    # In[28]:


    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
    url = 'https://spaceimages-mars.com'
    browser.visit(url)   


    # In[6]:


    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    div = soup.find('div', class_="floating_text_area")

    link = div.find('a')
    href = link['href']

    featured_image_url= f"{url}/{href}"
    print(featured_image_url)


    # # Mars Facts
    # 
    # Visit the Mars Facts webpage here and use Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.
    # 
    # Use Pandas to convert the data to a HTML table string.

    # In[7]:


    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
    url = 'https://galaxyfacts-mars.com/'
    browser.visit(url)   


    # In[8]:


    tables = pd.read_html(url)


    # In[18]:


    mars_facts_df= tables[0]
    mars_facts_df.columns = [['Category', 'Mars Value', 'Earth Value']]
    del mars_facts_df['Earth Value']
    mars_facts_df


    # In[19]:


    html_table = mars_facts_df.to_html()
    html_table


    # In[156]:


    html_table_string=html_table.replace('\n', '')


    # # Mars Hemispheres
    # 
    # Visit the astrogeology site here to obtain high resolution images for each of Mar's hemispheres.
    # 
    # You will need to click each of the links to the hemispheres in order to find the image url to the full resolution image.
    # 
    # Save both the image url string for the full resolution hemisphere image, and the Hemisphere title containing the hemisphere name. Use a Python dictionary to store the data using the keys img_url and title.
    # 
    # Append the dictionary with the image url string and the hemisphere title to a list. This list will contain one dictionary for each hemisphere.

    # In[167]:


    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
    url = 'https://marshemispheres.com/'
    browser.visit(url)  


    # In[80]:


    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    browser.links.find_by_partial_text('Hemisphere').click()


    # In[180]:


    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')    
    hemispheres= soup.find_all('div', class_='collapsible results')
    items = soup.find_all('div', class_='item')
    h_titles = []
    url_things=[]
    #hemisphere_image_urls = []

    for item in items:
        #h_titles=item.find('h3').text
        h3=item.find('h3').text
        h_titles.append(h3)
        print(h3)
        try:
            browser.links.find_by_partial_text(h3).click()
            html = browser.html
            soup = BeautifulSoup(html, 'html.parser')
            div = soup.find('div', class_="downloads")
            image = div.find('a')
            href = image['href']
            image_url= f"{url}{href}"
            url_things.append(image_url)
            print(image_url)
            #hemisphere_image_urls.append({'title': h_title, 'img_url': image_url})
            browser.back()
        except:
            print('nope')







