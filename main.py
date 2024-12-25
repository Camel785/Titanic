import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px
import seaborn as sns
from cabins import CabinsAnalysis
#"C" (Cherbourg), "Q" (Queenstown), "S" (Southampton).EMBARKED
#







pd.set_option("display.max_columns", 20)
df = pd.read_csv("data.csv")
print(df.info())

#print(df.isna().values.any())
# rows_with_NaN = df[df.isna().any(axis=1)].index
# #print(rows_with_NaN)
#
# missing_age = df["Age"].isna().sum()
# missing_age_position = df[df["Age"].isna()]["Age"]
# #print(f"Missing age values are: {missing_age}")
# #print(f"Rows with missing Ages: {missing_age_position}")
#
# missing_cabin = df["Cabin"].isna().sum()
# missing_cabin_position = df[df["Cabin"].isna()]["Cabin"]
# print(f"Missing Cabins values are: {missing_cabin}")
# print(f"Rows with missing Cabins are: {missing_cabin_position}")
#
# not_nan_cabins = df[df["Cabin"].notna()]
# #print(not_nan_cabins)
# unique_cabin = df["Cabin"].dropna().unique()
# #print(unique_cabin)
#
# unique_letters = df["Cabin"].dropna().str[0]
# number_of_letters = unique_letters.value_counts()
# print(number_of_letters)
#
# df["First_Letter"] = df['Cabin'].dropna().str[0]
# mortality_by_cabin = df.groupby("First_Letter")['Survived'].sum()
# count_by_cabin = df.groupby("First_Letter")['Survived'].count()
#
# #mortality_by_cabin = 1 - mortality_by_cabin
# print("Chance to survived when you look at the Cabins are: ")
# for letter, mortality in mortality_by_cabin.items():
#     print(f"{letter}: {mortality:.2f}")
#
# plt.figure(figsize=(12,8))
#
# mortality_by_cabin.plot(kind="bar", color='skyblue', edgecolor='black')
#
# plt.title('Death Depends of First Cabin Letter')
# plt.xlabel('First Letter of Cabin, With Numbers of Passengers ', fontsize=12)
# plt.ylabel('Number of Deaths', fontsize=12)
#
# labels = [f"{letter}{count_by_cabin[letter]}" for letter in mortality_by_cabin.index]
# plt.xticks(ticks=range(len(mortality_by_cabin)), labels=labels, rotation=45)
# plt.tight_layout()
# plt.show()

analysis = CabinsAnalysis(df)

analysis.mortality_plot()
analysis.fare_plot()
#analysis.plot_analysis()