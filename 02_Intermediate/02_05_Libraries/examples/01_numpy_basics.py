
# 01_numpy_basics.py
import numpy as np
# Creating arrays
a = np.array([1, 2, 3, 4, 5])
b = np.zeros((3, 3))
c = np.ones((2, 4))
d = np.random.randint(0, 100, size=(5, 3))
print("Array a:", a)
print("Shape of d:", d.shape)
print("Mean of a:", np.mean(a))
print("Sum of d:", np.sum(d))
print("Max value in d:", np.max(d))

