#!/usr/bin/env python
# coding: utf-8

# In[5]:


get_ipython().system('jupyter nbconvert --to script fact.ipynb')


# In[1]:


def fact(n):
    return 1 if n == 1 else n * fact(n-1)

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        print(fact(int(sys.argv[1])))

