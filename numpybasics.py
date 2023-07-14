import numpy as np
a = np.array([[1,2,3,5],[3,4,6,4]]) #2darray
print(a)

a.ndim
a.shape

a[1,2]
a[1,:]
a[1,1:-1]

b = np.array([[[1,2],[3,4]],[[4,5],[6,7]]]) #3darray
print(b)
b.shape
b.ndim
b[0,1,0]

b[:,:,0] = [[5,5],[5,5]]
print(b)

c = np.zeros([2,3,3]) #zerosfuncfor multiple dimension zero arrays
print(c)

d = np.ones([2,3,1])
print(d)

e = np.full([2,4], 99)
print(e)

f = np.full_like(a,55)
print(f)

g = np.random.rand(2,4)
print(g)

h = np.random.randint(5, size = (4,5))
print(h)

i = np.identity(5)
print(i)

aray = [[1,2,3]]
f = np.repeat(aray,3,axis = 0)
print(f)


#excercise in video

g = np.ones([5,5])
print(g)

zeroar = np.zeros((3,3))
print(zeroar)
zeroar[1,1] = 9
print(zeroar)

g[1:-1,1:-1] = zeroar
print(g)