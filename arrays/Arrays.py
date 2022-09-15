# This page shows you how to use LISTS as ARRAYS, however,
# to work with arrays in Python you will have to import a library,
# like the NumPy library.
import numpy as np

cars = ["Ford", "Volvo", "BMW"]

# Python List
my_list = [1,2,3]
for i in range(len(my_list)):
    my_list[i] *= 3

# Numpy Array   
my_array = np.array([2,3,4])
my_array *= 3

print(my_list)
print(my_array)
# Single Data Type avoids type checking at runtime
# Uses continious blocks of memory

# Need to use NumPy Data Types
# bool_, int8, int16, int32, int64, uint8, ... , float16, ..., complex64, complex128
