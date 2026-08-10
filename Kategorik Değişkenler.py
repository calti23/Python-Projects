import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from collections import Counter

import warnings
warnings.filterwarnings("ignore")

veri = pd.read_csv("new_athlete_events.csv")

def plotBar(değişken , n = 5):
    """
        Girdi:Değişken/Sütun ismi
            n:en önemli 5 eşsiz değer
        Çıktı:Çubuk(Bar) Grafiği
    """
    veri_ = veri[değişken]
    veri_sayma = veri_.value_counts()
    veri_sayma = veri_sayma[:n]
    plt.figure()
    plt.bar(veri_sayma.index , veri_sayma , color = "blue")
    plt.xticks(veri_sayma.index , veri_sayma.index.values) #X-EKSENİNDE YAZACAK DEĞİŞKEN ADI
    plt.xticks(rotation = 45) #YAZDIRIRKEN 45 DERECE AÇIYLA YAZDIRACAĞIZ
    plt.ylabel("Frekans")
    plt.title("Veri Sıklığı - {}".format(değişken))
    plt.show()
    print("{} \n {}".format(değişken , veri_sayma))

kategorik_değişken = ["isim" , "cinsiyet" , "takım" , "uok" , "sezon" , "şehir" , "spor" , "etkinlik" , "madalya"]

for i in kategorik_değişken:
    plotBar(i)
