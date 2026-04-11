
import pandas as pd
df = pd.read_csv("students.csv")   # assume file exists
print("First 5 rows:")
print(df.head())
print("\nAverage Score by City:")
print(df.groupby("City")["Score"].mean())
# Filtering
high_scorers = df[df["Score"] > 90]
print("\nStudents with score > 90:")
print(high_scorers)
