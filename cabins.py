import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class CabinsAnalysis:
    def __init__(self, df):
        """
        Inicjalizacja klasy z danymi data frame
        :param df: DataFrame zawierajace dane o pasazerach
        """
        self.df = df
        self.df['First_Letter'] = self.df['Cabin'].dropna().str[0]

    def mortality(self):
        """
        Analizujemy liczbe smierci i ilosc osob  w zaleznosci od litery Kabiny
        """
        mortality_by_cabin = self.df.groupby('First_Letter')['Survived'].sum()
        count_by_cabin = self.df.groupby('First_Letter')['Survived'].count()
        return mortality_by_cabin, count_by_cabin

    def analyze_fare(self):
        """
        Analizujemy oplate w zaleznosci od przezycia
        """
        fare_by_survival = self.df.groupby('Survived')['Fare'].count()
        return  fare_by_survival

    def analyze_family(self):
        """
        Analizujemy dane o rodzinach (Sibsp - liczba osob spokrewnionych) (parch - liczba rodzicow/dzieci)
        """
        family_by_survival = self.df.groupby('Survived')['SibSp'].mean()
        family_by_survival_parch = self.df.groupby('Survived')['Parch'].mean()
        return family_by_survival, family_by_survival_parch

    def plot_analysis(self):
        """
        Tworzymy Zaawansowany wykres z wynikami wszystkich analiz z uzyciem Seaborn
        """
        sns.set(style='whitegrid')

        fig, axes = plt.subplots(2, 2, figsize=(16, 10))
        fig.suptitle("Analiza Danych o Pasazerach Titanic", fontsize=16)

        mortality_by_cabin, count_by_cabin = self.mortality()
        mortality_by_cabin_percent = (mortality_by_cabin / count_by_cabin) * 100
        sns.barplot(x=mortality_by_cabin_percent.index, y=mortality_by_cabin_percent.values, ax=axes[0,0], palette="Blues_d")
        axes[0, 0].set_title("Śmiertelność w zależności od litery kabiny")
        axes[0, 0].set_xlabel("Litera Kabiny")
        axes[0, 0].set_ylabel("Procent Zmarłych (%)")

        # Wykres 2: Fare (Opłata) w zależności od przeżycia
        fare_by_survival = self.analyze_fare()
        sns.barplot(x=fare_by_survival.index, y=fare_by_survival.values, ax=axes[0, 1], palette="Reds_d")
        axes[0, 1].set_title("Średnia opłata w zależności od przeżycia")
        axes[0, 1].set_xlabel("Przeżycie")
        axes[0, 1].set_ylabel("Średnia Opłata")

        # Wykres 3: Średnia liczba rodzeństwa/spokrewnionych (SibSp) w zależności od przeżycia
        family_by_survival_sibsp, _ = self.analyze_family()
        sns.barplot(x=family_by_survival_sibsp.index, y=family_by_survival_sibsp.values, ax=axes[1, 0],
                    palette="Greens_d")
        axes[1, 0].set_title("Średnia liczba rodzeństwa/spokrewnionych (SibSp)")
        axes[1, 0].set_xlabel("Przeżycie")
        axes[1, 0].set_ylabel("Średnia Liczba")

        # Wykres 4: Średnia liczba rodziców/dzieci (Parch) w zależności od przeżycia
        _, family_by_survival_parch = self.analyze_family()
        sns.barplot(x=family_by_survival_parch.index, y=family_by_survival_parch.values, ax=axes[1, 1],
                    palette="Purples_d")
        axes[1, 1].set_title("Średnia liczba rodziców/dzieci (Parch)")
        axes[1, 1].set_xlabel("Przeżycie")
        axes[1, 1].set_ylabel("Średnia Liczba")

        # Dostosowanie układu
        plt.tight_layout(rect=[0, 0.03, 1, 0.95])
        plt.show()

