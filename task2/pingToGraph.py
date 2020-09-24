#!/usr/bin/env python
# coding: utf-8

# In[34]:


import os 
filename = 'ping_out.txt'
lines = open(filename).readlines()

time = []
for line in lines[1:-4]: 
    t = line.split(' ')
    time.append(float(t[7].split('=')[1]))
print(time)


# In[35]:


import matplotlib.pyplot as plt

plt.plot(time)
plt.show


# In[ ]:




