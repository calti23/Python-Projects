import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from collections import Counter

import warnings
warnings.filterwarnings("ignore")

veri = pd.read_csv("new_athlete_events.csv")

#PİVOT TABLOSU GENİŞ VERİ YAPILARININ İSTATİSTİKLERİNİ TUTMAYA YARAYAN TABLODUR
veri_pivot = veri.pivot_table(index = "madalya" , columns = "cinsiyet" , values = ["boy" , "kilo" , "yaş"] ,
                              aggfunc = {"boy" : np.mean , "kilo" : np.mean , "yaş" : [min , max , np.std]})
print(veri_pivot.head(5))

print("-" * 70)

#ANOMALİ TESPİTİ BİR VERİ GRUBUNDA AYKIRI DEĞERLERİN DÜZELTİLMESİ VEYA O DEĞERLERİN ÇIKARILMAS GİBİ YÖNTEMLERLE ORTALAMA VERİLERİN ÇOK DIŞINDA YANİ IQR DÜZEYİNİN VE 1.5XIQR DÜZEYİNİN DE ÖTESİNDE KALAN DEĞERLER İÇİN GEREKLİDİR
def anomaliTespiti(df , özellik):
    outlier_indices = []
    for c in özellik:
        #%25 LİK DİLİM-İLK ÇEYREK
        Q1 = np.percentile(df[c],25)
        #%75 LİK DİLİM-ÜÇÜNCÜ ÇEYREK
        Q3 = np.percentile(df[c],75)
        #IQR DEĞERİNİ (Q3-Q1(KUTU GRAFİĞİNDEN)) HESAPLAMAMIZ GEREKİYOR (IQR:ÇEYREKLER AÇIKLIĞI)
        IQR = Q3 - Q1
        #AYKIRI TESPİTİ İÇİN ÇARPAN DEĞERİ
        outlier_step = IQR * 1.5
        #AYKIRIYI VE AYKIRI İNDEKSİNİ TESPİT ET
        outlier_list_col = df[(df[c] < Q1 - outlier_step) | (df[c] > Q3 + outlier_step)].index
        #AYKIRI İNDEKSLERİNİ DEPOLA
        outlier_indices.extend(outlier_list_col)

    #EŞSİZ AYKIRI DEĞERLERİ BUL
    outlier_indices = Counter(outlier_indices)
    #EĞER BİR ÖRNEK VE 1 FARKLI SÜTUN İÇİN AYKIRI DEĞERSE AYKIRI KABUL EDECEĞİZ
    multiple_outliers = list(i for i , v in outlier_indices.items() if v > 1)

    return multiple_outliers

veri_anomali = veri.loc[anomaliTespiti(veri , ["yaş" , "kilo" , "boy"])] #VERİ(DF) İÇİNDEKİ BOY KİLO YAŞ ÖZELLİKLERİNDEKİ ANOMALİLİER TESPİT EDİLİR
print(veri_anomali.spor.value_counts()) #VERİ SETİNDEKİ SPORLARDA BOY GÖSTEREN SPORCULARIN KAÇ TANESİNİN YAŞ-BOY-KİLO ÖZELLİKLERİNDE ANOMALİ OLDUĞUNUN SAYISINI BULDUK

print("-" * 70)

plt.figure()
plt.bar(veri_anomali.spor.value_counts().index , veri_anomali.spor.value_counts().values)
plt.xticks(rotation = 30)
plt.title("Anomali Görünen Spor Branşları")
plt.ylabel("Frekans")
plt.grid(True , alpha = 0.5)
plt.show()

print("-" * 70)

#JİMNASTİKTE MEYDANA GELEN ANOMALİNİN NEDENİNE BAKALIM YANİ JİMNASTİKÇİ HANGİ SPORCULARDA ANOMALİ GÖRÜNDÜĞÜNE
veri_gym = veri_anomali[veri_anomali.spor == "Gymnastics"]
print(veri_gym)

print("-" * 70)

#BU ANOMALİLERİN HANGİ MÜSABAKALARDA OLDUĞUNU BULALIM
print(veri_gym.etkinlik.value_counts())

print("-" * 70)

#BASKETBOLCU SPORCULARIN HANGİLERİNDE ANOMALİ GÖRÜNDÜĞÜNE BAKALIM
veri_basketbol = veri_anomali[veri_anomali.spor == "Basketball"]
print(veri_basketbol)

print("-" * 70)

#BASKETBOLDAKİ ANOMALİ SPORCULARIN HANGİ MÜSABAKALARDA YER ALDIĞINA DA BAKALIM
print(veri_basketbol.etkinlik.value_counts())
