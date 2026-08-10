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

#DÜNYA HARİTASI GRAFİĞİ
"""
KULLANILABİLİR RENK PALETLERİ
Twilight , IceFire , Edge , Phase , HSV , mrybm , mygbm
"""
veri2016 = veri[veri.yıl == 2016]
veri2016.ülke.value_counts()
#ABD DE 146 ÜNİVERSİTE BU SIRALAMADA OLDUĞU İÇİN BUNLARI TEKER TEKER AYIRALIM
ülkeye_göre_toplam_veriler = veri2016.groupby("ülke").sum(numeric_only=True) / 146
print(ülkeye_göre_toplam_veriler)

#İLK GRAFİK
çizgi1 = go.Choropleth(locations = ülkeye_göre_toplam_veriler.index ,
                       locationmode = 'country.names' ,
                       z = ülkeye_göre_toplam_veriler['araştırma'] ,
                       text = ülkeye_göre_toplam_veriler.index ,
                       autocolorscale = False , reversescale = True ,
                       colorscale = "iceFire" , marker = dict(line = dict(color = 'rgb(255 , 255 , 255)' , width = 1)) ,
                       colorbar = dict(title = 'Araştırma Puanı' , tickprefix = ''))
veri_ = [çizgi1]
yerleşim = go.Layout(title = "Ülkelerin Toplam Araştırma Puanları" ,
                     geo = dict(showframe = True , showlakes = False , showcoastlines = True ,
                                projection = dict(type = 'natural earth')))
#SHOWFRAME : ÇERÇEVE ÇİZİLSİN Mİ? #SHOWLAKES : HARİTADA VERİLERİ GÖSTERSİN Mİ? #SHOWCOASTLİNES : KIYI ŞERİTLERİNİ GÖSTERSİN Mİ?
#PROJECTİON : HARİTA PROJEKSİYON TİPİ
fig = dict(data = veri_ , layout = yerleşim)
plot(fig)

