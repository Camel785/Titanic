import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class Statistic:
    def __init__(self, df):
        self.df = df

    def death_plot(self):
        survival_counts = self.df["Survived"].value_counts()

        plt.figure(figsize=(12,8))
        survival_counts.plot(kind='bar', color=['red', 'green'])
        plt.title("Number of survived and deaths")
        plt.xlabel("Survived", fontsize=16)
        plt.ylabel("Number of people", fontsize=16)

        plt.show()