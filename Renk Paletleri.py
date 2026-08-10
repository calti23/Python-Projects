import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from collections import Counter

import warnings
warnings.filterwarnings("ignore")

veri = pd.read_csv("new_athlete_events.csv")

#PALETTE = SET1 --> KIRMIZI-MAVİ-YEŞİL
def saçılımGrafik1():
    sns.scatterplot(x = 'boy' , y = 'kilo' , hue = 'madalya' , palette = 'Set1' , data = veri)
    plt.title('Madalyaya Göre Boy ve Kilo Dağılımları')
    plt.show()
#saçılımGrafik1()

print("-" * 70)

#PALETTE = SET2 --> TURKUAZ-TURUNCU-MAVİ/GRİ
def saçılımGrafik2():
    sns.scatterplot(x = 'boy' , y = 'kilo' , hue = 'madalya' , palette = 'Set2' , data = veri)
    plt.title('Madalyaya Göre Boy ve Kilo Dağılımları')
    plt.show()
#saçılımGrafik2()

print("-" * 70)

#PALETTE = SET3 --> SARI-TURKUAZ-AÇIK MOR
def saçılımGrafik3():
    sns.scatterplot(x = 'boy' , y = 'kilo' , hue = 'madalya' , palette = 'Set3' , data = veri)
    plt.title('Madalyaya Göre Boy ve Kilo Dağılımları')
    plt.show()
#saçılımGrafik3()

print("-" * 70)

#PALETTE = ROCKET --> MOR-KOYU PEMBE-TEN RENGİ
def saçılımGrafik4():
    sns.scatterplot(x = 'boy' , y = 'kilo' , hue = 'madalya' , palette = 'rocket' , data = veri)
    plt.title('Madalyaya Göre Boy ve Kilo Dağılımları')
    plt.show()
#saçılımGrafik4()

print("-" * 70)

def saçılımGrafik5():
    sns.scatterplot(x = 'boy' , y = 'kilo' , hue = 'madalya' , palette = 'rocket' , data = veri)
    plt.title('Madalyaya Göre Boy ve Kilo Dağılımları')
    plt.show()
#saçılımGrafik5()

print("-" * 70)

#ÇİZGİ GRAFİĞİ
sns.lineplot(x = 'boy' , y = 'kilo' , data = veri)
plt.title('Boy ve Kilo')
plt.show()

print("-" * 70)

#KATEGORİK ÇİZGİ GRAFİĞİ
sns.lineplot(x = 'boy' , y = 'kilo' , hue = 'cinsiyet' , data = veri)
plt.title('Cinsiyete Göre Boy ve Kilo Dağılımları')
plt.show()

#HİSTOGRAM GRAFİĞİ
sns.displot(veri , x = "kilo")
plt.ylabel("Sporcu Sayısı")
plt.title('Sporcuların Kilo Dağılımı')
plt.show()

#HİSTOGRAM - KATEGORİK
sns.displot(veri , x = "kilo" , hue = "cinsiyet")
plt.ylabel("Sporcu Sayısı")
plt.title('Kilonun Cinsiyete Göre Durumu')
plt.show()

#AYRI AYRI CİNSİYETLERİN KİLOYLA OLAN DURUMUNUN HİSTOGRAM GRAFİKLERİNİ ÇİZELİM
sns.displot(veri , x = "kilo" , col = "cinsiyet" , multiple = "dodge") #2 AYRI GRAFİK ÇİZMEMİZE YARAYAN SATIR
plt.show()

#İKİ BOYUTLU HİSTOGRAM
sns.displot(veri , x = "kilo" , y = "boy" , kind = "kde")
plt.xlabel("kilo")
plt.ylabel("boy")
plt.title('Kilo - Boy Histogramı')
plt.show()

#BU GRAFİĞİ CİNSİYETLERE AYRIŞTIRALIM
sns.displot(veri , x = "kilo" , y = "boy" , hue = "cinsiyet" , kind = "kde")
plt.xlabel("kilo")
plt.ylabel("boy")
plt.title('Kilo - Boy Histogramı')
plt.show()

#FİLL ETİKETİ İLE BU TOPOGRAFİK GRAFİKLERİN İÇLERİ DOLDURULMUŞ OLUR
sns.displot(veri , x = "kilo" , y = "boy" , hue = "cinsiyet" , fill = True)
plt.xlabel("kilo")
plt.ylabel("boy")
plt.title('Kilo - Boy Histogramı')
plt.show()
