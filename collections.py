
# coding: utf-8

# ### Python module/package imports for this chapter

# In[30]:


import math, json, collections, itertools


# In[53]:


import numpy as np
import matplotlib.pyplot as pp
get_ipython().magic('matplotlib inline')
get_ipython().magic('pylab')
import pandas as pd


# In[32]:


from mpl_toolkits.basemap import Basemap
import geopy


# ## Beyond lists, dicts, and sets: more powerful collections

# In[33]:


open('goldmedals.txt', 'r').readlines()[:10]


# In[34]:


medal = collections.namedtuple('medal',['year', 'athlete', 'team', 'event'])


# In[35]:


m = medal('1896','Thomas Burke', 'USA', '100m men')


# In[36]:


m


# In[37]:


m.year, m.athlete


# In[38]:


medals =[medal(*line.split('\t'))for line in open('goldmedals.txt', 'r')]


# In[39]:


medals[:5]


# In[40]:


medals =[medal(*line.strip().split('\t'))for line in open('goldmedals.txt', 'r')]


# In[41]:


medals[:5]


# In[42]:


#counting object 
teams = collections.Counter(medal.team for medal in medals)


# In[43]:


teams


# In[44]:


teams.most_common(5)


# In[45]:


def best_by_year(year):
    counts = collections.Counter(medal.team for medal in medals if medal.year == str(year))
    best = counts.most_common(5)
    
    return [b[0] for b in best], [b[1] for b in best]


# In[46]:


best_by_year(1900)


# In[56]:


countries, tally = best_by_year(1900)

pp.figure(figsize=(6,3))

bars = pp.bar(np.arange(5),tally,align='center')
pp.xticks(np.arange(5),countries)


# In[58]:


pp.style.use('ggplot')

colors = pp.cm.Set3(np.linspace(0,1,5))

def plotyear(year):
    countries, tally = best_by_year(year)

    bars = pp.bar(np.arange(5),tally,align='center')
    pp.xticks(np.arange(5),countries)
    
    for bar, color in zip(bars,colors):
        bar.set_color(color)
    
    pp.title(year)


# In[65]:


pp.figure(figsize=(4,6))

pp.subplot(3,1,1); plotyear(2008)
pp.subplot(3,1,2); plotyear(2012)
pp.subplot(3,1,3); plotyear(2016)

pp.tight_layout()


# In[66]:


winners_by_country = {}

for medal in medals:
    if medal.team not in winners_by_country:
        winners_by_country[medal.team] = [medal.athlete]
    else:
        winners_by_country[medal.team].append(medal.athlete)


# In[67]:


winners_by_country['ITA']


# In[68]:


winners_by_country = collections.defaultdict(list)

for medal in medals:
    winners_by_country[medal.team].append(medal.athlete)


# In[69]:


winners_by_country['FRA']


# In[70]:


ordered_winners = collections.OrderedDict()

for medal in medals:
    if medal.team == 'ITA':
        ordered_winners[medal.athlete] = medal.event + ' ' + medal.year


# In[71]:


ordered_winners


# In[72]:


{medal.athlete: medal.event + ' ' + medal.year for medal in medals if medal.team == 'ITA'}


# In[73]:


dq = collections.deque(range(10))


# In[74]:


dq


# In[75]:


for i in range(10,15):
    dq.append(i)
    v = dq.popleft()
    print(dq)


# In[76]:


for i in reversed(range(0,5)):
    dq.appendleft(i)
    v = dq.pop()
    print(dq)


# In[ ]:




