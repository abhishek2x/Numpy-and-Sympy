
# NUMPY STATISTICS

import numpy as np

a = np.array([[0, 1], [2, 3]])
print(a)
print("Sum = ", np.sum(a))

print(np.sum(a, axis=0)) # sum of each columns
print(np.sum(a, axis=1)) # sum of each row

print(np.min(a))
print(np.max(a))
print(np.mean(a))
print(np.median(a))
print(np.var(a)) # variance
print(np.std(a)) # standard deviation

# LINEAR ALGRBRA
print("=====================================")

print(np.transpose(a))
print(np.linalg.inv(a)) # inverse

b = ([[5], [7]])
print(a)
print(b)

# ax = b, find x
x = np.linalg.solve(a, b)
print(x)

# determinant
print(np.linalg.det(a))
print(np.diag(a))
print(np.trace(a))

# RANDOM NUMBER GENERATORS

print(np.random.normal(85, 10, size=(5, 5)))

a = list(range(5))
print(a)
print(np.random.permutation(a))
print(np.random.permutation(a))
print(np.random.permutation(a))
print(a)
np.random.shuffle(a) # actually shuffles a
print(a)


# SORTING

c = np.random.randn(5)
print(c)
c.sort()
print(c)

# Sorting can also be done by axis

a = np.r_[-3, -4, 1:4]
print(a)
print(np.c_[a])

# Numpy supperts Broadcasting