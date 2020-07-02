#!/usr/bin/env python
# coding: utf-8

# ## 1.Write a python program to create a tuple

# In[1]:


tuplex = 5, 10, 15, 20, 25
print(tuplex)


# ## 2.Write a python program to create a tuple with different data types

# In[2]:


tuplex = ("tuple", False, 3.2, 1)
print(tuplex)


# ## 3.Write a python program to convert a tuple to a string

# In[3]:


tup = ('e', 'x', 'e', 'r', 'c', 'i', 's', 'e', 's')
str =  ''.join(tup)
print(str)


# ## 4.Write a python program to slice a tuple

# In[5]:


tuplex = tuple("HELLO WORLD")
print(tuplex)
_slice = tuplex[2:9:2]
print(_slice)
_slice = tuplex[::4]
print(_slice)
_slice = tuplex[9:2:-4]
print(_slice)


# ## 5.Write a python program to find length of a tuple

# In[6]:


tuplex = tuple("Python")
print(tuplex)
print(len(tuplex))


# ## 6.Write a python program to convert a tuple to a dictionary

# In[7]:


tuplex = ((2, "w"),(3, "r"))
print(dict((y, x) for x, y in tuplex))


# ## 7.Write a python program to reverse a tuple

# In[8]:


x = (5, 10, 15, 20)
y = reversed(x)
print(tuple(y))


# ## 8.Write a python program to convert a list of tuples into a dictionary

# In[9]:


l = [("x", 1), ("x", 2), ("x", 3), ("y", 1), ("y", 2), ("z", 1)]
d = {}
for a, b in l:
    d.setdefault(a, []).append(b)
print (d)


# ## 9.Write a python program to convert a list to a tuple

# In[10]:


listx = [5, 10, 7, 4, 15, 3]
print(listx)
tuplex = tuple(listx)
print(tuplex)

