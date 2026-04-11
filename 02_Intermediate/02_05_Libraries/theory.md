# NumPy Basics, Pandas Introduction & Data Visualization
## 1. NumPy Basics
**Definition**: NumPy (Numerical Python) is the fundamental package for scientific computing in Python. It provides support for large multi-dimensional arrays and matrices, along with high-level mathematical functions.
### Key Features
- `ndarray` — efficient multi-dimensional array object
- Vectorized operations (fast)
- Broadcasting
- Linear algebra, random number generation, etc.
```python
import numpy as np
# Creating arrays
arr1 = np.array([1, 2, 3, 4])
arr2 = np.zeros((3, 4))
arr3 = np.random.randn(5, 5)
```
## 2. Pandas Introduction
**Definition**: Pandas is a powerful data manipulation and analysis library built on top of NumPy. It provides two main data structures:
Series — 1-dimensional labeled array
DataFrame — 2-dimensional labeled data structure (like Excel table)
### Core Features
Easy data cleaning and transformation
Powerful indexing and selection
GroupBy operations
Handling missing data
Reading/writing different file formats
### 3. Data Visualization with Matplotlib & Seaborn
**Matplotlib**: Foundation library for plotting in Python (highly customizable)
**Seaborn**: Statistical data visualization library built on Matplotlib (more beautiful and easier for statistical plots)
```Python
import matplotlib.pyplot as plt
import seaborn as sns
```