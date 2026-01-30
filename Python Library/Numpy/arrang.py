import numpy as np

a = np.arange(1,11)
print(a)# in ascending order from 1 to 10
b = np.arange(1,11,2)
print(b)

c = np.arange(1,11).reshape(5,2)#in a matrix format with reshape(row,column)
print(c)

#np.ones and np.zeroes matrix 
z=np.ones((3,4)) 
print(z)#weight of the matrix is 1

l = np.zeros((6,7))
print(l)#weight of the matrix is 0

#np.linspace
f = np.linspace(-10,10,6) #give any 6 number between 10 and -10
print(f)

#np.identity
print("Identity Matrix:")
g= np.identity(3)
print(g)

#arrange with reshape

x = np.arange(16).reshape(2,2,2,2)
print(x)