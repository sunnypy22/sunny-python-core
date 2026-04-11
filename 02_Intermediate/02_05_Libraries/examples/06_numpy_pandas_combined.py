
import numpy as np
import pandas as pd
# Create random data with NumPy
np.random.seed(42)

data = np.random.randn(1000, 4)
df = pd.DataFrame(data, columns=["Feature1", "Feature2", "Feature3", "Feature4"])
print("DataFrame shape:", df.shape)
print("Mean of each column:\n", df.mean())

print("Correlation matrix:\n", df.corr())
