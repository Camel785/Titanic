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
        # fare_by_survival = self.df.groupby('Survived')['Fare'].count()
        # return  fare_by_survival
        fare_bins = [0, 50, 100, 150, 200, 250, 500]
        fare_labels = ['0-50', '51-100', '101-150', '151-200', '201-250', '251+']

        self.df['Fare_Category'] = pd.cut(self.df['Fare'], bins=fare_bins, labels=fare_labels, right=False)
        fare_by_survival = self.df.groupby(['Fare_Category', 'Survived']).size().unstack(fill_value=0)
        return fare_by_survival


    def analyze_family(self):
        """
        Analizujemy dane o rodzinach (Sibsp - liczba osob spokrewnionych) (parch - liczba rodzicow/dzieci)
        """
        family_by_survival = self.df.groupby('Survived')['SibSp'].mean()
        family_by_survival_parch = self.df.groupby('Survived')['Parch'].mean()
        return family_by_survival, family_by_survival_parch

    def mortality_plot(self):
        """Tworzymy wykres dla mortality cabins"""
        mortality_ba_cabin, count_by_cabin = self.mortality()
        #death_rate = mortality_ba_cabin / count_by_cabin

        plt.figure(figsize=(14,10))
        mortality_ba_cabin.plot(kind='bar', color='blue', edgecolor='black')

        plt.title("Mortality Rate by Cabin Letter")
        plt.xlabel("Cabin Letter", fontsize=14)
        plt.ylabel("Mortality ", fontsize=14)

        plt.xticks(rotation=0)
        plt.show()

    def fare_plot(self):
        fare_by_survival = self.analyze_fare()  # Get the analysis data

        # Create the plot
        fare_by_survival.plot(kind='bar', stacked=True, color=['red', 'green'], edgecolor='black', figsize=(12, 8))

        # Adding title and axis labels
        plt.title("Survival by Category", fontsize=16)
        plt.xlabel("Fare Category", fontsize=14)
        plt.ylabel("Number of People", fontsize=14)
        plt.xticks(rotation=45)


        plt.legend(["Died", "Survived"], loc='upper left')

        plt.show()

    def family_plot(self):
        family_by_survival, family_by_survival_parch = self.analyze_family()

        fig, ax = plt.subplots(figsize=(10, 6))

        # Dane dla wykresu
        labels = ['Survived', 'Died']
        sibsp_values = [family_by_survival[1], family_by_survival[0]]  # 1 -> Survived, 0 -> Died
        parch_values = [family_by_survival_parch[1], family_by_survival_parch[0]]

        # Słupki dla SibSp
        ax.bar(labels, sibsp_values, width=0.4, label='SibSp (Siblings/Spouses)', color='skyblue', align='center')

        # Słupki dla Parch
        ax.bar(labels, parch_values, width=0.4, label='Parch (Parents/Children)', color='salmon', align='edge')

        # Ustawienia wykresu
        ax.set_title('Average Family Size by Survival')
        ax.set_xlabel('Survival Status')
        ax.set_ylabel('Average Family Size')
        ax.legend()

        plt.show()




