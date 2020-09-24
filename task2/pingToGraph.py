#!/usr/bin/env python
# coding: utf-8

# In[7]:


import os 
filename = 'ping_out.txt'
lines = open(filename).readlines()

time = []
for line in lines[1:-4]: 
    t = line.split(' ')
    time.append(float(t[7].split('=')[1]))
print(time)


# In[19]:


import matplotlib.pyplot as plt

plt.plot(time)
plt.title('Distribution of network delays')
plt.ylabel('Time')
plt.xlabel('Amount')
#plt.show()
plt.savefig('img.png', dpi=300)


# In[ ]:




