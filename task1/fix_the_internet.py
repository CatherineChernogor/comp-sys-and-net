#!/usr/bin/env python
# coding: utf-8

# In[6]:


import os 

with open('data2.txt') as file:

    v_amount = file.readline()

    edge_lst = [ edge.rstrip().split() for edge in file.readlines()]
#print(v_amount, edge_lst)


# In[7]:


new_e = []
for e in edge_lst:
    lst = []
    for v in e:
        lst.append(int(v))
    new_e.append(lst)
edge_lst = new_e


# In[8]:


g= {i: set() for i in range(1,int(v_amount)+1)}

for edge in edge_lst:
    v0, v1 = edge[0], edge[1]
    g.get(v0).add(v1)
    g.get(v1).add(v0)


# In[9]:


def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    for nxt in graph[start] - visited:
        dfs(graph, nxt, visited)
    return visited


# In[10]:


def get_ind(lst, val):
    for i in range(len(lst)):
        if lst[i]==val:
            return i


# In[11]:


not_visited = [ i for i in range(1, int(v_amount)+1)]
components = 0

while not not not_visited:
    visited_v = list(dfs(g, not_visited[0]))
    for v in visited_v:
        index = get_ind(not_visited, v)
        not_visited.pop(index)
    components+=1
print('%d links is required ' % (components-1))


# In[71]:


#ping - i 0.2 ya.ru > ping
#look for gawk

