import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from collections import Counter

import warnings
warnings.filterwarnings("ignore")

veri = pd.read_csv("new_athlete_events.csv")

#ORTAKLIK GRAFİĞİ
sns.jointplot(x = "kilo" , y = "boy" , hue  ="sezon" , kind = "kde" , data = veri)
plt.show()

#ORTAKLIK GRAFİĞİNİN BAŞKA BİR GÖSTERİLİŞİ
g = sns.JointGrid(data = veri , x = "kilo" , y = "boy")
g.plot_joint(sns.histplot)
g.plot_marginals(sns.boxplot) #MARJİNAL DEĞERLERİ DE GÖSTER
plt.show()

#ÇİFT/EŞ GRAFİĞİ
sns.pairplot(veri)
plt.show()

#ÇİFT/EŞ GRAFİĞİNİN BAŞKA BİR GÖSTERİLİŞİ
g = sns.PairGrid(veri)
g.map_upper(sns.histplot) #HARİTAMIZIN ÜST KISMI HİSTOGRAM GRAFİKLERİ İLE DOLU OLSUN
g.map_lower(sns.kdeplot , fill = True) #HARİTAMIZIN ALT KISMI İZOHİPS GRAFİKLERİ İLE DOLU OLSUN VE İÇLERİ DE DOLDURULSUN
g.map_diag(sns.histplot , kde = True) #DİAGONAL (1-1 , 2-2 , 3-3 , 4-4) HİSTOGRAM GRAFİKLERİ İLE DOLU OLSUN
plt.show()

#SAYMA GRAFİĞİ
#HANGİ ŞEHİRDE KAÇ TANE MADALYA VERİLDİĞİNİ GÖSTEREN SAYMA GRAFİĞİ
sns.countplot(x = "şehir" , data = veri)
plt.xticks(rotation = 90)
plt.show()
