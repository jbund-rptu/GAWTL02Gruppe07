import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt


#Daten einlesen
data=pd.read_csv("../Aufgabe 1/data/data.csv")

#Ausgabe der Urlisten
for i in data.columns:
    data[i].to_csv("../Aufgabe 1/data/urliste_"+i+".csv", header=False, index=False)

#Ausgabe der Ranglisten
data["Jahr"].sort_values(ascending=False).to_csv("../Aufgabe 1/data/Rangliste_Jahr.csv", header=False, index=False)

data["Monat"].sort_values(ascending=False).to_csv("../Aufgabe 1/data/Rangliste_Monat.csv", header=False, index=False)
months = ["Jan", "Feb", "Mär", "Apr", "Mai", "Jun", 
          "Jul", "Aug", "Sep", "Okt", "Nov", "Dez"]
data['Monat'] = pd.Categorical(data['Monat'], categories=months, ordered=True)
data["Monat"].sort_values(ascending=False).to_csv("../Aufgabe 1/data/Rangliste_Monat.csv", header=False, index=False)

data["Verbraucherpreisindex insgesamt"].sort_values(ascending=False).to_csv("../Aufgabe 1/data/Rangliste_Verbraucherpreisindex insgesamt.csv", header=False, index=False)

print("Modus:")
print(stats.mode(data["Verbraucherpreisindex insgesamt"], keepdims=True))
print("arithmetischer Mittelwert:")
print(np.mean(data["Verbraucherpreisindex insgesamt"]))
print("Median:")
print(np.median(data["Verbraucherpreisindex insgesamt"]))

