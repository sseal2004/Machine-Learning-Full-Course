#np.array
import numpy as np

# 1D numpy array (vector)
print("1d array:")
a=np.array([1,2,3])#inside np.arry include a list.
print(a)
print(type(a))#type 

# 2D numpy array (matrix)
print("2d array:")
b= np.array([[1,2,3],[4,5,6]])#you can also call it matrix
print(b)
#3D numpy array (tensor)
print("3d array:")
c = np.array([[[1,2],[1,3]],[[5,6],[7,8]]])
print(c)
#data type
print("Data Type: Float")
d= np.array([1,2,3],dtype=float)
print(d)
print("Data Type: Boolean")
e= np.array([1,0,3],dtype=bool)#for 0 it gives false
print(e)
print("Data Type:Complex Number")
f = np.array([1,0,7],dtype=complex)
print(f)
print("Data Type:Float Number")
g = np.array([1,0,7],dtype=float)
print(g)










