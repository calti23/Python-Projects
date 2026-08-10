import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from collections import Counter

import warnings
warnings.filterwarnings("ignore")

veri = pd.read_csv("new_athlete_events.csv")

#ERKEK SPORCU VERİLERİNİ OKUYALIM
erkek = veri[veri.cinsiyet == "M"]
print(erkek.head(5))

print("-" * 70)

#KADIN SPORCU VERİLERİNİ OKUYALIM
kadın = veri[veri.cinsiyet == "F"]
print(kadın.head(5))

print("-" * 70)

#KADIN VE ERKEKLER ARASINDAKİ BOY İLİŞKİSİNE BAKALIM
plt.figure()
plt.scatter(kadın.boy , kadın.kilo , alpha = 0.4 , label = "Kadın")
plt.scatter(erkek.boy , erkek.kilo , alpha = 0.4 , label = "Erkek")
plt.xlabel("Boy(Cm)")
plt.ylabel("Kilogram(kg)")
plt.title("Boy ve Kilo Arasındaki İlişki")
plt.legend() #SAĞ ÜSTE HANGİ RENGİN HANGİ ETİKETİ TEMSİL ETTİĞİNİ GÖSTEREN LEJANTI AÇAR
plt.show()

print("-" * 70)

#YAŞ-BOY-KİLO ARASINDA BİR KORELASYON VAR MI KONTROLÜ YAPACAĞIZ CORR FONKSİYONU İLE (YANİ ORANLAMALAR)
print(veri.loc[:,["yaş" , "boy" , "kilo"]].corr()) #KORELASYON TABLOSU OLUŞTURULUR
#KORELASYON DEĞERLERİ 1 E NE KADAR YAKINSA O VERİLER ARASINDA O KADAR YAKIN BİR İLİŞKİ VARDIR

print("-" * 70)

#MADALYA DERECESİ İLE YAŞ ARASINDA BİR İLİŞKİ VAR MI?
veri_geçici = veri.copy()
veri_geçici = pd.get_dummies(veri_geçici , columns = ['madalya']) #MADALYA SATIRINI 3 E BÖLMÜŞ OLDUK(ALTIN-GÜMÜŞ-BRONZ)
print(veri_geçici.head(5))

print("-" * 70)

print(veri_geçici.loc[:,["yaş" , "madalya_Bronze" , "madalya_Silver" , "madalya_Gold"]].corr()) #SORUMUZUN CEVABINIBU SATIRDA KORELASYONA BAKARAK BULACAĞIZ

print("-" * 70)

#TAKIMLARIN KAZANDIKLARI BRONZ-GÜMÜŞ-ALTIN MADALYA SAYILARI
veri_geçici[["takım" , "madalya_Gold" , "madalya_Silver" , "madalya_Bronze"]].groupby(["takım"] , as_index = False).sum().sort_values(by = "madalya_Gold" , ascending = False)[:10]
#ASCENDİNG ARTAN DİSCENDİNG AZALAN SIRA DEMEK...
print(veri_geçici[["takım" , "madalya_Gold" , "madalya_Silver" , "madalya_Bronze"]].groupby(["takım"] , as_index = False).sum().sort_values(by = "madalya_Gold" , ascending = False)[:10])

print("-" * 70)

#KAZANILAN MADALYALARIN ŞEHİRLERE GÖRE SAYILARI
veri_geçici[["şehir" , "madalya_Gold" , "madalya_Silver" , "madalya_Bronze"]].groupby(["şehir"] , as_index = False).sum().sort_values(by = "madalya_Gold" , ascending = False)[:10]
print(veri_geçici[["şehir" , "madalya_Gold" , "madalya_Silver" , "madalya_Bronze"]].groupby(["şehir"] , as_index = False).sum().sort_values(by = "madalya_Gold" , ascending = False)[:10])

print("-" * 70)

#KADIN VE ERKEKLERE GÖRE KAZANILAN MADALYA SAYILARI
print(veri_geçici[["cinsiyet" , "madalya_Gold" , "madalya_Silver" , "madalya_Bronze"]].groupby(["cinsiyet"] , as_index = False).sum().sort_values(by = "madalya_Gold" , ascending = False)[:10])
