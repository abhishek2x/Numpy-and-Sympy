#!/usr/bin/env python
# coding: utf-8

# ## Limit

# In[2]:


from sympy import *


# In[74]:


x, y, z = symbols('x y z')
init_printing(pretty_print=True)


# In[6]:


limit(sin(x)/x, x, 0)


# In[8]:


limit(x, x, oo)


# In[11]:


limit(1/x, x, oo)


# In[14]:


limit(x**x, x, 0)


# # Limit at a Certain Direction

# In[19]:


limit(1/x, x, 0, dir='+')


# In[21]:


limit(1/x, x, 0, dir='-')


# # Differentiation

# In[24]:


diff(sin(x), x)


# In[27]:


diff(sin(2*x), x)


# In[28]:


diff(sin(2*x), x, 2)


# In[29]:


diff(sin(2*x), x, 3)


# # Indefinite Integral

# In[31]:


integrate(6 * x**5, x)


# In[33]:


integrate(sin(x), x)


# In[35]:


integrate(2*x + sinh(x), x)


# # Definit Integrals

# In[37]:


integrate(x**3, (x, -1, 2))


# In[40]:


integrate(cos(x), (x, -pi/2, pi/2))


# # Taylor Series Expansion
# 

# In[42]:


series(ln(x), x, 1, 4)


# # Equation Solution

# In[46]:


solve(x**2-3*x+2, x)


# In[48]:


# system of equations
solve([x+5*y-2, -3*x+6*y-15], [x, y])


# In[50]:


solve(exp(x) + 1, x)


# In[53]:


f = x**4 - 3*x**2 + 1
f


# In[55]:


factor(f)


# In[58]:


f = symbols('f', cls=Function)

f(x)


# In[60]:


f(x).diff(x, x)


# In[62]:


f(x).diff(x, x) + f(x) # ordinary differential equation


# In[64]:


dsolve(f(x).diff(x, x) + f(x), f(x)) #solve ODE


# # Substitution

# In[70]:


expr = x**2 + 2*x + 1
expr


# In[72]:


expr.subs(x, 2)


# In[76]:


expr.subs(x, y+1)


# In[78]:


n, k = symbols('n k', integer=True)


# In[81]:


a = factorial(n)
a


# In[84]:


a.subs(n, 7)


# In[86]:


b = binomial(n, k)


# In[88]:


b


# In[90]:


b.subs([(n, 3), (k, 2)])


# In[93]:


exp = x**3 + 4*x*y - z
exp


# In[95]:


exp.subs([(x, 2), (y, 4), (z, 0)])


# # Converting Strings to Expressions
# 

# In[98]:


str_expr = "x**3 + 4*x*y - z"
expr = sympify(str_expr)
expr


# In[100]:


expr = S(str_expr)
expr
