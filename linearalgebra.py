import numpy as np
a = np.array([[2,4,6],[2,1,2]])
print(a)

b = np.array([[1,2],[3,1],[5,1]])
print(b)

c = np.matmul(b,a)
print(c)

d = np.linalg.det(c)
print(d)

e = np.max(c)
print(e)

f = np.min(c)
print(f)

g = np.max(c,axis = 1)
print(g)

h = np.sum(c,axis = 0)
print(h)

i = c.reshape(1,9)
print(i)

arr1 = np.array([1,2,3,4])
arr2 = np.array([2,3,4,5] )
g = np.vstack([arr1, arr2])
print(g)