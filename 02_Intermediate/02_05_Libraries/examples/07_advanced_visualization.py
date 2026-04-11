
import seaborn as sns

import matplotlib.pyplot as plt
# Load built-in dataset
tips = sns.load_dataset("tips")
plt.figure(figsize=(12, 8))
# Subplot with multiple plots

plt.subplot(2, 2, 1)
sns.histplot(data=tips, x="total_bill", kde=True)
plt.title("Distribution of Total Bill")
plt.subplot(2, 2, 2)
sns.boxplot(data=tips, x="day", y="total_bill")
plt.title("Total Bill by Day")
plt.subplot(2, 2, 3)
sns.scatterplot(data=tips, x="total_bill", y="tip", hue="sex")
plt.title("Tip vs Total Bill")
plt.tight_layout()
plt.show()