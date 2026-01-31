# ---------------------------------------------
# NumPy Arrays: Creation & Properties
# ---------------------------------------------

import numpy as np

print("===== NUMPY ARRAY EXAMPLES =====\n")

# ---------------------------------------------
# 1. 1-D Array
# ---------------------------------------------
a1 = np.arange(10)

print("1-D Array (a1):")
print(a1)
print()

# ---------------------------------------------
# 2. 2-D Array (Matrix)
# ---------------------------------------------
a2 = np.arange(12, dtype=float).reshape(3, 4)

print("2-D Array (a2):")
print(a2)
print()

# ---------------------------------------------
# 3. 3-D Array
# ---------------------------------------------
a3 = np.arange(8).reshape(2, 2, 2)

print("3-D Array (a3):")
print(a3)
print()

# ---------------------------------------------
# Array Properties
# ---------------------------------------------

print("===== ARRAY PROPERTIES =====\n")

# Number of dimensions
print("Number of dimensions of a2 (ndim):")
print(a2.ndim)
print()

# Shape of the array
print("Shape of a2 (rows, columns):")
print(a2.shape)
print()

# Total number of elements
print("Total number of elements in a2 (size):")
print(a2.size)
print()

# Memory size of each element
print("Item size of a3 (in bytes):")
print(a3.itemsize)
print()

# ---------------------------------------------
# 4. Array with Specific Data Type
# ---------------------------------------------
a4 = np.arange(12, dtype=np.int32).reshape(3, 4)

print("2-D Array with int32 data type (a4):")
print(a4)
print()

print("Data type of a4 elements:")
print(a4.dtype)


#to change or optimize the memory size
print(a4.astype(np.int64))