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

        # Adding a legend
        plt.legend(["Died", "Survived"], loc='upper left')

        # Show the plot
        plt.show()
        # fare_by_survival = self.analyze_fare()  # Get the analysis data
        #
        # # Plot for each fare category
        # for fare_category in fare_by_survival.index:
        #     # Get the survival counts for the current fare category
        #     survival_counts = fare_by_survival.loc[fare_category]
        #
        #     # Labels for the pie chart (0 for Died, 1 for Survived)
        #     labels = ['Died', 'Survived']
        #
        #     # Plot the pie chart
        #     plt.figure(figsize=(7, 7))  # Make the plot a square
        #     plt.pie(survival_counts, labels=labels, autopct='%1.1f%%', startangle=90, colors=['red', 'green'])
        #     plt.title(f"Survival by Fare Category: {fare_category}")
        #
        #     # Show the pie chart
        #     plt.show()
        # fare_bins = [0, 50, 100, 150, 200, 250, 500]
        # fare_labels = ['0-50', '51-100', '101-150', '151-200', '201-250', '250+']
        #
        # # Dodajemy nową kolumnę z kategorią cenową
        # self.df['Fare_Category'] = pd.cut(self.df['Fare'], bins=fare_bins, labels=fare_labels, right=False)
        #
        # # Grupujemy dane po Fare_Category i Survived, liczymy ile osób przeżyło i zginęło w każdej kategorii
        # survival_by_fare_category = self.df.groupby(['Fare_Category', 'Survived']).size().unstack(fill_value=0)
        #
        # # Przygotowanie do wykresu kołowego
        # # Rozpoczynamy od "flattening" DataFrame: tworzymy listę etykiet i wartości dla wykresu kołowego
        # labels = []
        # sizes = []
        # for category in survival_by_fare_category.index:
        #     # Dla każdej kategorii cenowej
        #     survived = survival_by_fare_category.loc[category, 1]  # Liczba przeżyłych
        #     died = survival_by_fare_category.loc[category, 0]  # Liczba zmarłych
        #
        #     # Dodajemy odpowiednie etykiety i liczby
        #     labels.append(f"{category} - Survived")
        #     sizes.append(survived)
        #     labels.append(f"{category} - Died")
        #     sizes.append(died)
        #
        # # Tworzymy wykres kołowy
        # plt.figure(figsize=(10, 10))
        # plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, colors=plt.cm.Paired.colors)
        # plt.title("Survival and Death Rate by Fare Category")
        #
        # # Pokazujemy wykres
        # plt.show()

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

