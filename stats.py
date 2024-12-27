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

    def survival_by_gender(self):
        # gender_survival = self.df.groupby(["Survived", "Sex"]).size().unstack(fill_value=0)
        #
        #
        # gender_survival.plot(kind="bar", stacked=True, color=["red","green"])
        # plt.title("Survival by Gender")
        # plt.xlabel("Przezycie i Plec")
        # plt.ylabel("liczba osob")
        # #plt.legend(["Zginęli (0)", "Przeżyli (1)", "Kobiety", "Mężczyźni"], loc='upper right', title="Legenda")
        #
        # plt.show()
        male_survival = self.df[self.df["Sex"] == "male"]["Survived"].value_counts()
        female_survival = self.df[self.df["Sex"] == "female"]["Survived"].value_counts()

        # Przygotowanie wykresu
        fig, ax = plt.subplots(figsize=(10, 6))

        # Rysujemy słupki dla mężczyzn i kobiet
        ax.bar([0, 1], male_survival, width=0.4, label="Mężczyźni", color="blue", align="center")
        ax.bar([0, 1], female_survival, width=0.4, label="Kobiety", color="pink", align="edge")

        # Ustawienia wykresu
        ax.set_title("Survival by Gender")
        ax.set_xlabel("Survived")
        ax.set_ylabel("Number of people")
        ax.set_xticks([0, 1])
        ax.set_xticklabels(["Zginęli (0)", "Przeżyli (1)"])

        # Dodanie legendy
        ax.legend(title="Płeć", loc="upper right")
        plt.show()
        # Pokaż wykres
