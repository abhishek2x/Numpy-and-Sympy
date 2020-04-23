#!/usr/bin/env python
# coding: utf-8

# In[2]:


from sympy import *


# In[4]:


a = Rational(1, 3)


# In[7]:


a


# In[9]:


a*2


# In[11]:


type(a)


# In[12]:


b = 1/3
b


# In[14]:


type(b)


# In[19]:


pi**2


# In[25]:


init_printing(pretty_print=True)


# In[31]:


pi**3


# In[34]:


pi.evalf(20) # first 20 digits


# In[35]:


N(pi)


# In[36]:


N(pi, 3)


# In[39]:


E.evalf(20)


# In[41]:


(pi + E).evalf(30)


# In[43]:


oo > 84983948902384902384


# In[46]:


oo < 999999999999999999999999999999999999999999999999


# In[48]:


oo + 8908


# In[49]:


# Declare Symbolic Variable


# In[51]:


x = Symbol('x')
y = Symbol('y')


# In[54]:


x, y = symbols('x y')


# In[56]:


x + y + x - y


# In[58]:


(x+y)**3


# In[60]:


x, y = symbols('y x')


# In[62]:


x


# In[63]:


y


# In[67]:


get_ipython().run_line_magic('reset', '')


# In[69]:


from sympy import *


# In[71]:


x, y = symbols('x y')


# In[73]:


expand((x + y)**3)


# In[75]:


expand(cos(x+ y))


# In[78]:


expand(cos(x+y), trig=True)


# In[80]:


simplify((x + x*y)/x)


# In[82]:


# Generating series


# In[87]:


expr = Sum(1/((x**2) + 2*x), (x, 1, 10))
expr


# In[90]:


expr.doit()


# In[92]:


expr2 = Product(1/((x**2) + 2*x), (x, 1, 10))
expr2


# In[93]:


expr2.doit()
