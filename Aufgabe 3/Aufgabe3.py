import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt


#Daten einlesen
data=pd.read_csv("../Aufgabe 3/data/data.csv")

#Ausgabe der Urlisten
for i in data.columns:
    data[i].to_csv("../Aufgabe 3/data/urliste_"+i+".csv", header=False, index=False)

#Ausgabe der Ranglisten
data["Jahr"].sort_values(ascending=False).to_csv("../Aufgabe 3/data/Rangliste_Jahr.csv", header=False, index=False)

data["Monat"].sort_values(ascending=False).to_csv("../Aufgabe 3/data/Rangliste_Monat.csv", header=False, index=False)
months = ["Jan", "Feb", "Mär", "Apr", "Mai", "Jun", 
          "Jul", "Aug", "Sep", "Okt", "Nov", "Dez"]
data['Monat'] = pd.Categorical(data['Monat'], categories=months, ordered=True)
data["Monat"].sort_values(ascending=False).to_csv("../Aufgabe 3/data/Rangliste_Monat.csv", header=False, index=False)

data["Key"].sort_values(ascending=False).to_csv("../Aufgabe 3/data/Rangliste_Key.csv", header=False, index=False)

data["Verbraucherpreisindex insgesamt"].sort_values(ascending=False).to_csv("../Aufgabe 3/data/Rangliste_Verbraucherpreisindex insgesamt.csv", header=False, index=False)


#---R3.9---
print("\nModus:")
print(stats.mode(data["Verbraucherpreisindex insgesamt"].dropna(), keepdims=True))
print("\narithmetischer Mittelwert:")
print(np.mean(data["Verbraucherpreisindex insgesamt"].dropna()))
print("\nMedian:")
print(np.median(data["Verbraucherpreisindex insgesamt"].dropna()))

#---R3.10---
print("\nSpannweite:")
print(data["Verbraucherpreisindex insgesamt"].max()- data["Verbraucherpreisindex insgesamt"].min())



#---R3.11---
print("\nmittlere Abweichung vom Median")
print(np.median(np.absolute(data["Verbraucherpreisindex insgesamt"].dropna() - np.median(data["Verbraucherpreisindex insgesamt"].dropna()))))

#---R3.12---
print("\nStichprobenvarianz")
print( (1/(len(data["Verbraucherpreisindex insgesamt"].dropna())-1)) * sum(pow(data["Verbraucherpreisindex insgesamt"].dropna()-np.mean(data["Verbraucherpreisindex insgesamt"].dropna()),2)))

#---R3.13---
print("\nVariationskoeffizient")#standardabweichung/ arithmetisches mittel
print(np.std(data["Verbraucherpreisindex insgesamt"])/np.mean(data["Verbraucherpreisindex insgesamt"]))

#---R2.13---
#"""
plt.boxplot(data["Verbraucherpreisindex insgesamt"].dropna(),
                vert=False,
                whis=(10,90)) # quartil beschriftung einfügen
plt.text(np.percentile(data["Verbraucherpreisindex insgesamt"].dropna(),10),1.1,r'$Q_{ 0.1}$',rotation=45)
plt.text(np.percentile(data["Verbraucherpreisindex insgesamt"].dropna(),25),1.1,r'$Q_{ 0.25}$',rotation=45)
plt.text(np.percentile(data["Verbraucherpreisindex insgesamt"].dropna(),75),1.1,r'$Q_{ 0.75}$',rotation=45)
plt.text(np.percentile(data["Verbraucherpreisindex insgesamt"].dropna(),90),1.1,r'$Q_{ 0.90}$',rotation=45)
plt.show()
"""
#---R2.14---
"""
x = pd.date_range( '2017-01-01','2022-09-01', freq='MS').tolist()
print(len(x))
print(len(data["Verbraucherpreisindex insgesamt"].reindex(index=data.index[::-1])))
plt.scatter(x, data["Verbraucherpreisindex insgesamt"].reindex(index=data.index[::-1]))
plt.ylabel("Verbrauchspreisindex in %")
plt.xlabel("Zeit in Jahren")
plt.show()
"""

#---R2.17---
"""
quantile = pd.DataFrame(columns=['Quantil','Wert'])

for i in range(1,10):
    quantile = quantile.append({'Quantil':i*0.1, 'Wert':np.percentile(data["Verbraucherpreisindex insgesamt"].dropna(),i*10).round(decimals=3)}, ignore_index=True)

for i in range(1,4):
    quantile = quantile.append({'Quantil':i*0.25, 'Wert':np.percentile(data["Verbraucherpreisindex insgesamt"].dropna(),i*25).round(decimals=3)}, ignore_index=True)

print(quantile)
#"""
