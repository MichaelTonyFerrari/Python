
# coding: utf-8

# ### Python module/package imports for this chapter

# In[7]:

import math, json, collections, itertools


# In[10]:

import numpy as np
import matplotlib.pyplot as pp
get_ipython().magic('matplotlib inline')


# In[9]:

from mpl_toolkits.basemap import Basemap
import geopy


# ## Comparing C and Python: computing the digits of pi

# Leibniz series: $\pi/4 = 1 - \frac{1}{3} + \frac{1}{5} - \frac{1}{7} + \cdots = \sum_{k=0} \frac{(-1)^k}{(2k+1)}$

# In[1]:

get_ipython().run_cell_magic('file', 'pi.c', '\n#include <math.h>\n#include <stdio.h>\n\nint main(int argc,char **argv) {\n    int k;\n    double acc = 0.0;\n    \n    for(k=0;k<10000;k++) {\n        acc = acc + pow(-1,k)/(2*k+1);\n    }\n    \n    acc = 4 * acc;\n    \n    printf("pi: %.15f\\n",acc);\n    \n    return 0;\n}')


# In[6]:


acc = 0.0;
    
for k in range(10000):
    acc = acc + pow(-1, k)/(2*k+1)
    
acc = 4 * acc

print("pi:",acc)



# In[7]:

#same as for loop, one line :) vs C  
4*sum(pow(-1, k)/(2*k+1) for k in range(10000))


# In[ ]:



