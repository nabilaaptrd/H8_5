#!/usr/bin/env python
# coding: utf-8

# In[4]:


get_ipython().system('jupyter nbconvert --to script mod.ipynb')


# In[14]:


s="Hacktiv8-PTP Python For Data Science"
a=[100, 200, 300]
print('a= ', a)

def foo(arg):
    print(f'arg={arg}')
    
class Foo:
    pass

if(__name__=='__main__'):
    print(s)
    print(a)
    foo('quux')
    x=Foo()
    print(x)


# In[ ]:




