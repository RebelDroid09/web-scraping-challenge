#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Dependencies
from bs4 import BeautifulSoup
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager

import requests
import os
import cssutils
import pandas as pd


# In[3]:


# Setup splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[12]:


#Scraping the mars news website.
marsNewsUrl = 'https://mars.nasa.gov/news/'
browser.visit(marsNewsUrl)


# In[16]:



html = browser.html
soup = BeautifulSoup(html, 'html.parser')
title = ""
text = ""

newsHeadings = soup.find_all('li', class_='slide')

for heading in newsHeadings:
    print(heading)
    title = heading.find("div", { "class" : "content_title" }).getText()
    text = heading.find("div", { "class" : "article_teaser_body" }).getText()
    break


# In[17]:


print(title)
print(text)


# In[18]:


browser.quit()


# In[2]:


#Scraping the mars image website.
# Setup splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)

marsPicUrl = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(marsPicUrl)


# In[7]:


html = browser.html
soup = BeautifulSoup(html, 'html.parser')
title = ""
text = ""

mainPicture = soup.find('div', class_='carousel_items')

article = mainPicture.find("article", { "class" : "carousel_item" })

article_style = article['style']

style = cssutils.parseStyle(article_style)

featured_image_url = style['background-image']
featured_image_url = featured_image_url.replace('url(', '').replace(')', '')

print(featured_image_url)

finalImageUrl = 'https://www.jpl.nasa.gov' + featured_image_url


# In[8]:


browser.quit()


# In[4]:


#Scraping the mars facts.
# Setup splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)

marsPicUrl = 'https://space-facts.com/mars/'
browser.visit(marsPicUrl)


# In[5]:


html = browser.html
soup = BeautifulSoup(html, 'html.parser')

tableFacts = pd.read_html(html)

df = tableFacts[0]
df.head()


# In[6]:


browser.quit()


# In[32]:


#Scraping the mars hemispheres.
# Setup splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)

marsHemisphereUrl = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(marsHemisphereUrl)


# In[36]:


html = browser.html
soup = BeautifulSoup(html, 'html.parser')

hemisphereList = soup.find_all('div', class_='item')
hemisphereDict = []

for hemisphere in hemisphereList:
    
    hemisphereText = hemisphere.find("h3").getText()
    
    browser.links.find_by_partial_text('Hemisphere Enhanced').click()
    
    newHtml = browser.html
    newSoup = BeautifulSoup(newHtml, 'html.parser')
    
    downloadLinks = newSoup.find_all('a')    
            
    for aItem in downloadLinks:
        #print(aItem)
        if aItem.contents[0] == "Sample":
            print(aItem.contents[0])
            hemisphereImageUrl = aItem['href']
            break
    
    #childA = downloadLi.findChildren("a" , recursive=False)
    #hemisphereImageUrl = childA['href']
    
    hemisphereItem = {hemisphereText, hemisphereImageUrl}
    
    hemisphereDict.append(hemisphereItem)
    
    #print(hemisphereDict)


# In[ ]:


browser.quit()

