#!/usr/bin/env python
# coding: utf-8

# In[2]:


from sympy import *
from sympy.stats import *
init_printing(pretty_print=True)


# In[5]:


X, Y = Die('X', 6), Die('Y', 6)
density(X).dict


# In[8]:


density(X).set


# In[10]:


sample(X) # Rolling die X


# In[11]:


sample(Y) # Rolling die Y


# In[13]:


P(X > 3)


# In[14]:


E(X + Y) # Expection function


# In[16]:


variance(X + Y) # Expection function


# In[17]:


C = Coin('C')
density(C).dict


# In[18]:


Z = Normal('Z', 0, 1) # Represents Curve
P(Z > 1).evalf()


# In[19]:


V = Bernoulli('V', 0.75) # bar type
density(V).dict


# In[20]:


sample(V)


# In[21]:


sample(V)


# In[22]:


sample(V)


# In[23]:


sample(V)


# # Complex Numbers
# 

# In[24]:


I


# In[25]:


I**2


# In[40]:


x = Symbol('x')
solve(x**2 + 1, x)


# In[44]:


z = 4 + 3*I
z


# In[45]:


re(z)


# In[48]:


im(z)


# In[47]:


Abs(z)


# In[50]:


conjugate(z)


# In[ ]:



