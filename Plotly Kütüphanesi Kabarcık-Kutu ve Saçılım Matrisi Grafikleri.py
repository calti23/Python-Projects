import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

import warnings
warnings.filterwarnings("ignore")

#PLOTLY KÜTÜPHANESİNİ İÇE AKTARIYORUZ
from plotly.offline import iplot , plot
import plotly as py
import plotly.graph_objs as go
import plotly.io as pio
import plotly.figure_factory as ff

veri = pd.read_csv("timesData.csv")

veri.rename(columns = {'world_rank' : 'dünya_sıralama' ,
                       'university_name' : 'üni_isim' ,
                       'country' : 'ülke' ,
                       'teaching' : 'öğretim' ,
                       'international' : 'uluslararası' ,
                       'research' : 'araştırma' ,
                       'citations' : 'alıntı' ,
                       'income' : 'gelir' ,
                       'total_score' : 'toplam_puan' ,
                       'num_students' : 'öğrenci_sayısı' ,
                       'student_staff_ratio' : 'öğrenci_çalışan_oranı' ,
                       'international_students' : 'uluslararası_öğrenci' ,
                       'female_male_ratio' : 'kadın_erkek_oranı' ,
                       'year' : 'yıl'
                       } , inplace = True)
print(veri.tail(3))

#KABARCIK GRAFİĞİ
veri2016 = veri[veri.yıl == 2016].iloc[:20 , :]
öğrenci_sayısı = [float(each.replace(',' , '.')) for each in veri2016.öğrenci_sayısı]
uluslararası_renk = [float(each) for each in veri2016.uluslararası]

data = [{'y' : veri2016.öğretim ,
         'x' : veri2016.dünya_sıralama , #KABARCIK BÜYÜKLÜĞÜ ÖĞRENCİ SAYISI
         'mode' : 'markers' , #RENK SKALASINA GÖRE DE ÖĞRETİM KALİTESİ BELİRLENİR
         'marker' : {'color' : uluslararası_renk ,
                     'size' : öğrenci_sayısı ,
                     'showscale' : True} ,
         "text" : veri2016.üni_isim}]
plot(data)

#KUTU GRAFİĞİ
veri2015 = veri[veri.yıl == 2015]
#İLK GRAFİK
çizgi1 = go.Box(y = veri2015.toplam_puan , name = '2015 Yılında Toplam Puan' ,
                marker = dict(color = 'rgba(255 , 86 , 4)'))
#İKİNCİ GRAFİK
çizgi2 = go.Box(y = veri2015.araştırma , name = '2015 Yılında Araştırma Puanı' ,
                marker = dict(color = 'rgba(4 , 86 , 255)'))
veri_ = [çizgi1 , çizgi2]
plot(veri_)

#SAÇILIM MATRİSİ GRAFİĞİ
veri_geçici = veri[veri.yıl == 2015]
veri2015 = veri_geçici.loc[:,["araştırma" , "uluslararası" , "toplam_puan"]]
veri2015["index"] = np.arange(1 , len(veri2015) + 1)

fig = ff.create_scatterplotmatrix(veri2015 , diag = 'box' , index = 'index' ,
                                  colormap = 'Jet' , colormap_type = 'cat' ,
                                  height = 700 , width = 700)
"""
ÖRNEK RENK HARİTALARI
'Greys', 'YlGnBu', 'Greens', 'YlOrRd', 'Bluered', 'RdBu',
'Reds', 'Blues', 'Picnic', 'Rainbow', 'Portland', 'Jet',
'Hot', 'Blackbody', 'Earth', 'Electric', 'Viridis', 'Cividis'
"""
plot(fig)
