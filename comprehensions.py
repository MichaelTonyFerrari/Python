
# coding: utf-8

# ### Python module/package imports for this chapter

# In[26]:


import math, json, collections, itertools


# In[58]:


import numpy as np
import matplotlib.pyplot as pp
get_ipython().magic('matplotlib inline')


# In[59]:


import matplotlib 
print (matplotlib.__file__)

import mpl_toolkits.mplot3d
mpl_toolkits.mplot3d.__file__


# In[60]:


from mpl_toolkits.basemap import Basemap
import geopy


# ### Code and data needed from previous videos

# List of olympic cities and years:

# In[61]:


cities = []
years = []

for game in open('games.txt','r'):
    words = game.split()
    
    city = ' '.join(words[:-1])
    year = words[-1].strip('()')

    cities.append(city)
    years.append(year)


# Geolocated olympic-city coordinates (from a JSON file):

# In[31]:


coordinates_by_city = json.load(open('coords.json','r'))
coordinates_by_city


# ## Comprehensions and generators

# In[32]:


results = []

for city, year in zip(cities, years):
    if int(year) > 1945:
        results.append(city + ': ' + year)


# In[33]:


results[:10]


# In[34]:


results = [city + ': ' + year for city,year in zip(cities, years) if int(year) > 1945]


# In[35]:


results[:10]


# In[36]:


cities_by_year = {year: city for city, year in zip(cities, years)}


# In[37]:


cities_by_year


# In[38]:


#set compreshension 
cities_after_1930 = {city for year,city in cities_by_year.items() if int(year) > 1930}


# In[39]:


cities_after_1930


# In[44]:


pp.figure(figsize(8,8))

world = Basemap(projection = 'ortho', lat_0=75, lon_0=0)

world.drawcoastlines(linewidth=.25)
world.drawcountries(linewidth=.25)

for year,city in cities_by_year.items():
    x,y = world(coordinates_by_city[city])
    
    world.plot(x,y,'r.')
    pp.text(x,y,year,fontsize=8, ha='center',va='bottom',color='navy')


# In[45]:


even = (i for i in range(20) if i%2 ==0)


# In[46]:


even


# In[47]:


even.__next__()


# In[48]:


even.__next__()


# In[49]:


even = (i for i in range(20) if i%2 ==0)


# In[50]:


sum(even)


# In[51]:


def fibo():
    f1, f2 = 0,1 
    
    while True:
        yield f2
        f1, f2=f2, f1+f2


# In[52]:


f = fibo()


# In[53]:


[next(f) for i in range(20)]


# In[ ]:




