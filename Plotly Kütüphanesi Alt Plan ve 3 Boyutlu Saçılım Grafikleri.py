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

#ALT PLAN GRAFİĞİ
veri2015 = veri[veri.yıl == 2015]
#İLK GRAFİK
çizgi1 = go.Scatter(x = veri2015.dünya_sıralama , y = veri2015.araştırma ,
                    name = '2015 Yılı Araştırma - Dünya Sıralaması Grafiği')
#İKİNCİ GRAFİK
çizgi2 = go.Scatter(x = veri2015.dünya_sıralama , y = veri2015.alıntı ,
                    xaxis = 'x2' , yaxis = 'y2' ,
                    name = '2015 Yılı Alıntılama - Dünya Sıralaması Grafiği') #AYIRT ETMEK İÇİN X/Y EKSENLERİNİN İSİMLERİNİ DEĞİŞTİRDİK
#ÜÇÜNCÜ GRAFİK
çizgi3 = go.Scatter(x = veri2015.dünya_sıralama , y = veri2015.gelir ,
                    xaxis = 'x3' , yaxis = 'y3' ,
                    name = '2015 Yılı Gelir - Dünya SıralamasıGrafiği')
#DÖRDÜNCÜ GRAFİK
çizgi4 = go.Scatter(x = veri2015.dünya_sıralama , y = veri2015.toplam_puan ,
                    xaxis = 'x4' , yaxis = 'y4' ,
                    name = '2015 Yılı Toplam Puan - Dünya Sıralaması Grafiği')

veri_ = [çizgi1 , çizgi2 , çizgi3 , çizgi4]
yerleşim = go.Layout(xaxis = dict(domain = [0 , 0.45]) , #DOMAİN İLE SAYFANIN ÜZERİNDEKİ BÖLGELERİ GRAFİKLER İÇİN AYIRDIK/PARSELLEDİK
                     xaxis2 = dict(domain = [0.55 , 1] , anchor = 'y2') , #ANCHOR : İLİŞKİLENDİRMEK
                     xaxis3 = dict(domain = [0 , 0.45] , anchor = 'y3') ,
                     xaxis4 = dict(domain = [0.55 , 1] , anchor = 'y4') ,
                     yaxis = dict(domain = [0 , 0.45]) ,
                     yaxis2 = dict(domain = [0 , 0.45] , anchor = 'x2') ,
                     yaxis3 = dict(domain = [0.55 , 1] , anchor = 'x3') ,
                     yaxis4 = dict(domain = [0.55 , 1] , anchor = 'x4') ,
                     title = 'Üniversite Sıralamalarına Göre Araştırma - Alıntı - Gelir - Toplam Puan Değerleri')
fig = go.Figure(data = veri_ , layout = yerleşim)
plot(fig , filename = 'Üniversite Sıralamalarına Göre Aaraştırma-Alıntı-Gelir-Toplam Puan Değerleri.html')

#3 BOYUTLU SAÇILIM GRAFİĞİ
çizgi1 = go.Scatter3D(x = veri2015.dünya_sıralama , y = veri2015.araştırma , z = veri2015.alıntı ,
                      mode = 'markers' , marker = dict(size = 10 , color = "seagreen") ,
                      opacity = .5) #OPACİTY : OPAKLIK
veri_ = [çizgi1]
yerleşim = go.Layout(margin = dict(l = 0 , r = 0 , b = 0 , t = 0))
fig = go.Figure(data = veri_ , layout = yerleşim)
plot(fig)

