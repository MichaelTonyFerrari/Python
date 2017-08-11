
# coding: utf-8

# ### Python module/package imports for this chapter

# In[1]:

import math, json, collections, itertools


# In[19]:

import numpy as np
import matplotlib.pyplot as pp
from IPython import get_ipython

get_ipython().magic('matplotlib inline')


# In[22]:

from mpl_toolkits.basemap import Basemap
import geopy


# ## Mastering Python loops

# In[3]:

for n in [1,1,2,3,5,8,13,21,34,55]:
    print(n)


# In[4]:

for l in "Fibonacci":
    print(l)


# In[8]:

it = iter("Fib")
print(it.__next__())
print(it.__next__())
print(it.__next__())


# In[9]:

for game in open('games.txt', 'r'):
    print(game, end='')


# In[10]:

for game in open('games.txt', 'r'):
    city = game.split()[0]
    year = game.split()[1]
    
    print(game, end='')
    


# In[11]:

for game in open('games.txt', 'r'):
    words = game.split()
    
    city= ' '.join(words[:-1])
    year = words[-1].strip('()')
    
    print(city, year)
    


# In[12]:

cities, years = [], []

for game in open('games.txt', 'r'):
    words = game.split()
    
    city= ' '.join(words[:-1])
    year = words[-1].strip('()')
    
    cities.append(city)
    years.append(year)
    


# In[16]:

geolocator = geopy.geocoders.Nominatim()

locations = {}
for city in cities:
    print("Locating", city)
    locations[city] = geolocator.geoecode(city.split('/')[0])


# In[17]:

locations["Paris"]


# In[20]:

pp.figure(figsize=(10, 5))

world = Basemap()
world.drawcoastlines(linewidth=.25)
world.drawcountries(linewidth=.25)


# In[23]:

pp.figure(figsize=(10, 5))

world = Basemap()
world.drawcoastlines(linewidth=.25)
world.drawcountries(linewidth=.25)

for city,pos in locations.items():
    world.plot(pos.longitude, pos.latitude,'r.',markersize=10,latlon=True)


# In[24]:

#rome in wrong locations after checking locations 
locations


# In[25]:

#give position manually
locations['Rome'] = geolocator.geocode('Rome, Italy')


# In[26]:

locations['Rome']


# In[27]:

locations['Athens'] = geolocator.geocode('Athens, Greece')


# In[28]:

pp.figure(figsize=(10, 5))

world = Basemap()
world.drawcoastlines(linewidth=.25)
world.drawcountries(linewidth=.25)
for city,pos in locations.items():
    world.plot(pos.longitude, pos.latitude,'r.',markersize=10,latlon=True)


# In[29]:

for i, city in enumerate(cities[:10]):
    print(i, city)


# In[30]:

for city in enumerate(cities[:10]):
    print(city)


# In[31]:

for city in sorted(cities[:10]):
    print(city)


# In[32]:

#sort by length of city name
for city in sorted(cities[:10],key=len):
    print(city)


# In[33]:

for i,city in enumerate(reversed(cities[:10])):
    print(i,city)


# In[34]:

for year,city in zip(years[:10], cities):
    print(year, city)


# In[ ]:



