#!/usr/bin/env python
# coding: utf-8

# In[3]:


from bs4 import BeautifulSoup


# In[4]:


import requests


# In[ ]:


#For all Types of Restaurent present in Hyderabaad


# In[5]:


page=requests.get("https://www.dineout.co.in/hyderabad-restaurants/trending")
page


# In[6]:


soup=BeautifulSoup(page.content)
soup


# In[ ]:


#First, we will use html tag where we have the first title of the restaurants 


# **Scrapping First Name**

# In[17]:


Title = soup.find('a',class_="restnt-name ellipsis")
Title


# In[18]:


Title.text


# **Scrapping First Location**

# In[9]:


loc =soup.find('div',class_="restnt-loc ellipsis")
loc.text


# **Scrapping First Place Value**

# In[10]:


price=soup.find('div',class_="detail-info")
price.text.split("|")[0]


# **Now Scrapping Multiple Price Of Restaurant**

# In[12]:


# Printing All the price .
price=[]
for i in soup.find_all('div',class_="detail-info"):
    price.append(i.text.split("|")[0])
    
price


# **Now Scrapping Multiple Images Of Restaurant**

# In[13]:


#Printin all the images .
image=[]
for i in soup.find_all("img",class_="no-img"):
    image.append(i.get('data-src'))
    
image


# **Scrapping Multiple Location**

# In[14]:


#Printing All the location.
location=[]
for i in soup.find_all('div',class_="restnt-loc ellipsis"):
    location.append(i.text)
    
location


# In[19]:


# Printing all the Titles.
Title=[]
for i in soup.find_all('a',class_="restnt-name ellipsis"):
    
    Title.append (i.text)
    
Title


# In[21]:


# Priting Length
print(len(Title),len(location),len(price),len(image))


# In[22]:


#Making DataFrame 
import pandas as pd


# In[23]:


df=pd.DataFrame({"Titles":Title,"Location":location,"Price":price,"Image":image})
df


# In[ ]:




