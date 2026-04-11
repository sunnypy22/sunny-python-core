
import pandas as pd
# Creating a DataFrame
data = {
    "Name": ["Sunny", "Priya", "Rahul", "Neha"],
    "Age": [25, 22, 28, 24],
    "City": ["Pune", "Mumbai", "Delhi", "Bangalore"],
    "Score": [92, 88, 95, 85]
}
df = pd.DataFrame(data)
print("DataFrame:")
print(df)
print("\nBasic Info:")
print(df.info())
print("\nStatistics:")
print(df.describe())