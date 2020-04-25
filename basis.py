# ~/anaconda3/bin/anaconda-navigator
# NUMPY BASIS

import numpy as np

a = np.array([0, 1, 2, 3])
print(a)
print(type(a))
print("--------")

b = np.array([[1, 2], [2, 3]])
print(b)
print("--------")

# Numpy contains homogeneous type of data

c = np.arange(6) # returns array
print(c)
print(type(c))
print("--------")

d = np.arange(-2, 1, 0.5)
print(d)

e = np.linspace(1, 10, 5) # distribute range in 5 parts
print(e)

print(np.ones([3, 5]))
print("--------")
print(np.zeros([3, 5]))
print("--------")
print(np.eye(6)) # diagonal 2d
print("--------")

# distributing 1d array a in diagonal
f = np.diag(a)
print(f)

print(f.ndim) # number of dimentions
print(f.shape)  # length of each dimention
print(f.size) # number of elements


# ARRAY RESHAPING

g = np.arange(6)
print(g)
print("--------")
print(g.reshape(2, 3))
print("--------")
print(g.reshape(3, 2))

print("--------")
print(f.ravel())  # convering to 1d (flattening)



# Mathematical operations can also be applied on numpy arrays


h = np.linspace(2, 20, 5)
i = np.linspace(1, 10, 5)
print("--------")
print(h)
print("--------")
print(i)
print("--------")
print(h + i)
print("--------")
print(h - i)
print("--------")
print(h * i)
print("--------")
print(h / i)

