Python 3.13.7 (v3.13.7:bcee1c32211, Aug 14 2025, 19:10:51) [Clang 16.0.0 (clang-1600.0.26.6)] on darwin
Enter "help" below or click "Help" above for more information.
>>> 
============ RESTART: /Users/kheycie/Desktop/starbucks nutrition.py ============
Matplotlib is building the font cache; this may take a moment.
First 5 rows:
   Unnamed: 0                         item  calories  ...  fiber  protein    type
0           1                 8-Grain Roll       350  ...      5       10  bakery
1           2            Apple Bran Muffin       350  ...      7        6  bakery
2           3                Apple Fritter       420  ...      0        5  bakery
3           4              Banana Nut Loaf       490  ...      4        7  bakery
4           5  Birthday Cake Mini Doughnut       130  ...      0        0  bakery

[5 rows x 8 columns]

Dataset info:
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 77 entries, 0 to 76
Data columns (total 8 columns):
 #   Column      Non-Null Count  Dtype  
---  ------      --------------  -----  
 0   Unnamed: 0  77 non-null     int64  
 1   item        77 non-null     object 
 2   calories    77 non-null     int64  
 3   fat         77 non-null     float64
 4   carb        77 non-null     int64  
 5   fiber       77 non-null     int64  
 6   protein     77 non-null     int64  
 7   type        77 non-null     object 
dtypes: float64(1), int64(5), object(2)
memory usage: 4.9+ KB
None

Missing values:
Unnamed: 0    0
item          0
calories      0
fat           0
carb          0
fiber         0
protein       0
type          0
dtype: int64

Warning (from warnings module):
  File "/Users/kheycie/Desktop/starbucks nutrition.py", line 21
    sns.barplot(x="protein", y="item", data=top_protein, palette="viridis")
FutureWarning: 

Passing `palette` without assigning `hue` is deprecated and will be removed in v0.14.0. Assign the `y` variable to `hue` and set `legend=False` for the same effect.

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the Starbucks dataset
df = pd.read_csv("starbucks_data.csv")

# Quick check
print("First 5 rows:")
print(df.head())
print("\nDataset info:")
print(df.info())
print("\nMissing values:")
print(df.isnull().sum())

# -------------------------------
# Top 10 items by protein
top_protein = df.sort_values("protein", ascending=False).head(10)

plt.figure(figsize=(8,6))
sns.barplot(x="protein", y="item", data=top_protein, palette="viridis")
plt.title("Top 10 Starbucks Items by Protein")
plt.xlabel("Protein (g)")
plt.ylabel("Item")
plt.tight_layout()
plt.show()

# -------------------------------
# Protein distribution by type
plt.figure(figsize=(10,6))
sns.boxplot(x="type", y="protein", data=df)
plt.xticks(rotation=45)
plt.title("Protein Distribution by Starbucks Item Type")
plt.tight_layout()
plt.show()

# -------------------------------
# Optional: Protein per calorie
df["protein_per_calorie"] = df["protein"] / df["calories"]
top_efficiency = df.sort_values("protein_per_calorie", ascending=False).head(10)

plt.figure(figsize=(8,6))
sns.barplot(x="protein_per_calorie", y="item", data=top_efficiency, palette="magma")
plt.title("Top 10 Starbucks Items by Protein per Calorie")
plt.xlabel("Protein per Calorie")
plt.ylabel("Item")
plt.tight_layout()
plt.show()

print("Starbucks protein analysis complete!")

