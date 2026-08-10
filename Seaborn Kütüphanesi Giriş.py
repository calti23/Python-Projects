import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from collections import Counter

import warnings
warnings.filterwarnings("ignore")

veri = pd.read_csv("new_athlete_events.csv")

def saçılımGrafik1():
    sns.scannerplot(x = 'boy' , y = 'kilo' , data = veri)
    plt.title('Boy ve Kilo Arasondaki Değişim')
    plt.show()

sns.set_style("darkgrid") #SNS_STYLE FONKSİYONU GÖRÜNÜŞÜ AYARLAR

def saçılımGrafik2():
    sns.scannerplot(x = 'boy' , y = 'kilo' , hue = 'madalya' , data = veri) #HUE:NÜANS/ETİKET
    plt.title('Madalyaya Göre Boy ve Kilo Dağılmı')
    plt.show()

#SAÇILIM GRAFİĞİ - DOĞRUSAL REGRESYON
sns.regplot(x = 'boy' , y = 'kilo' , data = veri , marker = '+' , color = "purple" , scatter_kws = {'alpha' : 0.2})
plt.title('Boy ve Kilo Dağılımı')
#BU GRAFİKLE BİRLİKTE BOY VE KİLO ARASINDA BİR ORANA GÖRE REGRESYON EĞRİSİ ÇEKEREK BOY KİLO ARASINDAKİ DOĞRUSAL İLİŞKİYİ FORMÜLİZE EDEBİLİRİZ

