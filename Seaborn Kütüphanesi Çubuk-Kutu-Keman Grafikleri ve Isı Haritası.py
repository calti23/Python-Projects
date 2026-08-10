import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from collections import Counter

import warnings
warnings.filterwarnings("ignore")

veri = pd.read_csv("new_athlete_events.csv")

sns.catplot(x = "sezon" , y = "boy" , hue = "cinsiyet" , col = "madalya" , data = veri , kind = "violin" , split = True , height = 4 , aspect = .7)
plt.show()

#SEABORN KÜTÜPHANESİ İLE ÇUBUK GRAFİK ÇİZİMİ
sns.barplot(x = "madalya" , y = "boy" , data = veri)
plt.title('Madalyalara Göre Boy Durumları')
plt.show()

#ŞİMDİ DE CİNSİYET İLE MADALYA İLİŞKİSİNE BAKALIM
sns.barplot(x = "madalya" , y = "boy" , hue = "cinsiyet" , data = veri)
plt.title('Madalyaların ve Boyun Cinsiyete Göre Durumları')
plt.show()

#MADALYA ALMIŞ SPORCULARIN YAŞLARININ CİNSİYETLERE ve SEZONLARA GÖRE AYRILMIŞ ŞEKLİNİ GÖRMEK İSTİYORUZ
sns.catplot(x = "madalya" , y = "yaş" , hue = "cinsiyet" , col = "sezon" , data = veri , kind = "bar" , height = 4 , aspect = .7)
plt.show()

#KUTU GRAFİĞİ
sns.boxplot(x = "sezon" , y = "boy" , data = veri)
plt.title('Farklı Sezonlarda Madalya Kazanmış Sporcuların Boy Dağılımları')
plt.show()

#ŞİMDİ CİNSİYETE GÖRE AYRIŞTIRMA YAPALIM
sns.boxplot(x = "sezon" , y = "boy" , hue = "cinsiyet" , data = veri , palette = "rocket")
plt.title('Farklı Sezonlarda Madalya Kazanmış Sporcuların Boy Dağılımları')
plt.show()

#BİRDEN FAZLA KATEGORİYE GÖRE AYRIŞTIRALIM
veri_geçici = veri.loc[:,["yaş" , "boy" , "kilo"]]
sns.boxplot(data = veri_geçici , palette = "Set3" , orient = "h") #ORİENT = "H"(HORİZONTAL(YATAY)) GRAFİK DURUŞU
plt.title('Yaş - Boy - Kilo Verilerine Göre Ayrıştırılmış Kutu Grafiği')
plt.show()

#ALTIN - GÜMÜŞ - BRONZ VE CİNSİYET OLARAK AYRIŞTIRILMIŞ GRAFİĞİ ÇİZMEYİ DENEYELİM
sns.catplot(x = "sezon" , y = "boy" , data = veri , hue = "cinsiyet" , col = "madalya" , kind = "box" , height = 4 , aspect = .7)
plt.title('Madalya - Cinsiyete Ayrıştırması İle Hzırlanan Sezon - Boy Kutu Grafiği')
plt.show()

#ISI HARİTASI
sns.heatmap(veri.corr(numeric_only = True) , annot = True , linewidths = .5 , fmt = '.1f') #ANNOT(ANNOTATİON) : BELİRTME LİNEWİDTHS:ÇİZGİ KALINLIKLARI
#FMT = '.1F' : NOKTADAN SONRA 1 BASAMAK GÖSTER
plt.show()

#KEMAN GRAFİĞİ
sns.violinplot(x = "sezon" , y = "boy" , data = veri)
plt.title('Sezon - Boy Keman Grafiği')
plt.show()

#KEMAN GRAFİĞİNİ CİNSİYETE GÖRE AYRIŞTIRALIM
sns.violinplot(x = "sezon" , y = "boy" , data = veri , hue = "cinsiyet")
plt.title('Sezon - Boy Keman Grafiği')
plt.grid(True)
plt.show()

#BU GRAFİĞİN İKİ YANI DA SİMETRİK OLDUĞU İÇİN YALNIZCA BİR TARAFINI GÖRMEMİZ YETECEKTİR ŞİMDİ DE BUNU AYARLAYALIM
sns.violinplot(x = "sezon" , y = "boy" , data = veri , hue = "cinsiyet" , split = True) #SPLİT FONKSİYONU İLE ASLINDA 4 PARÇA OLAN GRAFİĞİ 2 PARÇAYA İNDİRMİŞ OLDUK
plt.title('Sezon - Boy Keman Grafiği')
plt.grid(True)
plt.show()

#SEZON - BOY KEMAN GRAFİĞİNİN MADALYA TÜRLERİ VE CİNSİYETE GÖRE AYRIŞTIRILMIŞ HALİ
sns.catplot(x = "sezon" , y = "boy" , hue = "cinsiyet" , col = "madalya" , data = veri , kind = "violin" , split = True , height = 4 , aspect = .7)
plt.show()
