
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
# Sample data
data = pd.DataFrame({
    "Age": [25, 22, 28, 24, 30, 27],
    "Score": [92, 88, 95, 85, 90, 87],
    "City": ["Pune", "Mumbai", "Delhi", "Bangalore", "Pune", "Mumbai"]
})

plt.figure(figsize=(10, 6))
sns.scatterplot(data=data, x="Age", y="Score", hue="City", s=100)
plt.title("Score vs Age by City")
plt.show()
# Boxplot
sns.boxplot(data=data, x="City", y="Score")
plt.title("Score Distribution by City")
plt.show()
